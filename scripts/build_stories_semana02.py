"""Gera os cards de Story (4:5) pra cada post do Lote 2."""

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
    "post-01-mito-roubo": dict(
        tag="MITO OU VERDADE",
        title="Roubo residencial só<br>paga com <span class='hl'>arrombamento?</span>",
        photo=p("ref-pexels-doorlock.jpg"),
    ),
    "post-02-vale-a-pena-residencial": dict(
        tag="VALE A PENA?",
        title="Mitos que te fazem<br>pagar mais <span class='hl'>caro</span>",
        photo=None,
    ),
    "post-03-mito-vida-suicidio": dict(
        tag="MITO OU VERDADE",
        title="Seguro de vida cobre<br><span class='hl'>suicídio?</span>",
        photo=p("ref-pexels-contract.jpg"),
    ),
    "post-04-caso-real-doenca-preexistente": dict(
        tag="CASO ILUSTRATIVO",
        title="O exame que a<br>seguradora nunca <span class='hl'>pediu</span>",
        photo=p("ref-pexels-doctor.jpg"),
    ),
    "post-05-papo-corretor": dict(
        tag="PAPO DE CORRETOR",
        title="A receita parada na<br>sua <span class='hl'>carteira</span>",
        photo=None,
    ),
}


def main():
    for slug, cfg in STORIES.items():
        out_dir = os.path.join(CONTENT, "semana-02", slug)
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
