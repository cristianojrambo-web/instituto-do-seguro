"""Gera os cards de Story (4:5) pra cada post do Lote 18."""

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
    "post-01-mito-carencia-seguro-de-vida": dict(
        tag="MITO OU VERDADE",
        title="Seguro de vida:<br>no começo <span class='hl'>não paga nada</span>?",
        photo=p("ref-pexels-contract.jpg"),
    ),
    "post-02-mito-protecao-veicular-x-seguro-auto": dict(
        tag="MITO OU VERDADE",
        title="Proteção veicular é<br>a mesma coisa que<br><span class='hl'>seguro auto</span>?",
        photo=p("ref-pexels-crash.jpg"),
    ),
    "post-03-vale-a-pena-seguro-empresarial-mei": dict(
        tag="VALE A PENA?",
        title="Seguro empresarial pra MEI:<br><span class='hl'>vale a pena</span>?",
        photo=None,
    ),
    "post-04-caso-pratico-mala-extraviada": dict(
        tag="CASO PRÁTICO",
        title="A mala não chegou<br>na viagem.<br><span class='hl'>E agora?</span>",
        photo=p("ref-pexels-travel.jpg"),
    ),
    "post-05-papo-corretor-pgbl-dezembro": dict(
        tag="PAPO DE CORRETOR",
        title="Dezembro é o mês<br>do <span class='hl'>PGBL</span>",
        photo=None,
    ),
}


def main():
    for slug, cfg in STORIES.items():
        out_dir = os.path.join(CONTENT, "semana-18", slug)
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
    src = os.path.join(CONTENT, "semana-18", "post-02-mito-protecao-veicular-x-seguro-auto", "story.jpg")
    dst_dir = os.path.join(CONTENT, "semana-18", "post-06-teste-domingo-protecao-veicular-x-seguro-auto")
    os.makedirs(dst_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(dst_dir, "story.jpg"))
    print("post-06-teste-domingo-protecao-veicular-x-seguro-auto: story.jpg gerado (copiado do post-02)")


if __name__ == "__main__":
    main()
