"""Gera o Lote 2 — ramo da semana: Seguro Residencial (+ 1 mito de seguro de vida)."""

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


def build_post_01_mito_roubo():
    out = os.path.join(CONTENT, "semana-02", "post-01-mito-roubo")
    photo = p("ref-pexels-doorlock.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "A cobertura de roubo do seu residencial<br>só paga com <span class='hl'>arrombamento</span>?",
                    "A resposta tem um detalhe que quase ninguém sabe.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Verdade</span>, como regra geral",
                    "A maioria das apólices exige furto qualificado — com sinais de arrombamento — pra evitar fraude.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O QUE CONTA COMO PROVA", "Boletim de ocorrência<br>+ <span class='hl'>sinais de arrombamento</span>",
                    "Sem isso, a seguradora pode alegar furto simples e negar a indenização.", 3, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O DETALHE QUE MUDA TUDO", "Não precisa listar<br><span class='hl'>bem por bem</span>",
                    "A cobertura de conteúdo funciona por um valor total segurado — não uma lista item a item.", 4, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "MAS ATENÇÃO", "Bens de <span class='hl'>alto valor</span> são exceção",
                    "Joias, obras de arte e equipamentos caros costumam exigir declaração específica na apólice.", 5, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Antes de acionar,<br>confira sua <span class='hl'>apólice</span>",
                    "Saber o que precisa comprovar evita surpresa na hora do sinistro.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_02_vale_a_pena_residencial():
    out = os.path.join(CONTENT, "semana-02", "post-02-vale-a-pena-residencial")
    total = 6
    slides = [
        notebook_slide(LOGO, "VALE A PENA?",
                        "Seguro Residencial:<br>os mitos que te fazem<br>pagar mais <span class='hl'>caro</span>",
                        [], "4 mitos que ainda travam muita gente na hora de decidir 👇", 1, total),
        notebook_slide(LOGO, "MITO 1", "\"Só pra quem tem casa própria\"",
                        [{"label": "É mito?", "value": "SIM", "highlight": True}],
                        "Quem mora de aluguel também pode contratar — a responsabilidade pelos bens é do morador, não do dono do imóvel.", 2, total),
        notebook_slide(LOGO, "MITO 2", "\"Só cobre incêndio\"",
                        [{"label": "É mito?", "value": "SIM", "highlight": True}],
                        "Cobre também dano elétrico, cano estourado, vidro quebrado, roubo/furto, responsabilidade civil e assistência 24h.", 3, total),
        notebook_slide(LOGO, "MITO 3", "\"Mora em condomínio não precisa\"",
                        [{"label": "É mito?", "value": "SIM", "highlight": True}],
                        "O seguro do condomínio cobre só a estrutura e áreas comuns — o interior do seu apê e seus bens ficam de fora.", 4, total),
        notebook_slide(LOGO, "MITO 4", "\"É caro\"",
                        [{"label": "É mito?", "value": "SIM", "highlight": True}],
                        "Existem planos parcelados e acessíveis pra vários perfis de casa — e o custo de um sinistro sem seguro costuma ser bem maior que qualquer parcela.", 5, total),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Sim — pra quase<br>qualquer perfil de casa",
                        [], "Guarda esse carrossel pra desmontar esses mitos com quem ainda acha que não precisa.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_03_mito_vida_suicidio():
    out = os.path.join(CONTENT, "semana-02", "post-03-mito-vida-suicidio")
    photo = p("ref-pexels-contract.jpg")
    total = 5
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE", "Seguro de vida cobre<br><span class='hl'>suicídio</span>?",
                    "Um tema sério — tratado aqui com respeito, sem dramatização.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "Depende do <span class='hl'>tempo</span> de contrato",
                    "Não é um simples sim ou não — o art. 798 do Código Civil define um critério objetivo (Súmula 610 do STJ).", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "NOS PRIMEIROS 2 ANOS", "Só o <span class='hl'>suicídio</span><br>fica de fora",
                    "A exclusão vale só pra esse risco específico — qualquer outra causa de morte continua com direito normal à indenização desde o início.", 3, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "APÓS 2 ANOS", "A seguradora deve<br><span class='hl'>indenizar</span> normalmente",
                    "Mesmo que haja prova de premeditação — a Súmula 610 do STJ superou o entendimento antigo e subjetivo (Súmula 61).", 4, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Entenda o tipo de<br><span class='hl'>contrato</span> que você tem",
                    "Risco puro ou resgatável muda o que esperar em cada situação — vale confirmar com quem vendeu.", 5, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_04_doenca_preexistente():
    out = os.path.join(CONTENT, "semana-02", "post-04-caso-real-doenca-preexistente")
    photo = p("ref-pexels-doctor.jpg")
    total = 7
    slides = [
        photo_slide(LOGO, photo, "ATENÇÃO", "Doença preexistente pode<br>tirar seu direito ao <span class='hl'>seguro?</span>",
                    "Pode sim — mas só nesse caso específico.", 1, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "PRINCÍPIO BÁSICO", "Seguro é um contrato<br>de <span class='hl'>boa-fé</span>",
                    "Você precisa responder o questionário de saúde (DPS) com exatidão na contratação.", 2, total),
        photo_slide(LOGO, photo, "SE VOCÊ OMITIU DE PROPÓSITO", "Você perde o direito<br>à <span class='hl'>cobertura</span>",
                    "A Lei de Seguros (15.040/2024) é clara: má-fé comprovada anula seu direito à indenização.", 3, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "MAS ATENÇÃO", "Só vale para o que foi<br><span class='hl'>perguntado</span>",
                    "A seguradora não pode negar por algo que nunca constou no questionário de saúde.", 4, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "E MAIS", "Precisa ter relação<br>com o <span class='hl'>sinistro</span>",
                    "A doença omitida precisa ter nexo causal com o motivo do sinistro — não é qualquer omissão que conta.", 5, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O QUE FAZER NA PRÁTICA", "Responda a DPS com<br><span class='hl'>honestidade total</span>",
                    "Mesmo sintomas que parecem sem importância podem fazer diferença depois.", 6, total),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Boa-fé no início evita<br>dor de cabeça <span class='hl'>depois</span>",
                    "Contratar com honestidade é o que garante seu direito na hora que você mais precisa.", 7, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_05_papo_corretor():
    out = os.path.join(CONTENT, "semana-02", "post-05-papo-corretor")
    total = 6
    slides = [
        notebook_slide(LOGO, "PAPO DE CORRETOR", "A receita parada que<br>você já tem na <span class='hl'>carteira</span>",
                        [], "Com fonte. Não é achismo.", 1, total),
        notebook_slide(LOGO, "DADO", "Corretoras que sempre fazem cross-sell",
                        [{"label": "Sincor-SP, 2023", "value": "44%", "highlight": True}],
                        "Menos da metade das corretoras associadas sempre oferece outros seguros na interação com o cliente.", 2, total),
        notebook_slide(LOGO, "DADO", "Corretoras que nunca fazem cross-sell",
                        [{"label": "Sincor-SP, 2023", "value": "11%", "highlight": True}],
                        "1 em cada 9 corretoras simplesmente nunca oferece uma segunda cobertura pro mesmo cliente.", 3, total),
        notebook_slide(LOGO, "O QUE ISSO SIGNIFICA", "Muito cliente fica<br>com só <span class='hl'>1 apólice</span>",
                        [], "Não por falta de necessidade — por falta de alguém perguntar.", 4, total),
        notebook_slide(LOGO, "O QUE FAZER COM ISSO", "Revise a carteira,<br>não só a <span class='hl'>renovação</span>",
                        [], "Pergunte ativamente: esse cliente tem carro, casa, vida, e só uma dessas coberturas com você?", 5, total),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Não é sobre vender mais.<br>É sobre vender <span class='hl'>melhor</span>",
                        [], "Manda pra um colega corretor que precisa ver isso.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


if __name__ == "__main__":
    build_post_01_mito_roubo()
    build_post_02_vale_a_pena_residencial()
    build_post_03_mito_vida_suicidio()
    build_post_04_doenca_preexistente()
    build_post_05_papo_corretor()
    print("Lote 2 gerado.")
