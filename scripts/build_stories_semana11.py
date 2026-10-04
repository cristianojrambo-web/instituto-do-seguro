"""Gera os cards de Story (4:5) pra cada post do Lote 11."""

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
    "post-01-mito-seguro-condominio": dict(
        tag="MITO OU VERDADE",
        title="O seguro do condomínio já protege<br>o <span class='hl'>interior do seu apartamento</span>?",
        photo=p("ref-pexels-house.jpg"),
    ),
    "post-02-mito-dpvat-spvat": dict(
        tag="MITO OU VERDADE",
        title="O DPVAT voltou e você já <span class='hl'>paga<br>junto com o licenciamento</span>?",
        photo=p("ref-pexels-bmw-damaged.jpg"),
    ),
    "post-03-vale-a-pena-seguro-fianca": dict(
        tag="VALE A PENA?",
        title="Seguro-fiança no aluguel: sem fiador,<br>sem depósito — <span class='hl'>vale a pena</span>?",
        photo=None,
    ),
    "post-04-caso-pratico-prazo-sinistro": dict(
        tag="CASO PRÁTICO",
        title="Avisou o sinistro e a seguradora<br><span class='hl'>sumiu por 40 dias</span> — pode?",
        photo=p("ref-pexels-contract.jpg"),
    ),
    "post-05-papo-corretor-susep-cp-05-2026": dict(
        tag="PAPO DE CORRETOR",
        title="Susep quer que o mercado <span class='hl'>reporte</span><br>risco climático como empresa grande",
        photo=None,
    ),
}


def main():
    for slug, cfg in STORIES.items():
        out_dir = os.path.join(CONTENT, "semana-11", slug)
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
    src = os.path.join(CONTENT, "semana-11", "post-01-mito-seguro-condominio", "story.jpg")
    dst_dir = os.path.join(CONTENT, "semana-11", "post-06-teste-domingo-seguro-condominio")
    os.makedirs(dst_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(dst_dir, "story.jpg"))
    print("post-06-teste-domingo-seguro-condominio: story.jpg gerado (copiado do post-01)")


if __name__ == "__main__":
    main()
