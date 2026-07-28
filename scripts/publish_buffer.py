"""
Publica um carrossel no Instagram via API do Buffer.

Uso:
    python scripts/publish_buffer.py --post content/semana-01-v2/post-00-apresentacao \
        --caption "texto da legenda" --channel instagram [--due "2026-07-29T19:00:00-03:00"]

Sem --due, publica imediatamente (shareNow). Com --due, agenda pro horário informado
(ISO 8601 com fuso horário).

As imagens são hospedadas temporariamente no litterbox.catbox.moe (anônimo, sem conta)
só o tempo suficiente pro Buffer buscar e processar — não é armazenamento permanente.
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
LITTERBOX_URL = "https://litterbox.catbox.moe/resources/internals/api.php"

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


def upload_temp(image_path, retention="72h"):
    with open(image_path, "rb") as f:
        resp = requests.post(
            LITTERBOX_URL,
            data={"reqtype": "fileupload", "time": retention},
            files={"fileToUpload": f},
            timeout=60,
        )
    resp.raise_for_status()
    url = resp.text.strip()
    if not url.startswith("http"):
        raise RuntimeError(f"Falha no upload temporário: {resp.text}")
    return url


def create_post(channel_id, text, image_urls, due_at=None, draft=False, story=False):
    assets = [{"image": {"url": url}} for url in image_urls]
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
                    "type": "story" if story else "post",
                    "shouldShareToFeed": False if story else True,
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
    args = parser.parse_args()

    if not API_KEY:
        sys.exit("Falta BUFFER_API_KEY em config/.env")

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

    print(f"Subindo {len(slide_paths)} imagens pra hospedagem temporária...")
    image_urls = []
    for path in slide_paths:
        url = upload_temp(path)
        print(f"  {os.path.basename(path)} -> {url}")
        image_urls.append(url)
        time.sleep(0.5)

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
