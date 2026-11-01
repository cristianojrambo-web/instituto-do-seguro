"""Gera os cards de Story (4:5) pra cada post do Lote 15."""

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
    "post-01-mito-carro-reserva-guincho": dict(
        tag="MITO OU VERDADE",
        title="Todo seguro auto inclui <span class='hl'>carro<br>reserva</span> e guincho ilimitado?",
        photo=p("ref-pexels-crash.jpg"),
    ),
    "post-02-mito-seguro-vida-cotas-beneficiarios": dict(
        tag="MITO OU VERDADE",
        title="Beneficiário morreu? O outro <span class='hl'>fica<br>com tudo</span>?",
        photo=p("ref-pexels-contract.jpg"),
    ),
    "post-03-vale-a-pena-seguro-energia-solar": dict(
        tag="VALE A PENA?",
        title="Seguro pra energia solar:<br><span class='hl'>vale a pena</span>?",
        photo=None,
    ),
    "post-04-caso-pratico-vazamento-subito-gradual": dict(
        tag="CASO PRÁTICO",
        title="Cano vazou e o seguro<br><span class='hl'>não pagou</span>. Por quê?",
        photo=p("ref-pexels-house.jpg"),
    ),
    "post-05-papo-corretor-iof-vgbl-tabela-ir": dict(
        tag="PAPO DE CORRETOR",
        title="IOF no VGBL e a escolha da<br><span class='hl'>tabela de IR</span>",
        photo=None,
    ),
}


def main():
    for slug, cfg in STORIES.items():
        out_dir = os.path.join(CONTENT, "semana-15", slug)
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
    src = os.path.join(CONTENT, "semana-15", "post-02-mito-seguro-vida-cotas-beneficiarios", "story.jpg")
    dst_dir = os.path.join(CONTENT, "semana-15", "post-06-teste-domingo-seguro-vida-cotas-beneficiarios")
    os.makedirs(dst_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(dst_dir, "story.jpg"))
    print("post-06-teste-domingo-seguro-vida-cotas-beneficiarios: story.jpg gerado (copiado do post-02)")


if __name__ == "__main__":
    main()
