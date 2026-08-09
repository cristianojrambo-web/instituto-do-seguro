"""Gera o Lote 3 — ramo da semana: Seguro Saude (+ Seguro Viagem, ramos novos)."""

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


def build_post_01_mito_saude():
    out = os.path.join(CONTENT, "semana-03", "post-01-mito-seguro-saude")
    photo = p("ref-pexels-doctor.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Seguro saúde te protege<br>menos que <span class='hl'>plano de saúde</span>?",
                    "A resposta desmonta uma confusão que até corretor às vezes tem.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span> — mesma lei, mesma agência",
                    "Desde 2001 (Lei 10.185), seguro saúde saiu da SUSEP e passou a ser fiscalizado pela ANS — igual plano de saúde.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "MESMA LEI PRA AMBOS", "A Lei 9656/98 regula<br><span class='hl'>os dois</span>, sem diferença",
                    "Carência, urgência em 24h, rol de procedimentos obrigatório — as mesmas regras valem pra seguradora especializada e pra operadora de plano.", 3, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "ENTÃO QUAL A DIFERENÇA", "Não é proteção —<br>é <span class='hl'>modelo de acesso</span>",
                    "Seguro saúde tende a funcionar por reembolso e livre escolha de médico; plano de saúde, por rede credenciada. Hoje os dois modelos se misturam no mercado.", 4, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "ANTES DE CONTRATAR", "Confirme o registro<br>na <span class='hl'>ANS</span>",
                    "Todo produto de saúde regulado — seguro ou plano — tem número de registro consultável no site da ANS. Sem isso, desconfie.", 5, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Seguro saúde não é<br>'sem regra' — é <span class='hl'>regulado igual</span>",
                    "Manda pra quem está decidindo entre os dois achando que um é mais seguro que o outro.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_02_mito_viagem():
    out = os.path.join(CONTENT, "semana-03", "post-02-mito-seguro-viagem")
    total = 6
    slides = [
        notebook_slide(LOGO, "MITO OU VERDADE",
                        "Seguro viagem só serve<br>pra quem vai pro <span class='hl'>exterior</span>?",
                        [], "Separamos o que a maioria não sabe sobre esse seguro 👇", 1, total),
        notebook_slide(LOGO, "A RESPOSTA", "É mito",
                        [{"label": "Resposta", "value": "SIM", "highlight": True}],
                        "E o motivo pode te surpreender.", 2, total),
        notebook_slide(LOGO, "DADO", "Brasileiros que viajaram ao exterior sem seguro em 2025",
                        [{"label": "Do total de 28,4 milhões", "value": "25,3 mi sem seguro", "highlight": True}],
                        "Quase 9 em cada 10 viajantes saíram do país sem nenhuma cobertura.", 3, total),
        notebook_slide(LOGO, "VIAGEM NACIONAL", "Também cobre<br>dentro do <span class='hl'>Brasil</span>",
                        [{"label": "Cobertura nacional", "value": "médica, odontológica, bagagem"}],
                        "Por menos de R$10/dia dá pra ter cobertura básica em qualquer viagem dentro do país.", 4, total),
        notebook_slide(LOGO, "FORA DO PAÍS", "Pra Europa,<br>é <span class='hl'>obrigatório</span>",
                        [{"label": "Zona Schengen exige", "value": "mín. €30 mil", "highlight": True}],
                        "Regulamento (CE) nº 810/2009 — sem apólice válida, você pode ser barrado na imigração.", 5, total),
        notebook_slide(LOGO, "GUARDA ISSO", "Viagem sem seguro é<br>risco <span class='hl'>evitável</span>",
                        [], "Manda pra quem tem viagem marcada e ainda não pensou nisso.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_03_vale_a_pena_saude():
    out = os.path.join(CONTENT, "semana-03", "post-03-vale-a-pena-saude")
    total = 6
    slides = [
        notebook_slide(LOGO, "VALE A PENA?",
                        "Seguro Saúde:<br>os mitos que travam<br>a <span class='hl'>decisão</span>",
                        [], "4 mitos que ainda confundem quem está escolhendo entre seguro e plano 👇", 1, total),
        notebook_slide(LOGO, "MITO 1", "\"Só rico contrata<br>seguro saúde\"",
                        [{"label": "É mito?", "value": "SIM", "highlight": True}],
                        "Existem faixas de preço bem mais baixas — planos regionais com coparticipação chegam a custar a partir de R$100/mês pras faixas etárias mais jovens.", 2, total),
        notebook_slide(LOGO, "MITO 2", "\"Cobre só<br>emergência\"",
                        [{"label": "É mito?", "value": "SIM", "highlight": True}],
                        "Segue o mesmo rol de procedimentos obrigatório da ANS — consulta, exame, cirurgia e internação entram na cobertura, igual plano de saúde.", 3, total),
        notebook_slide(LOGO, "MITO 3", "\"Trocar de seguradora<br>é recomeçar carência\"",
                        [{"label": "É mito?", "value": "SIM", "highlight": True}],
                        "A portabilidade de carências (RN 438/2018, ANS) permite trocar sem cumprir carência de novo, se o plano novo tiver preço igual ou menor.", 4, total),
        notebook_slide(LOGO, "MITO 4", "\"Plano da empresa<br>já é suficiente\"",
                        [{"label": "É mito?", "value": "SIM", "highlight": True}],
                        "Plano empresarial normalmente acaba quando você sai do emprego — sem um seguro próprio, a cobertura pra depois some junto com o cargo.", 5, total),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Sim — mas exige<br>comparar <span class='hl'>direito</span>",
                        [], "Guarda esse carrossel e usa como checklist antes de decidir entre seguro e plano de saúde.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_04_caso_real_urgencia():
    out = os.path.join(CONTENT, "semana-03", "post-04-caso-real-carencia-urgencia")
    photo = p("ref-pexels-contract.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "ATENÇÃO",
                    "Sua seguradora negou<br>atendimento de <span class='hl'>urgência</span><br>por causa da carência?",
                    "Isso pode ser ilegal — e a lei já resolveu esse caso há anos.", 1, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "A REGRA", "Carência máxima pra<br>urgência: <span class='hl'>24 horas</span>",
                    "Art. 12, V, 'c' da Lei 9656/98 — prazo de ordem pública, nenhum contrato pode estender isso.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O QUE CONTA", "Risco de vida ou<br><span class='hl'>acidente</span> conta como urgência",
                    "Art. 35-C: emergência é risco imediato de vida ou lesão irreparável; urgência inclui acidentes pessoais e complicações na gravidez.", 3, total),
        photo_slide(LOGO, photo, "JÁ FOI PRA JUSTIÇA", "Súmula 103 do<br><span class='hl'>TJSP</span> é clara",
                    "\"É abusiva a negativa de cobertura em urgência/emergência a pretexto de carência\" além das 24h — entendimento confirmado pelo TJDFT em 2025.", 4, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "SE ACONTECER COM VOCÊ", "Documente e reclame<br>na <span class='hl'>ANS</span>",
                    "Guarde a negativa por escrito e registre reclamação — negativa fora da regra pode ser revertida, inclusive na Justiça.", 5, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Carência de 24h não é<br>sugestão — é <span class='hl'>lei</span>",
                    "Manda pra alguém que já passou por uma negativa parecida.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_05_papo_corretor_viagem():
    out = os.path.join(CONTENT, "semana-03", "post-05-papo-corretor-viagem")
    total = 6
    slides = [
        notebook_slide(LOGO, "PAPO DE CORRETOR",
                        "O ramo que mais cresce<br>e quase ninguém<br><span class='hl'>vende</span>",
                        [], "Com fonte. Não é achismo.", 1, total),
        notebook_slide(LOGO, "DADO", "Crescimento do seguro viagem em 2026",
                        [{"label": "Projeção CNseg", "value": "+12,2%", "highlight": True}],
                        "Um dos ramos que mais cresce no mercado segurador brasileiro este ano.", 2, total),
        notebook_slide(LOGO, "DADO", "Brasileiros que viajaram ao exterior sem seguro",
                        [{"label": "Em 2025", "value": "25,3 milhões", "highlight": True}],
                        "De 28,4 milhões que saíram do país, a maioria não tinha nenhuma cobertura.", 3, total),
        notebook_slide(LOGO, "COMISSÃO", "Um dos ramos com<br>melhor <span class='hl'>remuneração</span>",
                        [{"label": "Comissão média", "value": "até 30%", "highlight": True}],
                        "Acima da média de boa parte dos outros produtos que você já vende.", 4, total),
        notebook_slide(LOGO, "O QUE FAZER COM ISSO", "Pergunte na<br>próxima <span class='hl'>renovação</span>",
                        [], "Cliente de auto ou vida tem viagem marcada? Essa pergunta simples já é uma venda a mais na carteira.", 5, total),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Não é sobre vender mais.<br>É sobre <span class='hl'>não deixar</span> na mesa",
                        [], "Manda pra um colega corretor que ainda não oferece viagem no combo.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


if __name__ == "__main__":
    build_post_01_mito_saude()
    build_post_02_mito_viagem()
    build_post_03_vale_a_pena_saude()
    build_post_04_caso_real_urgencia()
    build_post_05_papo_corretor_viagem()
    print("Lote 3 gerado.")
