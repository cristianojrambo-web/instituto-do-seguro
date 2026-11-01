"""Gera o Lote 15 — Mito: carro reserva/guincho; Mito: seguro de vida cotas fixas (STJ 2026); Vale a pena: seguro energia solar;
Caso pratico: vazamento subito x gradual; Papo de Corretor: IOF VGBL e tabela de IR. Seguro saude nunca entra."""


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
SEM = "semana-15"


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
    photo = p("ref-pexels-crash.jpg")
    t = 6
    return build("post-01-mito-carro-reserva-guincho", [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Todo seguro auto inclui<br><span class='hl'>carro reserva</span> e guincho ilimitado?",
                    "Muita gente só descobre o limite na hora do aperto.", 1, t),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span> — depende do plano",
                    "Carro reserva costuma ser cobertura adicional. Em material da Allianz, por exemplo, aparece como não contratado, 7, 15 ou 30 dias.", 2, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "GUINCHO", "Tem limite de <span class='hl'>quilômetros</span>",
                    "No mesmo material da Allianz, o guincho aparece com opções de 200 km, 500 km ou km livre. Cada seguradora define o seu.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "ASSISTÊNCIA 24H", "Pode ter <span class='hl'>limite de uso</span>",
                    "Alguns guias de seguradoras limitam o número de acionamentos por pane na vigência. Confira o da sua apólice.", 4, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "ANTES DE ACIONAR", "Leia as <span class='hl'>condições gerais</span>",
                    "Veja se o carro reserva foi contratado, por quantos dias e em quais situações vale.", 5, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Sabe quantos dias de <span class='hl'>carro reserva</span> você tem?",
                    "Manda pra quem vai renovar o seguro do carro.", 6, t),
    ])


def post_02():
    photo = p("ref-pexels-contract.jpg")
    t = 6
    return build("post-02-mito-seguro-vida-cotas-beneficiarios", [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Beneficiário morreu?<br>O outro <span class='hl'>fica com tudo</span>?",
                    "Uma decisão do STJ em 2026 trata desse caso.", 1, t),
        photo_slide(LOGO, photo, "A DECISÃO", "Com <span class='hl'>cotas fixas</span>, não",
                    "A 3ª Turma do STJ (REsp 2.203.542/RS) entendeu que, se o segurado fixou a parte de cada um, a cota de quem morreu antes não vai para o outro beneficiário.", 2, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "PARA QUEM VAI?", "Para os <span class='hl'>herdeiros do segurado</span>",
                    "Segundo a relatora, ministra Nancy Andrighi, a cota do beneficiário falecido antes do segurado pertence aos herdeiros do segurado (art. 792 do Código Civil).", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "SEM COTAS", "Sem percentuais, o capital é <span class='hl'>dividido</span>",
                    "Quando a indicação é conjunta e sem cotas definidas, a morte de um beneficiário faz o capital ser dividido entre os sobreviventes.", 4, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "ATENÇÃO", "Vale <span class='hl'>revisar</span> a apólice",
                    "Beneficiário mudou de situação? Atualizar a indicação evita surpresa para a família. Casos concretos pedem orientação jurídica.", 5, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Quando foi a última vez que revisou seus <span class='hl'>beneficiários</span>?",
                    "Manda pra quem tem seguro de vida.", 6, t),
    ])


def post_03():
    t = 6
    return build("post-03-vale-a-pena-seguro-energia-solar", [
        notebook_slide(LOGO, "VALE A PENA?",
                       "Seguro pra energia solar:<br><span class='hl'>vale a pena</span>?",
                       [], "Garantia do fabricante basta? 👇", 1, t),
        notebook_slide(LOGO, "GARANTIA x SEGURO", "Garantia cobre <span class='hl'>defeito</span>, seguro cobre <span class='hl'>causa externa</span>",
                       [{"label": "Garantia do fabricante", "value": "defeito de fabricação", "highlight": True},
                        {"label": "Seguro", "value": "danos externos"}],
                       "Segundo corretoras e sites do setor solar.", 2, t),
        notebook_slide(LOGO, "O QUE COSTUMA COBRIR", "Vendaval, granizo, incêndio e <span class='hl'>roubo</span>",
                       [{"label": "Cobertura básica", "value": "incêndio, raio, explosão", "highlight": True},
                        {"label": "Também", "value": "vendaval, granizo, roubo"}],
                       "Geada e outras coberturas dependem da seguradora.", 3, t),
        notebook_slide(LOGO, "O QUE FICA DE FORA", "Manutenção e <span class='hl'>greves</span> em geral não entram",
                       [{"label": "Exclusões citadas", "value": "reparo e manutenção", "highlight": True},
                        {"label": "Também", "value": "greve, guerra, terrorismo"}],
                       "Leia exclusões, franquia e limites antes de contratar.", 4, t),
        notebook_slide(LOGO, "QUANTO CUSTA", "Em torno de <span class='hl'>1% a 2%</span> do projeto",
                       [{"label": "Projeto de R$ 50 mil", "value": "~ R$ 500 a R$ 1.000/ano", "highlight": True}],
                       "Estimativa de fontes do setor; varia por seguradora e perfil.", 5, t),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Tende a valer em <span class='hl'>região de temporal</span>",
                       [], "Compare apólices com um corretor. Salva e manda pra quem instalou painéis.", 6, t),
    ])


def post_04():
    photo = p("ref-pexels-house.jpg")
    t = 6
    return build("post-04-caso-pratico-vazamento-subito-gradual", [
        photo_slide(LOGO, photo, "CASO PRÁTICO",
                    "Cano vazou e o seguro<br>residencial <span class='hl'>não pagou</span>. Por quê?",
                    "Caso ilustrativo, baseado em dúvida comum. Não é caso real identificável.", 1, t),
        photo_slide(LOGO, photo, "A SITUAÇÃO", "Mancha na parede, <span class='hl'>meses depois</span>",
                    "Imagine uma moradora que notou infiltração e acionou o seguro, esperando cobertura do reparo.", 2, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O PROBLEMA", "Vazamento <span class='hl'>gradual</span> costuma ficar de fora",
                    "Apólices em geral cobrem rompimento súbito e acidental. Desgaste, corrosão, falta de manutenção e infiltração progressiva costumam ser excluídos.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "SE FOSSE SÚBITO", "Rompimento repentino é <span class='hl'>tratado diferente</span>",
                    "Cano que estoura de repente pode ter cobertura, com limites para localizar o vazamento e remover entulho.", 4, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "ASSISTÊNCIA", "Não confunda com <span class='hl'>assistência residencial</span>",
                    "O serviço de reparo hidráulico tem regras e limites próprios, e costuma excluir quebra de parede, teto ou piso.", 5, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Guarde registro de <span class='hl'>manutenção</span>",
                    "Manda pra quem mora em imóvel com cano antigo.", 6, t),
    ])


def post_05():
    t = 6
    return build("post-05-papo-corretor-iof-vgbl-tabela-ir", [
        notebook_slide(LOGO, "PAPO DE CORRETOR",
                       "Previdência: IOF no VGBL e<br>a escolha da <span class='hl'>tabela de IR</span>",
                       [], "Dois pontos que mudam a conversa com o cliente. 👇", 1, t),
        notebook_slide(LOGO, "IOF NO VGBL", "5% sobre aportes acima de <span class='hl'>R$ 600 mil</span>/ano",
                       [{"label": "Limite em 2026", "value": "R$ 600 mil por CPF", "highlight": True},
                        {"label": "Soma", "value": "todas as seguradoras"}],
                       "Base: Decreto 12.499/2025. Fonte divergente diz que foi revogado: confirme.", 2, t),
        notebook_slide(LOGO, "EFEITO NO MERCADO", "Fenaprevi aponta <span class='hl'>queda na captação</span>",
                       [{"label": "Exemplo citado", "value": "R$ 400 mil acima = R$ 20 mil", "highlight": True},
                        {"label": "PGBL", "value": "sem esse IOF"}],
                       "Cálculo ilustrativo: 5% do excedente.", 3, t),
        notebook_slide(LOGO, "TABELA DE IR", "Escolha agora é no <span class='hl'>1º resgate</span>",
                       [{"label": "Lei 14.803/2024", "value": "opção no resgate", "highlight": True},
                        {"label": "Antes", "value": "na contratação"}],
                       "Regressiva: de 35% a 10%. Progressiva: faixas do IR.", 4, t),
        notebook_slide(LOGO, "PGBL x VGBL", "PGBL deduz até <span class='hl'>12%</span> da renda bruta",
                       [{"label": "PGBL", "value": "IR sobre o total", "highlight": True},
                        {"label": "VGBL", "value": "IR sobre rendimentos"}],
                       "Dedução vale na declaração completa.", 5, t),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Explicar imposto <span class='hl'>gera confiança</span>",
                       [], "Confirme normas e tabelas vigentes antes de orientar. Manda pro colega corretor.", 6, t),
    ])


def post_06(src):
    out = os.path.join(CONTENT, SEM, "post-06-teste-domingo-seguro-vida-cotas-beneficiarios")
    os.makedirs(out, exist_ok=True)
    for i in range(1, 7):
        shutil.copyfile(os.path.join(src, f"slide-{i:02d}.png"), os.path.join(out, f"slide-{i:02d}.png"))


if __name__ == "__main__":
    post_01()
    s2 = post_02()
    post_03(); post_04(); post_05()
    post_06(s2)
    print("Lote 15 gerado.")
