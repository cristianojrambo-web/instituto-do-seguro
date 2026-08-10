"""Substitui os posts 1, 3 e 4 do Lote 3 (que eram sobre seguro saude, ramo que o
usuario nao trabalha) por conteudo dentro do escopo real: auto, vida, e um caso
pratico que vale pra qualquer ramo (aviso de sinistro)."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from templates import photo_slide, notebook_slide  # noqa: E402
from render_html import render  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
ASSETS = os.path.join(ROOT, "content", "assets")
LOGO = os.path.join(CONTENT, "logo.png").replace("\\", "/")


def p(name):
    return os.path.join(ASSETS, name).replace("\\", "/")


def make_html_and_render(out_dir, name, html):
    os.makedirs(out_dir, exist_ok=True)
    html_path = os.path.join(out_dir, f"{name}.html")
    png_path = os.path.join(out_dir, f"{name}.png")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    render(html_path, png_path)
    return png_path


def build_post_01_mito_app():
    out = os.path.join(CONTENT, "semana-03", "post-01-mito-seguro-auto-app")
    photo = p("ref-pexels-navigation.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE", "Seu seguro auto cobre<br>rodar por <span class='hl'>aplicativo</span>?",
                    "A resposta pode custar o carro inteiro se você não souber disso.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span> — na maioria das apólices",
                    "Seguro auto comum tem cláusula de exclusão de uso comercial — corrida paga não entra.", 2, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O QUE A PLATAFORMA COBRE", "Só durante a<br><span class='hl'>corrida ativa</span>",
                    "Uber e 99 cobrem acidente só com o app ligado numa corrida — fora disso, nada.", 3, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O RISCO REAL", "Sinistro fora da corrida<br>pode ser <span class='hl'>negado</span>",
                    "Sem cobertura adequada, um roubo ou colisão fora do horário de corrida fica sem indenização nenhuma.", 4, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O QUE FAZER", "Existe cobertura<br><span class='hl'>APP específica</span>",
                    "A SUSEP exige produto próprio pra transporte remunerado de passageiros — vale contratar antes de ligar o app.", 5, total),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Avisa a seguradora<br>antes de <span class='hl'>rodar por app</span>",
                    "Omitir isso pode fazer a seguradora cancelar a apólice inteira, não só negar um sinistro.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_03_vale_a_pena_vida():
    out = os.path.join(CONTENT, "semana-03", "post-03-vale-a-pena-vida")
    total = 6
    slides = [
        notebook_slide(LOGO, "VALE A PENA?",
                        "Seguro de Vida:<br>muito mais do<br>que só <span class='hl'>morte</span>",
                        [], "4 formas de proteção que a maioria não sabe que já existem no contrato 👇", 1, total),
        notebook_slide(LOGO, "PROTEÇÃO EM VIDA", "Invalidez por acidente<br>ou doença grave",
                        [{"label": "Precisa morrer?", "value": "NÃO", "highlight": True}],
                        "Diagnóstico de câncer, AVC, infarto ou perda de autonomia já libera capital — sem esperar o pior acontecer.", 2, total),
        notebook_slide(LOGO, "PROTEÇÃO DE RENDA", "Diária por<br>incapacidade temporária",
                        [{"label": "Função", "value": "mantém sua renda"}],
                        "Ficou afastado por acidente ou doença? Essa cobertura substitui parte do salário durante a recuperação.", 3, total),
        notebook_slide(LOGO, "SUCESSÃO FACILITADA", "Não entra no<br><span class='hl'>inventário</span>",
                        [{"label": "Base legal", "value": "art. 794 CC", "highlight": True}],
                        "O capital vai direto pros beneficiários indicados — sem esperar anos de processo de inventário.", 4, total),
        notebook_slide(LOGO, "NÃO É SÓ PRA QUEM TEM FILHO", "Vale pra quem tem<br>alguém <span class='hl'>dependendo</span>",
                        [],
                        "Cônjuge, pais idosos, sócio no negócio — qualquer pessoa que sentiria sua falta financeiramente.", 5, total),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Sim — e a proteção<br>começa muito antes da morte",
                        [], "Guarda esse carrossel: a maioria só pensa no básico e não sabe do resto que já está incluso.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_04_caso_real_aviso_sinistro():
    out = os.path.join(CONTENT, "semana-03", "post-04-caso-real-aviso-sinistro")
    photo = p("ref-pexels-crash.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "CASO ILUSTRATIVO", "Avisar o sinistro<br>alguns dias <span class='hl'>depois</span> pode custar tudo?",
                    "Caso ilustrativo, baseado em situação real e comum, com respaldo do Código Civil.", 1, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O QUE ACONTECEU", "Segurado só avisou<br>a seguradora <span class='hl'>dias depois</span>",
                    "O sinistro aconteceu, mas a comunicação formal demorou.", 2, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O QUE A SEGURADORA ALEGOU", "Art. 771 do<br><span class='hl'>Código Civil</span>",
                    "A lei exige aviso do sinistro assim que o segurado toma conhecimento, sob pena de perder o direito.", 3, total),
        photo_slide(LOGO, photo, "A NUANCE IMPORTANTE", "Perda do direito<br><span class='hl'>não é automática</span>",
                    "A jurisprudência majoritária só aceita a perda se o atraso causar prejuízo real e comprovado à seguradora.", 4, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "A LIÇÃO", "Mesmo assim,<br>avise <span class='hl'>o quanto antes</span>",
                    "Contar com a exceção é arriscado — o ônus de provar que não houve prejuízo pode virar uma discussão longa.", 5, total),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Sinistro aconteceu?<br><span class='hl'>Avisa na hora</span>",
                    "Não espera resolver tudo sozinho antes de comunicar — isso é o que mais gera negativa depois.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


if __name__ == "__main__":
    build_post_01_mito_app()
    build_post_03_vale_a_pena_vida()
    build_post_04_caso_real_aviso_sinistro()
    print("Substituicoes do Lote 3 geradas.")
