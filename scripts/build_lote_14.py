"""Gera o Lote 14 — Mito: seguro viagem obrigatório na Europa; Mito: carro ligado/aberto x furto (STJ 2026);
Vale a pena: seguro de aluguel por temporada; Caso prático: franquia x vidros/faróis; Papo de Corretor: Open Insurance 2026.
Seguro saúde nunca entra."""


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
SEM = "semana-14"


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
    photo = p("ref-pexels-travel.jpg")
    t = 6
    return build("post-01-mito-seguro-viagem-europa", [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Seguro viagem é <span class='hl'>obrigatório</span><br>pra entrar na Europa?",
                    "Muita gente descobre a exigência só na hora de embarcar.", 1, t),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Verdade</span> — pra o espaço Schengen",
                    "Países como Portugal, França, Itália e Alemanha exigem seguro viagem com cobertura mínima de 30 mil euros para despesas médicas e hospitalares.", 2, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O VALOR", "Mínimo de <span class='hl'>€ 30.000</span> em despesas médicas",
                    "A apólice precisa valer durante toda a viagem e cobrir todos os países do roteiro.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "NA IMIGRAÇÃO", "Sem o comprovante, a entrada <span class='hl'>pode ser negada</span>",
                    "O agente de imigração pode pedir o comprovante do seguro. Leve a apólice impressa ou no celular.", 4, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "ETIAS", "Ainda <span class='hl'>sem data</span> confirmada",
                    "A previsão de início do ETIAS foi retirada do site oficial da UE em julho. Confira sempre o Portal Consular do Itamaraty antes de viajar.", 5, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Vai viajar? <span class='hl'>Contrate antes</span> de embarcar",
                    "Manda pra quem tem viagem pra Europa marcada.", 6, t),
    ])


def post_02():
    photo = p("ref-pexels-doorlock.jpg")
    t = 6
    return build("post-02-mito-carro-ligado-furto-stj", [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Deixou o carro <span class='hl'>ligado</span> pra abrir<br>o portão? Perde o seguro?",
                    "Uma decisão do STJ em 2026 mexeu com essa negativa.", 1, t),
        photo_slide(LOGO, photo, "A DECISÃO", "STJ afastou a negativa em <span class='hl'>2026</span>",
                    "A 3ª Turma, por unanimidade, afastou a recusa de cobertura em um caso de furto: a segurada deixou o carro aberto e ligado por instantes enquanto abria o portão.", 2, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "A TESE", "Quem prova o <span class='hl'>agravamento</span> é a seguradora",
                    "Para perder a garantia, a seguradora precisa comprovar que a conduta foi agravamento culposo ou doloso do risco e que foi determinante para o sinistro.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "NÃO BASTA", "Negligência simples <span class='hl'>não é</span> o suficiente",
                    "Em julgado anterior, o STJ manteve a negativa de carro deixado aberto com a chave na ignição, por considerar o agravamento voluntário e determinante.", 4, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "ATENÇÃO", "Cada caso <span class='hl'>depende</span> dos fatos",
                    "A decisão não vale como garantia automática. O que pesa é o contrato, a cláusula e a prova do que aconteceu.", 5, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Recebeu <span class='hl'>negativa</span>? Peça a cláusula por escrito",
                    "Manda pra quem já deixou o carro ligado na garagem.", 6, t),
    ])


def post_03():
    t = 6
    return build("post-03-vale-a-pena-seguro-aluguel-temporada", [
        notebook_slide(LOGO, "VALE A PENA?",
                       "Seguro pra aluguel de<br>temporada: <span class='hl'>vale a pena</span>?",
                       [], "Airbnb já tem proteção própria. Basta? 👇", 1, t),
        notebook_slide(LOGO, "O QUE O AIRBNB OFERECE", "AirCover: <span class='hl'>gratuito</span>, mas com limites",
                       [{"label": "Responsabilidade civil", "value": "lesões e bens de hóspedes", "highlight": True},
                        {"label": "Proteção contra danos", "value": "ao imóvel do anfitrião"}],
                       "Valores e regras mudam. Confira a página oficial do Airbnb.", 2, t),
        notebook_slide(LOGO, "O QUE FICA DE FORA", "Só vale pra reserva <span class='hl'>pela plataforma</span>",
                       [{"label": "Fora do AirCover", "value": "reservas diretas", "highlight": True},
                        {"label": "Exclusões típicas", "value": "desgaste normal, danos intencionais"}],
                       "Fontes divergem sobre limites; leia as exclusões de cada proteção.", 3, t),
        notebook_slide(LOGO, "SEGURO RESIDENCIAL COMUM", "Em geral <span class='hl'>não cobre</span> uso comercial",
                       [{"label": "Apólice residencial padrão", "value": "costuma excluir temporada", "highlight": True},
                        {"label": "Alternativa", "value": "apólice específica"}],
                       "Avise a seguradora que o imóvel é alugado por temporada.", 4, t),
        notebook_slide(LOGO, "APÓLICE ESPECÍFICA", "Pode incluir <span class='hl'>roubo por hóspede</span>",
                       [{"label": "Possíveis coberturas", "value": "responsabilidade civil", "highlight": True},
                        {"label": "Em alguns casos", "value": "perda de renda"}],
                       "As condições variam por seguradora e apólice.", 5, t),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Vale se o imóvel <span class='hl'>gira hóspedes</span>",
                       [], "Use o AirCover como base e compare uma apólice dedicada com um corretor. Salva e manda pro anfitrião que você conhece.", 6, t),
    ])


def post_04():
    photo = p("ref-pexels-bmw-damaged.jpg")
    t = 6
    return build("post-04-caso-pratico-franquia-vidros-farois", [
        photo_slide(LOGO, photo, "CASO PRÁTICO",
                    "Quebrou só o <span class='hl'>farol</span> e o<br>seguro não pagou. Por quê?",
                    "Caso ilustrativo, baseado em dúvida comum. Não é caso real identificável.", 1, t),
        photo_slide(LOGO, photo, "A SITUAÇÃO", "Dano <span class='hl'>pequeno</span>, conserto caro",
                    "Imagine um motorista que teve apenas um farol quebrado e acionou o seguro esperando reembolso total.", 2, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O PROBLEMA", "O conserto ficou <span class='hl'>abaixo da franquia</span>",
                    "Se o dano atinge só vidros, lanternas e faróis, o valor do reparo pode ser menor que a franquia da cobertura principal, e o segurado paga tudo.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "A SOLUÇÃO", "Existe garantia <span class='hl'>opcional</span>",
                    "Muitas seguradoras oferecem garantia de vidros, que costuma ter franquia menor. A versão completa pode incluir faróis, lanternas e retrovisores.", 4, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "DETALHE", "Pode exigir <span class='hl'>casco</span> contratado",
                    "Em alguns produtos, a garantia de faróis e retrovisores só pode ser contratada junto com a cobertura de casco. Franquias variam por seguradora.", 5, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Pergunte pela <span class='hl'>franquia de vidros</span>",
                    "Manda pra quem vai renovar o seguro do carro.", 6, t),
    ])


def post_05():
    t = 6
    return build("post-05-papo-corretor-open-insurance-2026", [
        notebook_slide(LOGO, "PAPO DE CORRETOR",
                       "Open Insurance em 2026:<br>onde o <span class='hl'>corretor</span> entra",
                       [], "Onde está o ecossistema e o que dá pra esperar. 👇", 1, t),
        notebook_slide(LOGO, "ONDE ESTAMOS", "Especialistas veem 2026 como ano de <span class='hl'>aplicação prática</span>",
                       [{"label": "Foco", "value": "proteção de dados", "highlight": True},
                        {"label": "Papel do corretor", "value": "fortalecido"}],
                       "Avaliação de especialistas, não uma norma.", 2, t),
        notebook_slide(LOGO, "CONSULTA PÚBLICA", "Susep abriu <span class='hl'>tomada de subsídios</span>",
                       [{"label": "Prorrogada até", "value": "05/05/2026", "highlight": True},
                        {"label": "Temas", "value": "governança, interoperabilidade"}],
                       "Também entraram certificações de jornada e monitoramento.", 3, t),
        notebook_slide(LOGO, "O GARGALO", "A demanda do consumidor ainda é <span class='hl'>baixa</span>",
                       [{"label": "Apontado pela CNseg", "value": "principal entrave", "highlight": True},
                        {"label": "Spocs autorizadas", "value": "2 (reportagem 2026)"}],
                       "Resultados concretos são projetados para 2027.", 4, t),
        notebook_slide(LOGO, "PRIORIDADE", "Revisão no grupo de <span class='hl'>prioridade máxima</span>",
                       [{"label": "Plano de Regulação 2026", "value": "segundo consultoria", "highlight": True}],
                       "Fonte secundária; confira no site da Susep.", 5, t),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Quem entende dados <span class='hl'>sai na frente</span>",
                       [], "Confira o texto oficial no site da Susep antes de aplicar. Manda pro colega corretor.", 6, t),
    ])


def post_06(src):
    out = os.path.join(CONTENT, SEM, "post-06-teste-domingo-seguro-viagem-europa")
    os.makedirs(out, exist_ok=True)
    for i in range(1, 7):
        shutil.copyfile(os.path.join(src, f"slide-{i:02d}.png"), os.path.join(out, f"slide-{i:02d}.png"))


if __name__ == "__main__":
    s1 = post_01()
    post_02(); post_03(); post_04(); post_05()
    post_06(s1)
    print("Lote 14 gerado.")
