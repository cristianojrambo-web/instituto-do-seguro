"""Gera os cards de Story (1080x1920) pra cada post do Lote 1, um por post."""

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
    "post-00-apresentacao": dict(
        tag="INSTITUTO DO SEGURO",
        title="Seguro de todos os<br>ramos, sem <span class='hl'>segurês</span>",
        photo=p("ref-pexels-house.jpg"),
    ),
    "post-01-vale-a-pena-auto": dict(
        tag="VALE A PENA?",
        title="Seguro Auto:<br>4 cláusulas que<br>ninguém <span class='hl'>lê</span>",
        photo=None,
    ),
    "post-02-mito-enchente": dict(
        tag="MITO OU VERDADE",
        title="Seu seguro cobre<br><span class='hl'>enchente?</span>",
        photo=p("ref-pexels-rain.jpg"),
    ),
    "post-03-caso-real": dict(
        tag="CASO ILUSTRATIVO",
        title="O detalhe que pode<br><span class='hl'>zerar</span> sua indenização",
        photo=p("ref-pexels-crash.jpg"),
    ),
    "post-04-papo-corretor": dict(
        tag="PAPO DE CORRETOR",
        title="2 dados que valem<br>mais que <span class='hl'>curso</span>",
        photo=None,
    ),
}


def main():
    for slug, cfg in STORIES.items():
        out_dir = os.path.join(CONTENT, "semana-01-v2", slug)
        os.makedirs(out_dir, exist_ok=True)
        html = story_card(LOGO, cfg["tag"], cfg["title"], photo_path=cfg["photo"])
        html_path = os.path.join(out_dir, "story.html")
        png_path = os.path.join(out_dir, "story.png")
        jpg_path = os.path.join(out_dir, "story.jpg")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        render(html_path, png_path, width=1080, height=1350)
        Image.open(png_path).convert("RGB").save(jpg_path, "JPEG", quality=92)
        print(f"{slug}: story.jpg gerado (4:5, dentro da proporção exigida pela API)")


if __name__ == "__main__":
    main()
