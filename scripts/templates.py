"""Templates HTML para os dois estilos de slide: foto+degradê (narrativa) e caderno (dado/número)."""

LOGO_REL = "../../assets-shared/logo.png"


def _brand_footer(logo_path, index, total, dark_text=False):
    color = "rgba(20,24,31,0.75)" if dark_text else "rgba(255,255,255,0.75)"
    return f"""
    <div class="brandline" style="color:{color}">
      <div style="display:flex;align-items:center;gap:16px;">
        <img src="{logo_path}" style="width:64px;height:64px;border-radius:14px;">
        <span style="font-weight:800;font-size:30px;">Instituto do Seguro</span>
      </div>
      <span style="font-weight:700;font-size:26px;">{index}/{total}</span>
    </div>
    """


def photo_slide(logo_path, photo_path, tag, title, subtitle, index, total, accent="#FFC93C"):
    return f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><style>
  html,body {{ margin:0;padding:0;width:1080px;height:1350px;font-family:'Segoe UI',sans-serif; }}
  .frame {{ position:relative;width:1080px;height:1350px;overflow:hidden;background:#000; }}
  .bg {{ position:absolute;inset:0;width:100%;height:100%;object-fit:cover; }}
  .scrim-top {{ position:absolute;top:0;left:0;right:0;height:340px;
    background:linear-gradient(to bottom, rgba(0,0,0,0.55), rgba(0,0,0,0)); }}
  .scrim-bottom {{ position:absolute;bottom:0;left:0;right:0;height:820px;
    background:linear-gradient(to top, rgba(4,8,20,0.97) 25%, rgba(4,8,20,0.78) 55%, rgba(4,8,20,0)); }}
  .tag {{ position:absolute;top:64px;left:64px;background:{accent};color:#14181F;font-weight:800;
    font-size:26px;padding:12px 26px;border-radius:6px;letter-spacing:0.5px; }}
  .bottom-content {{ position:absolute;bottom:66px;left:64px;right:64px; }}
  h1 {{ font-size:74px;font-weight:800;color:#fff;line-height:1.08;margin:0 0 24px 0;
    letter-spacing:-1px; }}
  h1 .hl {{ color:{accent}; }}
  .sub {{ font-size:32px;color:rgba(255,255,255,0.9);font-weight:500;line-height:1.4;margin:0 0 34px 0; }}
  .brandline {{ display:flex;justify-content:space-between;align-items:center; }}
</style></head>
<body><div class="frame">
  <img class="bg" src="{photo_path}">
  <div class="scrim-top"></div>
  <div class="scrim-bottom"></div>
  <div class="tag">{tag}</div>
  <div class="bottom-content">
    <h1>{title}</h1>
    {f'<div class="sub">{subtitle}</div>' if subtitle else ''}
    {_brand_footer(logo_path, index, total)}
  </div>
</div></body></html>"""


def notebook_slide(logo_path, tag, title, items, closing, index, total):
    """items: lista de dicts {label, value, highlight (bool)} para estilo tabela/checklist."""
    rows_html = ""
    for it in items:
        hl = "background:#FFE066;padding:2px 10px;border-radius:4px;" if it.get("highlight") else ""
        rows_html += f"""
        <div style="display:flex;justify-content:space-between;align-items:center;
                    padding:22px 0;border-bottom:2px dashed #D8D2C0;">
          <span style="font-size:36px;color:#2A2620;font-weight:600;">{it['label']}</span>
          <span style="font-size:40px;color:#2A2620;font-weight:800;{hl}">{it['value']}</span>
        </div>"""
    return f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><style>
  html,body {{ margin:0;padding:0;width:1080px;height:1350px;font-family:'Segoe UI',sans-serif; }}
  .frame {{ position:relative;width:1080px;height:1350px;box-sizing:border-box;
    background:#F5F1E6; padding:80px 70px; }}
  .spiral {{ position:absolute;top:0;bottom:0;left:0;width:56px;
    background-image:repeating-linear-gradient(to bottom, transparent 0 18px, #C9C2AC 18px 22px);
  }}
  .spiral-hole {{ position:absolute;left:14px;width:26px;height:26px;border-radius:50%;
    background:#F5F1E6; box-shadow: inset 0 2px 4px rgba(0,0,0,0.25); }}
  .content {{ margin-left:60px; }}
  .tag {{ display:inline-block;background:#14181F;color:#FFE066;font-weight:800;font-size:26px;
    padding:10px 24px;border-radius:6px;letter-spacing:1px;text-transform:uppercase;margin-bottom:36px; }}
  h1 {{ font-size:64px;font-weight:800;color:#14181F;line-height:1.12;margin:0 0 44px 0; }}
  h1 .hl {{ background:#FFE066;padding:2px 14px;border-radius:6px; }}
  .items {{ margin-bottom:40px; }}
  .closing {{ font-size:36px;color:#2A2620;font-weight:600;line-height:1.4; }}
  .brandline {{ position:absolute;bottom:60px;left:130px;right:70px;
    display:flex;justify-content:space-between;align-items:center; }}
</style></head>
<body><div class="frame">
  <div class="spiral"></div>
  {''.join(f'<div class="spiral-hole" style="top:{y}px;"></div>' for y in range(40, 1310, 70))}
  <div class="content">
    <div class="tag">{tag}</div>
    <h1>{title}</h1>
    <div class="items">{rows_html}</div>
    <div class="closing">{closing}</div>
  </div>
  {_brand_footer(logo_path, index, total, dark_text=True)}
</div></body></html>"""


def story_card(logo_path, tag, title, photo_path=None, accent="#FFC93C"):
    """Card de Story em 1080x1350 (4:5) — a API do Instagram exige proporcao entre
    4:5 e 1.91:1 pra qualquer imagem (inclusive STORIES), 9:16 tela cheia é rejeitado (erro 400).
    O Instagram estica/corta esse 4:5 pra preencher a tela 9:16 (cover, não letterbox) —
    corta ~15% de cada lado. Por isso todo conteúdo fica centralizado numa faixa de ~720px
    (bem mais estreita que os 1080px totais), nunca grudado na margem esquerda/direita."""
    bg_layer = (
        f'<img class="bg" src="{photo_path}">'
        f'<div class="scrim-top-s"></div><div class="scrim-bottom-s"></div>'
        if photo_path else '<div class="bg-solid"></div>'
    )
    return f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><style>
  html,body {{ margin:0;padding:0;width:1080px;height:1350px;font-family:'Segoe UI',sans-serif; }}
  .frame {{ position:relative;width:1080px;height:1350px;overflow:hidden;background:#0C1E30; }}
  .bg {{ position:absolute;inset:0;width:100%;height:100%;object-fit:cover; }}
  .bg-solid {{ position:absolute;inset:0;
    background:linear-gradient(160deg,#0B1030 0%,#101A4A 45%,#16256B 100%); }}
  .scrim-top-s {{ position:absolute;top:0;left:0;right:0;height:340px;
    background:linear-gradient(to bottom, rgba(0,0,0,0.6), rgba(0,0,0,0)); }}
  .scrim-bottom-s {{ position:absolute;bottom:0;left:0;right:0;height:900px;
    background:linear-gradient(to top, rgba(4,8,20,0.97) 35%, rgba(4,8,20,0.8) 60%, rgba(4,8,20,0)); }}
  .safe {{ position:absolute; inset:0; display:flex; flex-direction:column; align-items:center; }}
  .tag {{ margin-top:90px;background:{accent};color:#14181F;font-weight:800;
    font-size:26px;padding:12px 26px;border-radius:8px;letter-spacing:0.5px;text-align:center; }}
  .bottom {{ position:absolute;bottom:120px;left:180px;right:180px;
    display:flex;flex-direction:column;align-items:center;text-align:center; }}
  h1 {{ font-size:56px;font-weight:800;color:#fff;line-height:1.15;margin:0 0 30px 0;
    letter-spacing:-1px; }}
  h1 .hl {{ color:{accent}; }}
  .cta {{ display:inline-flex;align-items:center;gap:12px;background:rgba(255,255,255,0.14);
    border:1px solid rgba(255,255,255,0.3);border-radius:100px;padding:16px 28px;
    font-weight:800;font-size:26px;color:#fff;white-space:nowrap; }}
  .brand {{ position:absolute;bottom:44px;left:0;right:0;display:flex;align-items:center;
    justify-content:center;gap:14px; }}
  .brand span {{ color:rgba(255,255,255,0.75);font-weight:800;font-size:24px; }}
</style></head>
<body><div class="frame">
  {bg_layer}
  <div class="safe"><div class="tag">{tag}</div></div>
  <div class="bottom">
    <h1>{title}</h1>
    <div class="cta">⬆️ Post completo no feed</div>
  </div>
  <div class="brand"><img src="{logo_path}" style="width:56px;height:56px;border-radius:12px;"><span>Instituto do Seguro</span></div>
</div></body></html>"""
