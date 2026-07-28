"""
Gera slides de carrossel com a identidade visual do Instituto do Seguro — v3.
Fundo em gradiente, ícones vetoriais por tema, sombra suave, tipografia com mais contraste.
"""

import os
import re

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
NAVY_DARK = (12, 30, 48)
NAVY = (18, 42, 66)
NAVY_LIGHT = (32, 62, 94)
GOLD = (198, 155, 74)
GOLD_LIGHT = (222, 184, 110)
WHITE = (255, 255, 255)
LIGHT_GRAY = (196, 208, 220)

FONT_BLACK = r"C:\Windows\Fonts\arialbd.ttf"
FONT_REGULAR = r"C:\Windows\Fonts\arial.ttf"

MARGIN = 80
CONTENT_DIR = os.path.join(os.path.dirname(__file__), "..", "content")
LOGO_PATH = os.path.join(CONTENT_DIR, "logo.png")

_NUMBERED = re.compile(r"^(\d+)\.\s*(.*)$")

ICON_MAP = {
    "car": "car",
    "rain": "rain",
    "warning": "warning",
    "chart": "chart",
    "shield": "shield",
}


def _diagonal_gradient(c1, c2):
    """Gradiente diagonal suave de c1 (canto sup. esq.) a c2 (canto inf. dir.)."""
    x = np.linspace(0, 1, W)
    y = np.linspace(0, 1, H)
    xx, yy = np.meshgrid(x, y)
    t = (xx + yy) / 2
    arr = np.zeros((H, W, 3), dtype=np.uint8)
    for i in range(3):
        arr[:, :, i] = (c1[i] + (c2[i] - c1[i]) * t).astype(np.uint8)
    return Image.fromarray(arr, "RGB")


def _soft_shadow(img, box, blur=28, opacity=90, offset=(0, 14)):
    """Desenha uma sombra suave elíptica atrás de um elemento (box = x0,y0,x1,y1)."""
    shadow_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)
    x0, y0, x1, y1 = box
    sd.rounded_rectangle(
        [x0 + offset[0], y0 + offset[1], x1 + offset[0], y1 + offset[1]],
        radius=18, fill=(0, 0, 0, opacity),
    )
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(blur))
    img.paste(Image.alpha_composite(img.convert("RGBA"), shadow_layer).convert("RGB"), (0, 0))


def _wrap(draw, text, font, max_width):
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split(" ")
        current = ""
        for word in words:
            trial = f"{current} {word}".strip()
            if draw.textbbox((0, 0), trial, font=font)[2] <= max_width:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = word
        lines.append(current)
    return lines


def _draw_lines(draw, lines, font, fill, x, top_y, line_height):
    y = top_y
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += line_height
    return y


# ---------- ícones vetoriais simples (desenhados em uma caixa quadrada) ----------

def _icon_car(draw, cx, cy, s, color, width=8):
    x0, y0 = cx - s / 2, cy - s / 2
    body = [x0 + s * 0.05, y0 + s * 0.55, x0 + s * 0.95, y0 + s * 0.55,
            x0 + s * 0.80, y0 + s * 0.30, x0 + s * 0.20, y0 + s * 0.30]
    draw.line(body + [body[0], body[1]], fill=color, width=width, joint="curve")
    draw.line([x0 + s * 0.05, y0 + s * 0.55, x0 + s * 0.02, y0 + s * 0.72,
                x0 + s * 0.98, y0 + s * 0.72, x0 + s * 0.95, y0 + s * 0.55],
               fill=color, width=width, joint="curve")
    r = s * 0.11
    for wx in (x0 + s * 0.24, x0 + s * 0.76):
        draw.ellipse([wx - r, y0 + s * 0.72 - r, wx + r, y0 + s * 0.72 + r], outline=color, width=width)


def _icon_rain(draw, cx, cy, s, color, width=8):
    x0, y0 = cx - s / 2, cy - s / 2
    draw.ellipse([x0 + s * 0.05, y0 + s * 0.20, x0 + s * 0.65, y0 + s * 0.55], outline=color, width=width)
    draw.ellipse([x0 + s * 0.35, y0 + s * 0.10, x0 + s * 0.95, y0 + s * 0.50], outline=color, width=width)
    for lx in (x0 + s * 0.25, x0 + s * 0.5, x0 + s * 0.75):
        draw.line([lx, y0 + s * 0.68, lx - s * 0.08, y0 + s * 0.92], fill=color, width=width)


def _icon_warning(draw, cx, cy, s, color, width=9):
    x0, y0 = cx - s / 2, cy - s / 2
    tri = [x0 + s * 0.5, y0 + s * 0.05, x0 + s * 0.97, y0 + s * 0.92, x0 + s * 0.03, y0 + s * 0.92]
    draw.line(tri + [tri[0], tri[1]], fill=color, width=width, joint="curve")
    draw.line([x0 + s * 0.5, y0 + s * 0.38, x0 + s * 0.5, y0 + s * 0.65], fill=color, width=width)
    draw.ellipse([x0 + s * 0.46, y0 + s * 0.74, x0 + s * 0.54, y0 + s * 0.82], fill=color)


def _icon_chart(draw, cx, cy, s, color, width=8):
    x0, y0 = cx - s / 2, cy - s / 2
    draw.line([x0 + s * 0.05, y0 + s * 0.95, x0 + s * 0.95, y0 + s * 0.95], fill=color, width=width)
    bars = [0.15, 0.42, 0.69]
    heights = [0.45, 0.75, 0.6]
    for bx, bh in zip(bars, heights):
        draw.rectangle([x0 + s * bx, y0 + s * (0.95 - bh), x0 + s * (bx + 0.18), y0 + s * 0.95],
                        outline=color, width=width)


def _icon_shield(draw, cx, cy, s, color, width=8):
    x0, y0 = cx - s / 2, cy - s / 2
    pts = [(x0 + s * 0.1, y0), (x0 + s * 0.9, y0), (x0 + s * 0.9, y0 + s * 0.55),
           (x0 + s * 0.5, y0 + s), (x0 + s * 0.1, y0 + s * 0.55)]
    draw.line(pts + [pts[0]], fill=color, width=width, joint="curve")
    draw.line([x0 + s * 0.3, y0 + s * 0.45, x0 + s * 0.45, y0 + s * 0.62, x0 + s * 0.72, y0 + s * 0.28],
               fill=color, width=width, joint="curve")


_ICON_FNS = {"car": _icon_car, "rain": _icon_rain, "warning": _icon_warning, "chart": _icon_chart, "shield": _icon_shield}


def _draw_icon(img, draw, name, cx, cy, s, color):
    fn = _ICON_FNS.get(name)
    if fn:
        fn(draw, cx, cy, s, color)


def _base_canvas(dark=False):
    base = _diagonal_gradient(NAVY_DARK if dark else NAVY, NAVY_LIGHT)
    img = base.convert("RGB")
    draw = ImageDraw.Draw(img)
    r = 460
    cx, cy = W - 40, H - 20
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255, 14))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 14], fill=GOLD)
    return img, draw


def _add_footer(draw, img, index, total):
    if os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH).convert("RGBA").resize((72, 72))
        img.paste(logo, (MARGIN, H - 72 - 56), logo)
    font = ImageFont.truetype(FONT_REGULAR, 30)
    text = f"{index} / {total}"
    w = draw.textbbox((0, 0), text, font=font)[2]
    draw.text((W - MARGIN - w, H - 56 - 24), text, font=font, fill=LIGHT_GRAY)


def _draw_kicker(draw, text, x, y):
    font = ImageFont.truetype(FONT_BLACK, 32)
    pad_x, pad_y = 26, 14
    w = draw.textbbox((0, 0), text, font=font)[2]
    h = font.size
    draw.rounded_rectangle([x, y, x + w + pad_x * 2, y + h + pad_y * 2], radius=8, fill=GOLD)
    draw.text((x + pad_x, y + pad_y - 4), text, font=font, fill=NAVY_DARK)
    return y + h + pad_y * 2


def _draw_cta_button(img, draw, text, center_x, bottom_y):
    font = ImageFont.truetype(FONT_BLACK, 38)
    pad_x, pad_y = 44, 26
    w = draw.textbbox((0, 0), text, font=font)[2]
    h = font.size
    x0 = center_x - (w + pad_x * 2) / 2
    y0 = bottom_y - (h + pad_y * 2)
    x1, y1 = x0 + w + pad_x * 2, y0 + h + pad_y * 2
    _soft_shadow(img, (x0, y0, x1, y1), blur=20, opacity=70, offset=(0, 10))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=GOLD)
    draw.text((x0 + pad_x, y0 + pad_y - 4), text, font=font, fill=NAVY_DARK)


def _draw_number_badge(img, cx, cy, r, number):
    shadow_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)
    sd.ellipse([cx - r, cy - r + 12, cx + r, cy + r + 12], fill=(0, 0, 0, 90))
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(22))
    img.paste(Image.alpha_composite(img.convert("RGBA"), shadow_layer).convert("RGB"), (0, 0))
    draw = ImageDraw.Draw(img)
    grad = _diagonal_gradient(GOLD_LIGHT, GOLD).resize((r * 2, r * 2))
    mask = Image.new("L", (r * 2, r * 2), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, r * 2, r * 2], fill=255)
    img.paste(grad, (int(cx - r), int(cy - r)), mask)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_BLACK, int(r * 1.15))
    bbox = draw.textbbox((0, 0), number, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((cx - tw / 2 - bbox[0], cy - th / 2 - bbox[1]), number, font=font, fill=NAVY_DARK)


def render_cover(index, total, kicker, title, icon=None):
    img, draw = _base_canvas()
    if icon:
        _draw_icon(img, draw, icon, W - 210, 210, 190, GOLD)
    y = 150
    if kicker:
        y = _draw_kicker(draw, kicker, MARGIN, y) + 60
    title_font = ImageFont.truetype(FONT_BLACK, 92 if len(title) < 24 else 72)
    lines = _wrap(draw, title, title_font, W - MARGIN * 2 - 160)
    line_h = title_font.size + 16
    total_h = line_h * len(lines)
    top = max(y, H / 2 - total_h / 2)
    _draw_lines(draw, lines, title_font, WHITE, MARGIN, top, line_h)
    draw.rectangle([MARGIN, top + total_h + 30, MARGIN + 110, top + total_h + 40], fill=GOLD)
    _add_footer(draw, img, index, total)
    return img


def render_statement(index, total, title, body, cta=None, icon=None):
    img, draw = _base_canvas(dark=True)
    if icon:
        _draw_icon(img, draw, icon, W - 190, 190, 170, NAVY_LIGHT)
        draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype(FONT_BLACK, 110)
    lines = _wrap(draw, title, title_font, W - MARGIN * 2)
    line_h = title_font.size + 10
    body_font = ImageFont.truetype(FONT_REGULAR, 42)
    body_lines = _wrap(draw, body, body_font, W - MARGIN * 2 - 40) if body else []
    body_line_h = body_font.size + 18

    block_h = line_h * len(lines) + (30 + body_line_h * len(body_lines) if body_lines else 0)
    top = H / 2 - block_h / 2 - 40

    y = _draw_lines(draw, lines, title_font, GOLD, MARGIN, top, line_h)
    if body_lines:
        y += 30
        _draw_lines(draw, body_lines, body_font, WHITE, MARGIN, y, body_line_h)

    if cta:
        _draw_cta_button(img, draw, cta, W / 2, H - 100)
    draw = ImageDraw.Draw(img)
    _add_footer(draw, img, index, total)
    return img


def render_numbered(index, total, number, title, body, cta=None):
    img, draw = _base_canvas()
    _draw_number_badge(img, MARGIN + 70, 230, 70, number.zfill(2))
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype(FONT_BLACK, 56)
    title_lines = _wrap(draw, title, title_font, W - MARGIN * 2)
    title_top = 230 + 90 + 40
    y = _draw_lines(draw, title_lines, title_font, WHITE, MARGIN, title_top, title_font.size + 10)

    if body:
        body_font = ImageFont.truetype(FONT_REGULAR, 40)
        body_lines = _wrap(draw, body, body_font, W - MARGIN * 2)
        y += 30
        _draw_lines(draw, body_lines, body_font, LIGHT_GRAY, MARGIN, y, body_font.size + 18)

    if cta:
        _draw_cta_button(img, draw, cta, W / 2, H - 100)
    draw = ImageDraw.Draw(img)
    _add_footer(draw, img, index, total)
    return img


def render_standard(index, total, title, body, cta=None, icon=None):
    img, draw = _base_canvas()
    if icon:
        _draw_icon(img, draw, icon, W - 150, 150, 130, GOLD)
        draw = ImageDraw.Draw(img)
    draw.rectangle([MARGIN, 140, MARGIN + 90, 152], fill=GOLD)

    title_font = ImageFont.truetype(FONT_BLACK, 60 if len(title) < 30 else 50)
    title_lines = _wrap(draw, title, title_font, W - MARGIN * 2)
    y = _draw_lines(draw, title_lines, title_font, WHITE, MARGIN, 185, title_font.size + 12)

    if body:
        body_font = ImageFont.truetype(FONT_REGULAR, 42)
        body_lines = _wrap(draw, body, body_font, W - MARGIN * 2)
        y += 30
        _draw_lines(draw, body_lines, body_font, LIGHT_GRAY, MARGIN, y, body_font.size + 20)

    if cta:
        _draw_cta_button(img, draw, cta, W / 2, H - 100)
    draw = ImageDraw.Draw(img)
    _add_footer(draw, img, index, total)
    return img


def render_slide(index, total, slide):
    kicker = slide.get("kicker", "")
    title = slide.get("title", "")
    body = slide.get("body", "")
    cta = slide.get("cta")
    icon = slide.get("icon")

    if index == 1 and kicker:
        return render_cover(index, total, kicker, title, icon=icon)

    match = _NUMBERED.match(title)
    if match:
        return render_numbered(index, total, match.group(1), match.group(2), body, cta)

    if not body and len(title) <= 14:
        return render_statement(index, total, title, "", cta, icon=icon)

    if len(title) <= 20 and body and index == 2:
        return render_statement(index, total, title, body, cta, icon=icon)

    return render_standard(index, total, title, body, cta, icon=icon)


def build_carousel(post_slug, slides):
    out_dir = os.path.join(CONTENT_DIR, post_slug)
    os.makedirs(out_dir, exist_ok=True)
    total = len(slides)
    paths = []
    for i, slide in enumerate(slides, start=1):
        img = render_slide(i, total, slide)
        path = os.path.join(out_dir, f"slide-{i:02d}.png")
        img.save(path)
        paths.append(path)
    return paths
