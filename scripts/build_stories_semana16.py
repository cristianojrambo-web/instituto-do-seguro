"""Gera os cards de Story (4:5) pra cada post do Lote 16."""

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
    "post-01-mito-bonus-seguro-auto": dict(
        tag="MITO OU VERDADE",
        title="O <span class='hl'>bônus</span> do seguro vai<br>junto com o carro?",
        photo=p("ref-pexels-rideapp.jpg"),
    ),
    "post-02-mito-seguro-viagem-cancelamento": dict(
        tag="MITO OU VERDADE",
        title="Seguro viagem devolve se você<br><span class='hl'>desistir de viajar</span>?",
        photo=p("ref-pexels-travel.jpg"),
    ),
    "post-03-vale-a-pena-garantia-estendida": dict(
        tag="VALE A PENA?",
        title="Garantia estendida:<br><span class='hl'>vale a pena</span>?",
        photo=None,
    ),
    "post-04-caso-pratico-arvore-granizo-compreensiva": dict(
        tag="CASO PRÁTICO",
        title="Árvore caiu no carro e o seguro<br><span class='hl'>não pagou</span>. Por quê?",
        photo=p("ref-pexels-rain.jpg"),
    ),
    "post-05-papo-corretor-reforma-tributaria-ibs-cbs": dict(
        tag="PAPO DE CORRETOR",
        title="Reforma tributária:<br>o que muda pra <span class='hl'>corretoras</span>",
        photo=None,
    ),
}


def main():
    for slug, cfg in STORIES.items():
        out_dir = os.path.join(CONTENT, "semana-16", slug)
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

    # Post 6 (teste de domingo) reaproveita o story do Post 1 (mesmo pilar/tema)
    src = os.path.join(CONTENT, "semana-16", "post-01-mito-bonus-seguro-auto", "story.jpg")
    dst_dir = os.path.join(CONTENT, "semana-16", "post-06-teste-domingo-bonus-seguro-auto")
    os.makedirs(dst_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(dst_dir, "story.jpg"))
    print("post-06-teste-domingo-bonus-seguro-auto: story.jpg gerado (copiado do post-01)")


if __name__ == "__main__":
    main()
