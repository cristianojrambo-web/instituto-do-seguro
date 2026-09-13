"""Gera os cards de Story (4:5) pra cada post do Lote 8."""

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
    "post-01-mito-estacionamento": dict(
        tag="MITO OU VERDADE",
        title="Carro roubado em<br>estacionamento pago: precisa<br><span class='hl'>processar</span> pra ser pago?",
        photo=p("ref-pexels-flood.jpg"),
    ),
    "post-02-mito-residencial-vendaval": dict(
        tag="MITO OU VERDADE",
        title="Árvore caiu na sua casa<br>num temporal — o seguro<br><span class='hl'>residencial</span> cobre?",
        photo=p("ref-pexels-house.jpg"),
    ),
    "post-03-vale-a-pena-moto": dict(
        tag="VALE A PENA?",
        title="Seguro de moto: vale o<br>preço ou é <span class='hl'>dinheiro jogado fora</span>?",
        photo=None,
    ),
    "post-04-caso-real-agravamento-risco": dict(
        tag="CASO REAL",
        title="Empresa avisou a seguradora<br>antes de mudar o risco —<br>e o seguro <span class='hl'>continuou valendo</span>",
        photo=p("ref-pexels-contract.jpg"),
    ),
    "post-05-papo-corretor-marco-legal": dict(
        tag="PAPO DE CORRETOR",
        title="O que muda na sua rotina<br>com a <span class='hl'>Lei 15.040/2024</span>",
        photo=None,
    ),
}


def main():
    for slug, cfg in STORIES.items():
        out_dir = os.path.join(CONTENT, "semana-08", slug)
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
    src = os.path.join(CONTENT, "semana-08", "post-01-mito-estacionamento", "story.jpg")
    dst_dir = os.path.join(CONTENT, "semana-08", "post-06-teste-domingo-estacionamento")
    os.makedirs(dst_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(dst_dir, "story.jpg"))
    print("post-06-teste-domingo-estacionamento: story.jpg gerado (copiado do post-01)")


if __name__ == "__main__":
    main()
