"""Gera os cards de Story (4:5) pra cada post do Lote 5."""

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
    "post-01-mito-auto-condutor-nao-declarado": dict(
        tag="MITO OU VERDADE",
        title="Emprestar o carro<br><span class='hl'>anula</span> o seguro?",
        photo=p("ref-pexels-navigation.jpg"),
    ),
    "post-02-mito-residencial-rc-familiar": dict(
        tag="MITO OU VERDADE",
        title="Seu seguro cobre o<br>dano que <span class='hl'>você</span> causa?",
        photo=p("ref-pexels-house.jpg"),
    ),
    "post-03-vale-a-pena-equipamentos": dict(
        tag="VALE A PENA?",
        title="Seguro de<br><span class='hl'>Equipamentos</span> e Máquinas",
        photo=None,
    ),
    "post-04-caso-real-prescricao": dict(
        tag="ATENÇÃO",
        title="Só <span class='hl'>1 ano</span> pra cobrar<br>da seguradora",
        photo=p("ref-pexels-contract.jpg"),
    ),
    "post-05-papo-corretor-rc-profissional": dict(
        tag="PAPO DE CORRETOR",
        title="O seguro que protege<br>quem <span class='hl'>presta serviço</span>",
        photo=p("ref-pexels-doctor.jpg"),
    ),
}


def main():
    for slug, cfg in STORIES.items():
        out_dir = os.path.join(CONTENT, "semana-05", slug)
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
    src = os.path.join(CONTENT, "semana-05", "post-01-mito-auto-condutor-nao-declarado", "story.jpg")
    dst_dir = os.path.join(CONTENT, "semana-05", "post-06-teste-domingo-condutor")
    os.makedirs(dst_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(dst_dir, "story.jpg"))
    print("post-06-teste-domingo-condutor: story.jpg gerado (copiado do post-01)")


if __name__ == "__main__":
    main()
