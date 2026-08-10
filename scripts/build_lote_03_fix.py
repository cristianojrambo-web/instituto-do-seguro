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
    photo = p("ref-pexels-rideapp.jpg")
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
                        "Seguro de Vida:<br>os mitos que travam<br>a <span class='hl'>decisão</span>",
                        [], "4 mitos que ainda confundem quem está decidindo contratar 👇", 1, total),
        notebook_slide(LOGO, "MITO 1", "\"Só serve se eu morrer\"",
                        [{"label": "É mito?", "value": "SIM", "highlight": True}],
                        "A maioria das apólices já inclui cobertura por invalidez por acidente, não só morte.", 2, total),
        notebook_slide(LOGO, "MITO 2", "\"Preciso de exame médico caro\"",
                        [{"label": "É mito?", "value": "SIM", "highlight": True}],
                        "Pra maioria dos casos, um questionário de saúde (DPS) já basta — exame só em idade avançada ou valores altos.", 3, total),
        notebook_slide(LOGO, "MITO 3", "\"É só pra quem tem filho\"",
                        [{"label": "É mito?", "value": "SIM", "highlight": True}],
                        "Vale pra qualquer pessoa que tem alguém dependendo financeiramente dela — cônjuge, pais, sócio.", 4, total),
        notebook_slide(LOGO, "MITO 4", "\"É caro\"",
                        [{"label": "É mito?", "value": "SIM", "highlight": True}],
                        "Existem planos acessíveis pra vários perfis — e o custo de não ter, pra quem depende de você, pode ser bem maior.", 5, total),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Sim — se alguém<br>depende de você",
                        [], "Guarda esse carrossel pra revisar com quem ainda acha que não precisa.", 6, total),
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
