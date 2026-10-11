"""Gera os cards de Story (4:5) pra cada post do Lote 12."""

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
    "post-01-mito-seguro-vida-inventario": dict(
        tag="MITO OU VERDADE",
        title="O dinheiro do seguro de vida <span class='hl'>fica<br>preso no inventário</span>?",
        photo=p("ref-pexels-house.jpg"),
    ),
    "post-02-mito-seguro-celular": dict(
        tag="MITO OU VERDADE",
        title="O seguro do celular cobre se levarem<br>do bolso <span class='hl'>sem você ver</span>?",
        photo=p("ref-pexels-rideapp.jpg"),
    ),
    "post-03-vale-a-pena-seguro-bicicleta": dict(
        tag="VALE A PENA?",
        title="Seguro de bicicleta e bike elétrica:<br><span class='hl'>vale a pena</span>?",
        photo=None,
    ),
    "post-04-caso-pratico-sub-rogacao": dict(
        tag="CASO PRÁTICO",
        title="Bateram no seu carro e a seguradora pagou:<br><span class='hl'>o culpado paga o quê</span>?",
        photo=p("ref-pexels-crash.jpg"),
    ),
    "post-05-papo-corretor-numeros-cnseg-2026": dict(
        tag="PAPO DE CORRETOR",
        title="O que os números da <span class='hl'>CNseg</span><br>dizem pro corretor em 2026",
        photo=None,
    ),
}


def main():
    for slug, cfg in STORIES.items():
        out_dir = os.path.join(CONTENT, "semana-12", slug)
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
    src = os.path.join(CONTENT, "semana-12", "post-01-mito-seguro-vida-inventario", "story.jpg")
    dst_dir = os.path.join(CONTENT, "semana-12", "post-06-teste-domingo-seguro-vida-inventario")
    os.makedirs(dst_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(dst_dir, "story.jpg"))
    print("post-06-teste-domingo-seguro-vida-inventario: story.jpg gerado (copiado do post-01)")


if __name__ == "__main__":
    main()
