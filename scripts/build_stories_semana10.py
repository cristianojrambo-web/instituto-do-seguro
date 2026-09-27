"""Gera os cards de Story (4:5) pra cada post do Lote 10."""

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
    "post-01-mito-seguro-incendio-locacao": dict(
        tag="MITO OU VERDADE",
        title="Mora de aluguel? O seguro contra<br>incêndio do imóvel é <span class='hl'>obrigação<br>sua</span>, não do dono?",
        photo=p("ref-pexels-house.jpg"),
    ),
    "post-02-mito-seguro-rural-clima": dict(
        tag="MITO OU VERDADE",
        title="Geada, seca ou granizo — o seguro<br>rural cobre <span class='hl'>automaticamente</span><br>o prejuízo?",
        photo=p("ref-pexels-colheitadeira.jpg"),
    ),
    "post-03-vale-a-pena-prestamista": dict(
        tag="VALE A PENA?",
        title="Seguro Prestamista: o seguro que<br>quita sua dívida — <span class='hl'>vale a pena</span><br>mesmo?",
        photo=None,
    ),
    "post-04-caso-real-transporte-cargas": dict(
        tag="CASO REAL",
        title="Caminhão tombou com a carga toda<br>— quem <span class='hl'>paga o prejuízo</span>?",
        photo=p("ref-pexels-crash.jpg"),
    ),
    "post-05-papo-corretor-cnsp-493": dict(
        tag="PAPO DE CORRETOR",
        title="Virou <span class='hl'>dever formal</span> se atualizar<br>— pela 1ª vez na história do CNSP",
        photo=None,
    ),
}


def main():
    for slug, cfg in STORIES.items():
        out_dir = os.path.join(CONTENT, "semana-10", slug)
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
    src = os.path.join(CONTENT, "semana-10", "post-01-mito-seguro-incendio-locacao", "story.jpg")
    dst_dir = os.path.join(CONTENT, "semana-10", "post-06-teste-domingo-seguro-incendio-locacao")
    os.makedirs(dst_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(dst_dir, "story.jpg"))
    print("post-06-teste-domingo-seguro-incendio-locacao: story.jpg gerado (copiado do post-01)")


if __name__ == "__main__":
    main()
