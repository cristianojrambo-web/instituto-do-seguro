"""Gera os cards de Story (4:5) pra cada post do Lote 6."""

import os
import shutil
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
from templates import story_card  # noqa: E402
from render_html import render  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
ASSETS = os.path.join(ROOT, "content", "assets")
LOGO = os.path.join(CONTENT, "logo.png").replace("\\", "/")


def p(name):
    return os.path.join(ASSETS, name).replace("\\", "/")


STORIES = {
    "post-01-mito-vida-esporte-radical": dict(
        tag="MITO OU VERDADE",
        title="Esporte radical<br><span class='hl'>anula</span> o seguro de vida?",
        photo=None,
    ),
    "post-02-mito-moto-acessorios": dict(
        tag="MITO OU VERDADE",
        title="Seguro de moto cobre<br><span class='hl'>capacete</span> roubado?",
        photo=p("ref-pexels-doorlock.jpg"),
    ),
    "post-03-vale-a-pena-viagem": dict(
        tag="VALE A PENA?",
        title="Seguro viagem, mesmo<br><span class='hl'>perto</span> de casa",
        photo=p("ref-pexels-travel.jpg"),
    ),
    "post-04-caso-real-imovel-fechado": dict(
        tag="ATENÇÃO",
        title="Casa fechada por muito<br>tempo <span class='hl'>zera</span> o seguro?",
        photo=p("ref-pexels-house.jpg"),
    ),
    "post-05-papo-corretor-cyber": dict(
        tag="PAPO DE CORRETOR",
        title="O ramo que mais<br><span class='hl'>cresce</span> agora",
        photo=None,
    ),
}


def main():
    for slug, cfg in STORIES.items():
        out_dir = os.path.join(CONTENT, "semana-06", slug)
        os.makedirs(out_dir, exist_ok=True)
        html = story_card(LOGO, cfg["tag"], cfg["title"], photo_path=cfg["photo"])
        html_path = os.path.join(out_dir, "story.html")
        png_path = os.path.join(out_dir, "story.png")
        jpg_path = os.path.join(out_dir, "story.jpg")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        render(html_path, png_path, width=1080, height=1350)
        Image.open(png_path).convert("RGB").save(jpg_path, "JPEG", quality=92)
        print(f"{slug}: story.jpg gerado")

    # Post 6 (teste de domingo) reaproveita o story do Post 4 (mesmo pilar/tema)
    src = os.path.join(CONTENT, "semana-06", "post-04-caso-real-imovel-fechado", "story.jpg")
    dst_dir = os.path.join(CONTENT, "semana-06", "post-06-teste-domingo-imovel-fechado")
    os.makedirs(dst_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(dst_dir, "story.jpg"))
    print("post-06-teste-domingo-imovel-fechado: story.jpg gerado (copiado do post-04)")


if __name__ == "__main__":
    main()
