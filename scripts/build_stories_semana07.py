"""Gera os cards de Story (4:5) pra cada post do Lote 7."""

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
    "post-01-mito-perda-total-fipe": dict(
        tag="MITO OU VERDADE",
        title="Seguro sempre paga<br><span class='hl'>100% da FIPE</span> na perda total?",
        photo=p("ref-pexels-crash.jpg"),
    ),
    "post-02-mito-corretor-fantasma": dict(
        tag="MITO OU VERDADE",
        title="Boleto de seguro por<br><span class='hl'>WhatsApp</span> é sempre seguro?",
        photo=p("ref-pexels-contract.jpg"),
    ),
    "post-03-vale-a-pena-vida-grupo-individual": dict(
        tag="VALE A PENA?",
        title="Seguro de vida da empresa<br><span class='hl'>já basta</span>?",
        photo=None,
    ),
    "post-04-caso-real-dano-eletrico": dict(
        tag="CASO REAL",
        title="Queda de energia queimou<br>a geladeira — e o <span class='hl'>seguro</span> resolveu",
        photo=p("ref-pexels-house.jpg"),
    ),
    "post-05-papo-corretor-frota": dict(
        tag="PAPO DE CORRETOR",
        title="Cliente PJ pagando<br><span class='hl'>mais caro</span> sem precisar",
        photo=None,
    ),
}


def main():
    for slug, cfg in STORIES.items():
        out_dir = os.path.join(CONTENT, "semana-07", slug)
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

    # Post 6 (teste de domingo) reaproveita o story do Post 2 (mesmo pilar/tema)
    src = os.path.join(CONTENT, "semana-07", "post-02-mito-corretor-fantasma", "story.jpg")
    dst_dir = os.path.join(CONTENT, "semana-07", "post-06-teste-domingo-corretor-fantasma")
    os.makedirs(dst_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(dst_dir, "story.jpg"))
    print("post-06-teste-domingo-corretor-fantasma: story.jpg gerado (copiado do post-02)")


if __name__ == "__main__":
    main()
