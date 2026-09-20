"""Gera os cards de Story (4:5) pra cada post do Lote 9."""

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
    "post-01-mito-buraco-via": dict(
        tag="MITO OU VERDADE",
        title="Bateu num buraco e estourou<br>o pneu? Esse prejuízo é<br><span class='hl'>só seu</span> pra resolver?",
        photo=p("ref-pexels-bmw-damaged.jpg"),
    ),
    "post-02-mito-vida-portabilidade": dict(
        tag="MITO OU VERDADE",
        title="Ao ser demitido, o seguro de<br>vida em grupo <span class='hl'>acaba na hora</span><br>pra sempre?",
        photo=p("ref-pexels-contract.jpg"),
    ),
    "post-03-vale-a-pena-previdencia": dict(
        tag="VALE A PENA?",
        title="Previdência privada: PGBL<br>ou VGBL — o que realmente<br><span class='hl'>vale a pena</span>?",
        photo=None,
    ),
    "post-04-caso-real-endereco-nao-comunicado": dict(
        tag="CASO REAL",
        title="Motorista mudou de cidade,<br>manteve endereço antigo —<br>carro foi <span class='hl'>roubado</span>",
        photo=p("ref-pexels-navigation.jpg"),
    ),
    "post-05-papo-corretor-seguro-garantia": dict(
        tag="PAPO DE CORRETOR",
        title="O ramo que cresce <span class='hl'>13,6%</span><br>em 2026 e pouco corretor<br>ainda vende",
        photo=None,
    ),
}


def main():
    for slug, cfg in STORIES.items():
        out_dir = os.path.join(CONTENT, "semana-09", slug)
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
    src = os.path.join(CONTENT, "semana-09", "post-01-mito-buraco-via", "story.jpg")
    dst_dir = os.path.join(CONTENT, "semana-09", "post-06-teste-domingo-buraco-via")
    os.makedirs(dst_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(dst_dir, "story.jpg"))
    print("post-06-teste-domingo-buraco-via: story.jpg gerado (copiado do post-01)")


if __name__ == "__main__":
    main()
