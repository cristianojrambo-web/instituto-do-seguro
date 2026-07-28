"""Gera o Lote 1 (v2.1) — fatos corrigidos, slides expandidos pra 6-7 por post."""

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


def build_post_00():
    out = os.path.join(CONTENT, "semana-01-v2", "post-00-apresentacao")
    photo = p("ref-pexels-house.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "INSTITUTO DO SEGURO",
                    "Seguro de todos os ramos,<br>explicado sem <span class='hl'>segurês</span>",
                    "Pra quem compra E pra quem vende.", 1, total),
        photo_slide(LOGO, photo, "PRA QUEM COMPRA",
                    "Mito ou verdade.<br><span class='hl'>Casos reais.</span><br>Sem economês.",
                    "Respostas diretas sobre o seu seguro, sem letra miúda escondida.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "PRA QUEM VENDE",
                    "Papo de corretor.<br><span class='hl'>Dados de mercado.</span><br>Bastidores.",
                    "O conteúdo que a maioria das contas de seguro não faz de um jeito fácil de consumir.", 3, total, accent="#8FB8FF"),
        photo_slide(LOGO, photo, "TODA TERÇA", "<span class='hl'>Mito ou Verdade</span>",
                    "A crença sobre seguro que todo mundo repete — e nem sempre é verdade.", 4, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "TODA QUINTA", "<span class='hl'>Caso Real</span>",
                    "Situações reais e comuns do mercado, sem citar nomes.", 5, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "VAMOS?", "Manda sua primeira<br><span class='hl'>dúvida</span> aqui embaixo",
                    "Me conta o que te deixa em dúvida sobre seu seguro hoje.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_01():
    out = os.path.join(CONTENT, "semana-01-v2", "post-01-vale-a-pena-auto")
    total = 6
    slides = [
        notebook_slide(LOGO, "VALE A PENA?",
                        "Seguro Auto: o que<br>ninguém <span class='hl'>lê</span> no contrato",
                        [], "4 cláusulas que quase ninguém revisa antes de assinar 👇", 1, total),
        notebook_slide(LOGO, "ITEM 1", "Carro reserva",
                        [{"label": "Incluso por padrão?", "value": "NÃO", "highlight": True}],
                        "Sem essa cláusula, você fica sem carro durante o reparo — às vezes semanas.", 2, total),
        notebook_slide(LOGO, "ITEM 2", "Vidros e faróis",
                        [{"label": "Cobertura à parte?", "value": "SIM", "highlight": True}],
                        "Muita gente acha que é automático. Na maioria das apólices, não é.", 3, total),
        notebook_slide(LOGO, "ITEM 3", "Danos a terceiros",
                        [{"label": "Precisa de", "value": "RCF", "highlight": True}],
                        "O seguro cobre o SEU carro. Bater no carro de outra pessoa exige cobertura separada.", 4, total),
        notebook_slide(LOGO, "ITEM 4", "Franquia",
                        [{"label": "Você paga em todo sinistro?", "value": "ÀS VEZES", "highlight": True}],
                        "É a parte do prejuízo que fica por sua conta. Varia por apólice — vale conferir o valor antes de fechar.", 5, total),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Sim — se você souber<br>o que está no contrato",
                        [], "Guarda esse carrossel pra revisar sua apólice antes de renovar.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_02():
    out = os.path.join(CONTENT, "semana-01-v2", "post-02-mito-enchente")
    photo = p("ref-pexels-rain.jpg")
    total = 7
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE", "Seu seguro cobre <span class='hl'>enchente?</span>",
                    "A resposta tem uma pegadinha que pode custar caro.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Verdade</span> — com cobertura compreensiva",
                    "\"Seguro total\" já inclui isso por padrão, não é opcional à parte.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O QUE JÁ VEM INCLUSO", "Colisão, incêndio,<br><span class='hl'>roubo e furto</span>",
                    "Isso é a base de qualquer cobertura compreensiva.", 3, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "+ FENÔMENOS DA NATUREZA", "Enchente, alagamento<br>e <span class='hl'>queda de granizo</span>",
                    "Por água doce — já contam como padrão na cobertura compreensiva.", 4, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "A PEGADINHA 1", "Água do <span class='hl'>mar</span> não conta",
                    "Nenhuma apólice cobre dano por água salgada ou maré.", 5, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "A PEGADINHA 2", "Via alagada é <span class='hl'>imprudência</span>",
                    "Forçar passagem por alagamento visível é agravamento de risco — perde o direito à indenização.", 6, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "NA PRÓXIMA CHUVA", "<span class='hl'>Desligue</span> o carro se a água subir",
                    "Sem cobertura compreensiva, seu carro não tem essa proteção — RCF isolado cobre só terceiros.", 7, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_03():
    out = os.path.join(CONTENT, "semana-01-v2", "post-03-caso-real")
    photo = p("ref-pexels-crash.jpg")
    total = 7
    slides = [
        photo_slide(LOGO, photo, "CASO ILUSTRATIVO", "O detalhe que pode <span class='hl'>zerar</span> sua indenização",
                    "Baseado em situação real, comum e com jurisprudência do STJ.", 1, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O QUE ACONTECEU", "Segurado bateu o carro<br>e pediu a <span class='hl'>indenização</span>",
                    "Perda total, sinistro comunicado dentro do prazo.", 2, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O QUE A SEGURADORA ALEGOU", "<span class='hl'>Embriaguez</span> ao volante",
                    "Teste ou exame apontou álcool no sangue do condutor no momento do acidente.", 3, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O QUE DIZ A JUSTIÇA", "STJ: precisa <span class='hl'>provar</span> os dois lados",
                    "A seguradora só se exime se provar a embriaguez E que ela causou o agravamento do risco.", 4, total),
        photo_slide(LOGO, photo, "A NUANCE IMPORTANTE", "O ônus da prova é da<br><span class='hl'>seguradora</span>, não sua",
                    "Alegar não basta — precisa demonstrar que a bebida foi determinante para o acidente.", 5, total),
        photo_slide(LOGO, photo, "A LIÇÃO", "Dirigir bêbado não é só<br><span class='hl'>multa de trânsito</span>",
                    "É motivo real e documentado de perda de cobertura no seguro auto.", 6, total),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Beber e dirigir coloca<br><span class='hl'>tudo</span> em risco",
                    "A vida de alguém, e o direito à indenização do seu próprio carro.", 7, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_04():
    out = os.path.join(CONTENT, "semana-01-v2", "post-04-papo-corretor")
    total = 6
    slides = [
        notebook_slide(LOGO, "PAPO DE CORRETOR", "2 dados que valem mais<br>que curso de vendas",
                        [], "Com fonte. Não é achismo.", 1, total),
        notebook_slide(LOGO, "DADO 1", "A hora de ouro",
                        [{"label": "Renovariam com ajuste", "value": "42%", "highlight": True}],
                        "(McKinsey, 2024) De quem não renova o seguro, quase metade voltaria se a cobertura fosse revisada.", 2, total),
        notebook_slide(LOGO, "O QUE FAZER COM ISSO", "Renovação é consultoria,<br>não cobrança",
                        [], "Use os 60 dias antes do vencimento pra revisar a cobertura com o cliente — não só mandar o boleto.", 3, total),
        notebook_slide(LOGO, "DADO 2", "Indicação > anúncio",
                        [{"label": "Confiam mais em indicação", "value": "84%", "highlight": True}],
                        "(Nielsen) A maioria confia mais em indicação de amigos e família do que em qualquer propaganda.", 4, total),
        notebook_slide(LOGO, "O QUE FAZER COM ISSO", "Peça indicação<br>ativamente",
                        [], "Não espere acontecer sozinho — pergunte direto pro cliente satisfeito, no momento certo.", 5, total),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Vale mais que a maioria<br>dos treinamentos por aí",
                        [], "Manda pra um colega corretor que precisa ver isso.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


if __name__ == "__main__":
    build_post_00()
    build_post_01()
    build_post_02()
    build_post_03()
    build_post_04()
    print("Lote 1 v2.1 gerado.")
