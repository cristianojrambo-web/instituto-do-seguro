"""Gera os cards de Story (4:5) pra cada post do Lote 4."""

import os
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
    "post-01-mito-empresarial": dict(
        tag="MITO OU VERDADE",
        title="Empresa pequena não<br>precisa de <span class='hl'>seguro empresarial?</span>",
        photo=p("ref-pexels-contract.jpg"),
    ),
    "post-02-mito-auto-terceiro-nao-identificado": dict(
        tag="MITO OU VERDADE",
        title="Bateram e fugiram —<br>seu seguro <span class='hl'>cobre?</span>",
        photo=p("ref-pexels-bmw-damaged.jpg"),
    ),
    "post-03-vale-a-pena-equipamentos-agricolas": dict(
        tag="VALE A PENA?",
        title="Seguro de equipamentos<br><span class='hl'>agrícolas</span>",
        photo=p("ref-pexels-colheitadeira.jpg"),
    ),
    "post-04-caso-real-mora-premio": dict(
        tag="ATENÇÃO",
        title="Atrasou uma parcela?<br>Isso pode custar sua <span class='hl'>indenização</span>",
        photo=p("ref-pexels-house.jpg"),
    ),
    "post-05-papo-corretor-previdencia": dict(
        tag="PAPO DE CORRETOR",
        title="O produto de<br><span class='hl'>R$1,8 trilhão</span> parado na mesa",
        photo=None,
    ),
}


def main():
    for slug, cfg in STORIES.items():
        out_dir = os.path.join(CONTENT, "semana-04", slug)
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


if __name__ == "__main__":
    main()
