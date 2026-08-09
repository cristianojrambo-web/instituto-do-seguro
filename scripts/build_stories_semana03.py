"""Gera os cards de Story (4:5) pra cada post do Lote 3."""

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
    "post-01-mito-seguro-saude": dict(
        tag="MITO OU VERDADE",
        title="Seguro saúde protege<br>menos que <span class='hl'>plano de saúde?</span>",
        photo=p("ref-pexels-doctor.jpg"),
    ),
    "post-02-mito-seguro-viagem": dict(
        tag="MITO OU VERDADE",
        title="Seguro viagem só serve<br>pro <span class='hl'>exterior?</span>",
        photo=None,
    ),
    "post-03-vale-a-pena-saude": dict(
        tag="VALE A PENA?",
        title="Os mitos que travam<br>a decisão do <span class='hl'>seguro saúde</span>",
        photo=None,
    ),
    "post-04-caso-real-carencia-urgencia": dict(
        tag="ATENÇÃO",
        title="Negaram sua urgência<br>por <span class='hl'>carência?</span>",
        photo=p("ref-pexels-contract.jpg"),
    ),
    "post-05-papo-corretor-viagem": dict(
        tag="PAPO DE CORRETOR",
        title="O ramo que mais cresce<br>e quase ninguém <span class='hl'>vende</span>",
        photo=None,
    ),
}


def main():
    for slug, cfg in STORIES.items():
        out_dir = os.path.join(CONTENT, "semana-03", slug)
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
