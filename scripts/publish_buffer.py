"""
Publica um carrossel no Instagram via API do Buffer.

Uso:
    python scripts/publish_buffer.py --post content/semana-01-v2/post-00-apresentacao \
        --caption "texto da legenda" --channel instagram [--due "2026-07-29T19:00:00-03:00"]

Sem --due, publica imediatamente (shareNow). Com --due, agenda pro horário informado
(ISO 8601 com fuso horário) — o Buffer publica sozinho nesse horário, sem depender de
nenhum gatilho externo no momento exato (schedulingType=automatic).

As imagens são referenciadas via URL pública e PERMANENTE do GitHub (raw.githubusercontent.com,
repositório público) — não usa mais hospedagem temporária (litterbox), porque posts agendados
com muita antecedência (ex: 5 dias) passavam do prazo de expiração do link temporário antes do
Buffer conseguir buscar a imagem na hora certa. Requer que o arquivo já esteja commitado e
pusheado no repositório.
"""

import argparse
import glob
import os
import sys
import time

import requests
from dotenv import load_dotenv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(ROOT, "config", ".env"))

API_KEY = os.environ.get("BUFFER_API_KEY")
GRAPHQL_URL = "https://api.buffer.com/graphql"
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/cristianojrambo-web/instituto-do-seguro/main"

CHANNEL_IDS = {
    "instagram": "6a68eeba4b2d03035f58a0e6",
    "facebook": "6a68eedf4b2d03035f58a6f2",
}


def gql(query, variables=None):
    resp = requests.post(
        GRAPHQL_URL,
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        json={"query": query, "variables": variables or {}},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        raise RuntimeError(f"Buffer API error: {data['errors']}")
    return data["data"]


def github_raw_url(local_path):
    """Converte um caminho local (dentro do repo) na URL pública permanente do GitHub.
    Falha alto e claro se o arquivo não existir lá (esqueceu de commitar/pushear)."""
    rel_path = os.path.relpath(os.path.abspath(local_path), ROOT).replace("\\", "/")
    url = f"{GITHUB_RAW_BASE}/{rel_path}"
    resp = requests.head(url, timeout=15)
    if resp.status_code != 200:
        raise RuntimeError(
            f"Imagem não encontrada no GitHub (status {resp.status_code}): {url}\n"
            f"Rodou 'git add -A && git commit && git push' depois de gerar/editar esse arquivo?"
        )
    return url


def create_post(channel_id, text, image_urls=None, video_url=None, due_at=None, draft=False,
                 story=False, reel=False, ai_generated=False):
    """video_url + reel=True publica como Reels (a API do Instagram exige video de verdade
    pra Reels, nao aceita multiplas imagens como slideshow — isso so existe dentro do app).
    ai_generated=True marca o post com isAiGenerated=true, pro rotulo "Feito com IA" do
    Instagram — usar sempre que o post tiver audio narrado por IA (ex: Kokoro TTS) ou video
    fotorrealista gerado por IA, conforme a politica de divulgacao obrigatoria da Meta."""
    if video_url:
        assets = [{"video": {"url": video_url}}]
        post_type = "reel" if reel else "post"
    else:
        assets = [{"image": {"url": url}} for url in image_urls]
        post_type = "story" if story else "post"

    mode = "customScheduled" if due_at else "shareNow"
    scheduling_type = "automatic"

    variables = {
        "input": {
            "channelId": channel_id,
            "text": text,
            "assets": assets,
            "mode": mode,
            "schedulingType": scheduling_type,
            "needsApproval": False,
            "saveToDraft": draft,
            "metadata": {
                "instagram": {
                    "type": post_type,
                    "shouldShareToFeed": False if story else True,
                    "isAiGenerated": ai_generated,
                }
            },
        }
    }
    if due_at:
        variables["input"]["dueAt"] = due_at

    mutation = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        ... on PostActionSuccess { post { id status } }
        ... on NotFoundError { message }
        ... on UnauthorizedError { message }
        ... on UnexpectedError { message }
        ... on RestProxyError { code link message }
        ... on LimitReachedError { message }
        ... on InvalidInputError { message }
      }
    }
    """
    return gql(mutation, variables)


def check_final_status(post_id, attempts=6, delay=5):
    """Confere o status real do post algumas vezes — 'sending'/'sent' na resposta do
    createPost NÃO garante sucesso (a Instagram pode rejeitar depois, ex: erro 400)."""
    query = """
    query CheckPost($input: PostInput!) {
      post(input: $input) { id status error { message rawError } }
    }
    """
    for _ in range(attempts):
        time.sleep(delay)
        data = gql(query, {"input": {"id": post_id}})
        status = data["post"]["status"]
        if status not in ("sending", "pending", "processing"):
            return data["post"]
    return data["post"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--post", required=True, help="Pasta do post (ex: content/semana-01-v2/post-00-apresentacao)")
    parser.add_argument("--caption", required=True, help="Legenda do post")
    parser.add_argument("--channel", default="instagram", choices=list(CHANNEL_IDS))
    parser.add_argument("--due", default=None, help="ISO 8601 com fuso (ex: 2026-07-29T19:00:00-03:00). Sem isso, publica agora.")
    parser.add_argument("--draft", action="store_true", help="Salva como rascunho no Buffer em vez de publicar/agendar.")
    parser.add_argument("--story", action="store_true", help="Publica story.png do post como Story (imagem única, sem link/adesivo).")
    parser.add_argument("--reel", action="store_true", help="Publica reel.mp4 do post como Reels (video real, nao slideshow).")
    parser.add_argument("--ai-generated", action="store_true", help="Marca o post com isAiGenerated=true (rotulo 'Feito com IA' do Instagram) — usar quando o post tiver audio/video gerado por IA (ex: narração Kokoro TTS).")
    args = parser.parse_args()

    if not API_KEY:
        sys.exit("Falta BUFFER_API_KEY em config/.env")

    if args.reel:
        reel_path = os.path.join(args.post, "reel.mp4")
        if not os.path.exists(reel_path):
            sys.exit(f"reel.mp4 não encontrado em {args.post}")
        video_url = github_raw_url(reel_path)
        print(f"Resolvendo vídeo via GitHub (URL permanente)...\n  reel.mp4 -> {video_url}")
        channel_id = CHANNEL_IDS[args.channel]
        print("Criando post no Buffer (Reels)...")
        result = create_post(channel_id, args.caption, video_url=video_url, due_at=args.due,
                              draft=args.draft, reel=True, ai_generated=args.ai_generated)
        print("Post criado:", result)
        payload = result.get("createPost", {})
        if "message" in payload:
            sys.exit(f"ERRO ao criar post: {payload['message']}")
        post_id = payload["post"]["id"]
        if args.draft:
            print("Rascunho salvo — não publicado, não há status final pra checar.")
            return
        print("Confirmando status real da publicação (não confiar em 'sending')...")
        final = check_final_status(post_id)
        if final["status"] == "error":
            err = final.get("error") or {}
            sys.exit(f"ERRO: post foi rejeitado após a criação. status=error detalhe={err.get('rawError') or err.get('message')}")
        print(f"Status final confirmado: {final['status']}")
        return

    if args.story:
        story_path = os.path.join(args.post, "story.jpg")
        if not os.path.exists(story_path):
            sys.exit(f"story.jpg não encontrado em {args.post}")
        slide_paths = [story_path]
    else:
        slide_paths = sorted(glob.glob(os.path.join(args.post, "slide-*.png")))
        if not slide_paths:
            sys.exit(f"Nenhum slide-*.png encontrado em {args.post}")
        if len(slide_paths) > 10:
            sys.exit(f"Buffer só aceita até 10 imagens por carrossel ({len(slide_paths)} encontradas)")

    print(f"Resolvendo {len(slide_paths)} imagens via GitHub (URL permanente)...")
    image_urls = []
    for path in slide_paths:
        url = github_raw_url(path)
        print(f"  {os.path.basename(path)} -> {url}")
        image_urls.append(url)

    channel_id = CHANNEL_IDS[args.channel]
    print("Criando post no Buffer...")
    result = create_post(channel_id, args.caption, image_urls, due_at=args.due, draft=args.draft, story=args.story)
    print("Post criado:", result)

    payload = result.get("createPost", {})
    if "message" in payload:
        sys.exit(f"ERRO ao criar post: {payload['message']}")

    post_id = payload["post"]["id"]

    if args.draft:
        print("Rascunho salvo — não publicado, não há status final pra checar.")
        return

    print("Confirmando status real da publicação (não confiar em 'sending')...")
    final = check_final_status(post_id)
    if final["status"] == "error":
        err = final.get("error") or {}
        sys.exit(f"ERRO: post foi rejeitado após a criação. status=error detalhe={err.get('rawError') or err.get('message')}")
    print(f"Status final confirmado: {final['status']}")


if __name__ == "__main__":
    main()
