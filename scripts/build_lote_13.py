"""Gera o Lote 13 — Mito: seguro de vida só paga na morte?; Mito: embriaguez x seguro de vida (Súmula 620 STJ);
Vale a pena: seguro de máquinas e equipamentos (Riscos Diversos); Caso prático: reforma em casa x seguro residencial;
Papo de Corretor: plano de regulação Susep 2026. Seguro saúde nunca entra."""

import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(__file__))
from templates import photo_slide, notebook_slide  # noqa: E402
from render_html import render  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
ASSETS = os.path.join(CONTENT, "assets")
LOGO = os.path.join(CONTENT, "logo.png").replace("\\", "/")
SEM = "semana-13"


def p(name):
    return os.path.join(ASSETS, name).replace("\\", "/")


def build(slug, slides):
    out = os.path.join(CONTENT, SEM, slug)
    os.makedirs(out, exist_ok=True)
    for i, html in enumerate(slides, 1):
        name = f"slide-{i:02d}"
        hp = os.path.join(out, f"{name}.html")
        with open(hp, "w", encoding="utf-8") as f:
            f.write(html)
        render(hp, os.path.join(out, f"{name}.png"))
    return out


def post_01():
    photo = p("ref-pexels-contract.jpg")
    t = 6
    return build("post-01-mito-seguro-vida-so-morte", [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Seguro de vida só paga<br>se você <span class='hl'>morrer</span>?",
                    "Muita gente descarta o seguro por achar que só a família se beneficia.", 1, t),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span> — há coberturas pra quem continua vivo",
                    "Além de morte natural ou acidental, planos podem incluir coberturas adicionais, como invalidez, doenças graves e diária por incapacidade.", 2, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "INVALIDEZ", "Por <span class='hl'>acidente</span> ou por doença",
                    "A invalidez por acidente pode ser total ou parcial, com perda ou redução funcional definitiva de membro ou órgão. Por doença, costuma exigir incapacidade funcional permanente.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "DOENÇAS GRAVES", "Adianta parte do capital <span class='hl'>em vida</span>",
                    "Em caso de diagnóstico de doença listada na apólice (como câncer, infarto ou AVC), o segurado pode receber um adiantamento. Geralmente é cobertura facultativa.", 4, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O DETALHE", "Tem <span class='hl'>carência, franquia</span> e exclusões",
                    "A diária por incapacidade (DIT) tem regras próprias de carência, franquia e limite de diárias. E doença grave não pode ser contratada depois de já diagnosticada.", 5, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Leia as <span class='hl'>condições gerais</span> antes de assinar",
                    "Manda pra quem acha que seguro de vida é só pra deixar herança.", 6, t),
    ])


def post_02():
    photo = p("ref-pexels-bmw-damaged.jpg")
    t = 6
    return build("post-02-mito-seguro-vida-embriaguez", [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Seguro de vida <span class='hl'>não paga</span><br>se o segurado estava bêbado?",
                    "É uma das negativas mais comuns — e nem sempre é válida.", 1, t),
        photo_slide(LOGO, photo, "A RESPOSTA", "Em regra, <span class='hl'>mito</span> — o STJ já decidiu",
                    "A Súmula 620 do STJ diz que a embriaguez do segurado não exime a seguradora de pagar a indenização do seguro de vida.", 2, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O FUNDAMENTO", "Nos seguros de pessoas, <span class='hl'>excluir</span> por isso é vedado",
                    "A jurisprudência veda excluir cobertura de seguro de pessoas por atos em estado de alcoolismo ou sob efeito de substâncias tóxicas.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "VALE PRA OUTROS", "Já foi aplicada em <span class='hl'>prestamista e habitacional</span>",
                    "Tribunais estaduais já estenderam a lógica a seguros com cobertura por morte, como prestamista e habitacional.", 4, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "ATENÇÃO", "<span class='hl'>Seguro auto</span> é outra história",
                    "A súmula é sobre seguro de vida. No seguro de carro, dirigir embriagado pode gerar recusa por agravamento do risco. Cada caso depende do contrato e da prova.", 5, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Recebeu <span class='hl'>negativa</span>? Peça por escrito",
                    "Manda pra alguém que precise saber disso.", 6, t),
    ])


def post_03():
    t = 6
    return build("post-03-vale-a-pena-seguro-maquinas-equipamentos", [
        notebook_slide(LOGO, "VALE A PENA?",
                       "Seguro de máquinas e<br>equipamentos: <span class='hl'>vale a pena</span>?",
                       [], "O que cobre, o que fica de fora e pra quem faz sentido 👇", 1, t),
        notebook_slide(LOGO, "O QUE COBRE", "Cobertura básica: acidente, roubo e <span class='hl'>incêndio</span>",
                       [{"label": "Acidentes", "value": "colisão, tombamento", "highlight": True},
                        {"label": "Roubo e furto", "value": "com arrombamento"},
                        {"label": "Fogo", "value": "incêndio, raio, explosão"}],
                       "É o seguro de Riscos Diversos (RD). A cobertura exata varia por seguradora e apólice.", 2, t),
        notebook_slide(LOGO, "QUAIS EQUIPAMENTOS", "Fixos, móveis, arrendados e <span class='hl'>até médicos</span>",
                       [{"label": "Modalidades", "value": "estacionários e móveis", "highlight": True},
                        {"label": "Também", "value": "terraplenagem, equip. médicos"}],
                       "Há modalidades pra equipamento arrendado ou cedido a terceiros.", 3, t),
        notebook_slide(LOGO, "O QUE FICA DE FORA", "Máquina <span class='hl'>agrícola</span> tem apólice própria",
                       [{"label": "RD comum", "value": "não cobre agro", "highlight": True},
                        {"label": "Alternativa", "value": "modalidade específica"}],
                       "Maquinário rural exige produto específico do ramo.", 4, t),
        notebook_slide(LOGO, "NOVIDADE DE MERCADO", "Produto novo vai até <span class='hl'>R$ 3 milhões</span>",
                       [{"label": "Limite por equipamento", "value": "até R$ 3 mi", "highlight": True},
                        {"label": "Idade da máquina", "value": "até 20 anos"}],
                       "Lançamento de seguradora, setembro/2026 (CQCS). É um exemplo, não regra de mercado.", 5, t),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Vale se a máquina parada <span class='hl'>quebra o seu caixa</span>",
                       [], "Compare o prêmio com o valor do equipamento e o prejuízo da parada. Peça cotação em mais de uma seguradora. Salva e manda pro empresário que você conhece.", 6, t),
    ])


def post_04():
    photo = p("ref-pexels-house.jpg")
    t = 6
    return build("post-04-caso-pratico-reforma-residencial", [
        photo_slide(LOGO, photo, "CASO PRÁTICO",
                    "Fez uma reforma em casa e<br>deu problema: o <span class='hl'>seguro<br>residencial cobre</span>?",
                    "Caso ilustrativo, baseado em dúvida comum. Não é caso real identificável.", 1, t),
        photo_slide(LOGO, photo, "A SITUAÇÃO", "Obra em andamento, <span class='hl'>dano no imóvel</span>",
                    "Imagine que durante a reforma houve um dano e o morador aciona o seguro residencial esperando indenização.", 2, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O PROBLEMA", "Apólices têm <span class='hl'>exclusões gerais</span>",
                    "Todo seguro residencial registrado na Susep traz uma seção de exclusões. É nela que se confere se danos ligados a obras estão fora.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "OUTRO PRODUTO", "Obra tem seguro <span class='hl'>próprio</span>",
                    "A CNseg aponta o seguro de Riscos de Engenharia como ferramenta relevante também para pequenas reformas.", 4, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O QUE FAZER", "Pergunte <span class='hl'>antes</span> de começar a obra",
                    "Peça por escrito ao corretor ou à seguradora se danos durante reforma estão cobertos. Depois do sinistro, é tarde.", 5, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Reforma à vista? <span class='hl'>Confira a apólice</span>",
                    "Manda pra quem vai reformar a casa.", 6, t),
    ])


def post_05():
    t = 6
    return build("post-05-papo-corretor-plano-regulacao-susep-2026", [
        notebook_slide(LOGO, "PAPO DE CORRETOR",
                       "Plano de Regulação da Susep 2026:<br>o que o <span class='hl'>corretor</span> acompanha",
                       [], "A agenda normativa do ano e o que já virou norma.", 1, t),
        notebook_slide(LOGO, "A BASE", "Resolução Susep 72/2025 definiu a <span class='hl'>agenda</span>",
                       [{"label": "Aprovada em", "value": "17/12/2025", "highlight": True},
                        {"label": "Publicada no DOU", "value": "22/12/2025"}],
                       "O plano lista temas com prazo, unidade responsável e prioridade.", 2, t),
        notebook_slide(LOGO, "PRIORIDADES", "<span class='hl'>P1</span> é central, P2 conforme a capacidade",
                       [{"label": "P1", "value": "temas estratégicos", "highlight": True},
                        {"label": "P2", "value": "conforme tempo e recursos"}],
                       "O que está em P1 tende a sair primeiro.", 3, t),
        notebook_slide(LOGO, "AJUSTE DE AGOSTO", "Resolução Susep 91 <span class='hl'>reescreveu a tabela</span>",
                       [{"label": "Decisão do Conselho", "value": "12/08/2026", "highlight": True},
                        {"label": "Resolução", "value": "nº 91, 18/08/2026"}],
                       "Substitui o Anexo I da Resolução 72. Entre os temas: adequação de normas à Lei 15.040/2024.", 4, t),
        notebook_slide(LOGO, "JÁ VIROU NORMA", "Regras de corretor foram <span class='hl'>consolidadas</span>",
                       [{"label": "Resolução CNSP", "value": "nº 493/2026", "highlight": True},
                        {"label": "Inclui", "value": "devolução de comissão"}],
                       "O plano previa revisar as normas da categoria. A 493/2026 consolida regras de corretores, autorreguladoras e escolas.", 5, t),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Regulação muda, <span class='hl'>quem acompanha</span> sai na frente",
                       [], "Confira o texto oficial no site da Susep antes de aplicar. Manda pro colega corretor.", 6, t),
    ])


def post_06(src):
    out = os.path.join(CONTENT, SEM, "post-06-teste-domingo-seguro-vida-so-morte")
    os.makedirs(out, exist_ok=True)
    for i in range(1, 7):
        shutil.copyfile(os.path.join(src, f"slide-{i:02d}.png"), os.path.join(out, f"slide-{i:02d}.png"))


if __name__ == "__main__":
    s1 = post_01()
    post_02(); post_03(); post_04(); post_05()
    post_06(s1)
    print("Lote 13 gerado.")
