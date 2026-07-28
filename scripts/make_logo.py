"""
Gera a logo/avatar do Instituto do Seguro em scripts/../content/logo.png (1080x1080).
Marca: escudo (protecao/seguro) + monograma "IS" (Instituto do Seguro).
"""

import os
from PIL import Image, ImageDraw, ImageFont

SIZE = 1080
NAVY = (18, 42, 66)
GOLD = (198, 155, 74)
WHITE = (255, 255, 255)

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "content", "logo.png")
FONT_PATH = r"C:\Windows\Fonts\arialbd.ttf"


def build_shield_points(cx, cy, w, h):
    return [
        (cx - w / 2, cy - h / 2),
        (cx + w / 2, cy - h / 2),
        (cx + w / 2, cy + h * 0.08),
        (cx, cy + h / 2),
        (cx - w / 2, cy + h * 0.08),
    ]


def main():
    img = Image.new("RGB", (SIZE, SIZE), NAVY)
    draw = ImageDraw.Draw(img)

    cx, cy = SIZE / 2, SIZE / 2 + 20
    shield_w, shield_h = SIZE * 0.56, SIZE * 0.62

    shield_points = build_shield_points(cx, cy, shield_w, shield_h)
    draw.polygon(shield_points, fill=WHITE)

    inner_points = build_shield_points(cx, cy, shield_w * 0.86, shield_h * 0.86)
    draw.polygon(inner_points, fill=NAVY)

    font = ImageFont.truetype(FONT_PATH, int(SIZE * 0.24))
    text = "IS"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(
        (cx - text_w / 2 - bbox[0], cy - text_h / 2 - bbox[1] - SIZE * 0.02),
        text,
        font=font,
        fill=GOLD,
    )

    bar_y = cy + shield_h * 0.28
    draw.rectangle(
        [cx - shield_w * 0.18, bar_y, cx + shield_w * 0.18, bar_y + SIZE * 0.012],
        fill=GOLD,
    )

    img.save(OUT_PATH)
    print(f"Logo salva em {OUT_PATH}")


if __name__ == "__main__":
    main()
