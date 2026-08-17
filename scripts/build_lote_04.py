"""Gera o Lote 4 — ramos da semana: Seguro Empresarial, Seguro Auto, Equipamentos Agrícolas,
Previdência Privada (+ regra geral de mora, caso real). Seguro saúde nunca entra (fora do
escopo real do usuário)."""

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


def build_post_01_mito_empresarial():
    out = os.path.join(CONTENT, "semana-04", "post-01-mito-empresarial")
    photo = p("ref-pexels-contract.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Empresa pequena não<br>precisa de <span class='hl'>seguro empresarial</span>?",
                    "A maioria das PMEs brasileiras aposta que não vai precisar.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span> — e o dado assusta",
                    "Mais de 60% das pequenas e médias empresas no Brasil operam sem proteção adequada contra incêndio, roubo, danos elétricos ou responsabilidade civil.", 2, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "DIMENSÃO DO PROBLEMA", "Isso é quase<br><span class='hl'>todo</span> negócio do país",
                    "Micro e pequenas empresas são 97% dos negócios ativos no Brasil — 21,7 milhões de empreendimentos, responsáveis por 26,5% do PIB (Sebrae).", 3, total),
        photo_slide(LOGO, photo, "O QUE COBRE", "O seguro empresarial<br>básico <span class='hl'>protege</span> isso",
                    "Multirrisco (incêndio, roubo, danos elétricos), responsabilidade civil geral, equipamentos eletrônicos — e cada vez mais, seguro cyber básico pra dados de cliente.", 4, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "CUSTO REAL", "Não precisa ser<br><span class='hl'>caro</span>",
                    "MEI e pequenas empresas com cobertura básica pagam entre R$80 e R$150/mês; empresas médias com cobertura completa, R$300 a R$500/mês.", 5, total),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Antes de abrir as portas,<br>cota um <span class='hl'>seguro</span>",
                    "Manda pra quem tem negócio próprio e nunca parou pra cotar um seguro empresarial.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_02_mito_auto_terceiro():
    out = os.path.join(CONTENT, "semana-04", "post-02-mito-auto-terceiro-nao-identificado")
    photo = p("ref-pexels-bumper-yellow.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Bateram no seu carro e<br>o motorista <span class='hl'>fugiu</span>?",
                    "Muita gente acha que, sem saber quem foi, o seguro nunca cobre.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "Depende de <span class='hl'>um fator só</span>",
                    "Não tem a ver com achar o culpado. Tem a ver com o tipo de cobertura que você contratou — e isso é regra de contrato, não depende de decisão judicial.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "SE VOCÊ TEM ISSO", "Compreensiva ou colisão?<br><span class='hl'>Cobre sempre</span>",
                    "Com essa cobertura, seu carro está protegido mesmo sem identificar quem bateu — é assim que a cobertura funciona, com ou sem culpado encontrado.", 3, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "ATENÇÃO AO TIPO", "RCF-V <span class='hl'>nunca</span><br>cobre o seu carro",
                    "RCF-V (Responsabilidade Civil Facultativa a Terceiros) cobre só o que VOCÊ causa a terceiros — não indeniza o seu carro, com ou sem motorista identificado.", 4, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "FIQUE ATENTO", "Alguns contratos<br>tentam <span class='hl'>limitar isso</span>",
                    "Já houve seguradora negando cobertura compreensiva citando 'terceiro não identificado' — o TJMG entendeu abusivo quando a cláusula de exclusão não é clara e destacada (Apelação Cível 1.0000.22.102233-0/001).", 5, total),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Confira sua cobertura<br>antes de <span class='hl'>precisar</span>",
                    "Manda pra quem não sabe se tem compreensiva ou só RCF-V.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_03_vale_a_pena_agro():
    out = os.path.join(CONTENT, "semana-04", "post-03-vale-a-pena-equipamentos-agricolas")
    total = 6
    slides = [
        notebook_slide(LOGO, "VALE A PENA?",
                        "Seguro de Equipamentos<br>Agrícolas: vale a <span class='hl'>pena</span>?",
                        [], "Trator, colheitadeira, pulverizador — separamos os números antes de você decidir 👇", 1, total),
        notebook_slide(LOGO, "COBERTURA", "O que entra na<br><span class='hl'>proteção</span>",
                        [{"label": "Incêndio e roubo/furto", "value": "cobre"},
                         {"label": "Tombamento", "value": "cobre"},
                         {"label": "Danos elétricos", "value": "cobre"},
                         {"label": "Danos a terceiros", "value": "cobre", "highlight": True}],
                        "Vale pra trator, colheitadeira, plantadeira, enfardadeira e pulverizador.", 2, total),
        notebook_slide(LOGO, "CRESCIMENTO", "O ramo está<br><span class='hl'>disparando</span>",
                        [{"label": "Contratações no 1º semestre", "value": "+22%", "highlight": True},
                         {"label": "Nº de apólices", "value": "+12%"}],
                        "Dado de uma das maiores seguradoras do ramo — o trator é hoje o equipamento mais contratado, à frente da colheitadeira.", 3, total),
        notebook_slide(LOGO, "CUSTO", "Quanto custa<br><span class='hl'>proteger</span> a máquina",
                        [{"label": "Colheitadeira / ano", "value": "R$4mil a R$20mil", "highlight": True}],
                        "Varia com o ano e o valor do equipamento — uma fração do prejuízo de perder a máquina na safra.", 4, total),
        notebook_slide(LOGO, "ONDE MAIS CRESCE", "A demanda tem<br><span class='hl'>endereço</span>",
                        [{"label": "Paraná", "value": "+17% da carteira", "highlight": True},
                         {"label": "Norte/Centro-Oeste + Sul", "value": "~70% das vendas"}],
                        "Se você atende produtor rural nessas regiões, essa é pauta de venda pronta.", 5, total),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Sim — e o mercado<br>já <span class='hl'>confirma</span>",
                        [], "Guarda esse carrossel e usa como referência antes da próxima safra.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_04_caso_real_mora():
    out = os.path.join(CONTENT, "semana-04", "post-04-caso-real-mora-premio")
    photo = p("ref-pexels-house.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "ATENÇÃO",
                    "Atrasar uma parcela pode<br>custar a <span class='hl'>indenização</span> inteira?",
                    "Caso ilustrativo, baseado em situação real e comum entre segurados.", 1, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "PARCELA ÚNICA OU 1ª", "Nesse caso, é<br><span class='hl'>automático</span>",
                    "Pela Lei 15.040/2024, atraso na parcela única ou na 1ª parcela do prêmio resolve o contrato automaticamente — sem aviso prévio, salvo acordo em contrário.", 2, total),
        photo_slide(LOGO, photo, "PARCELAS SEGUINTES", "Aí sim, tem um<br><span class='hl'>prazo</span>",
                    "A seguradora precisa notificar o segurado, dando no mínimo 15 dias (a partir do recebimento) pra quitar o atraso antes de qualquer suspensão.", 3, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "SE NÃO PAGAR", "A cobertura fica<br><span class='hl'>suspensa</span>",
                    "A partir da notificação, a garantia é suspensa; a resolução definitiva do contrato só pode acontecer 30 dias depois dessa suspensão.", 4, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "SE ISSO ACONTECER", "Não ignore a<br><span class='hl'>notificação</span>",
                    "Ela define o prazo exato que você tem pra regularizar o pagamento e manter a cobertura ativa.", 5, total),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Prêmio em dia é a<br>garantia mais <span class='hl'>barata</span>",
                    "Manda pra alguém que já deixou uma parcela atrasar sem saber o risco.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


def build_post_05_papo_corretor_previdencia():
    out = os.path.join(CONTENT, "semana-04", "post-05-papo-corretor-previdencia")
    total = 6
    slides = [
        notebook_slide(LOGO, "PAPO DE CORRETOR",
                        "O produto de <span class='hl'>R$1,8 trilhão</span><br>que talvez você não ofereça",
                        [], "Com fonte. Não é achismo.", 1, total),
        notebook_slide(LOGO, "DADO", "O mercado de<br><span class='hl'>previdência privada</span>",
                        [{"label": "Ativos sob gestão (jan/2026)", "value": "R$1,8 tri", "highlight": True},
                         {"label": "Crescimento vs. 2025", "value": "+13,2%"}],
                        "Equivale a cerca de 14% do PIB brasileiro — e continua subindo.", 2, total),
        notebook_slide(LOGO, "DADO", "Uma base gigante de<br>clientes em <span class='hl'>potencial</span>",
                        [{"label": "Participantes", "value": "11,2 milhões", "highlight": True},
                         {"label": "Planos ativos", "value": "13,7 milhões"}],
                        "E muitos deles ainda não têm um corretor acompanhando de perto.", 3, total),
        notebook_slide(LOGO, "PGBL X VGBL", "A diferença que<br><span class='hl'>fecha venda</span>",
                        [{"label": "PGBL", "value": "deduz até 12% da renda"},
                         {"label": "VGBL", "value": "imposto só no rendimento"}],
                        "PGBL vale pra quem declara IR completo; VGBL, pra quem já bateu o teto do PGBL ou usa declaração simplificada.", 4, total),
        notebook_slide(LOGO, "O QUE FAZER COM ISSO", "Pergunte na<br>próxima <span class='hl'>renovação</span>",
                        [], "Cliente de auto ou vida já tem previdência? E sabe qual dos dois produtos combina com a declaração dele?", 5, total),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Não é vender mais.<br>É não deixar <span class='hl'>na mesa</span>",
                        [], "Manda pra um colega corretor que só vende auto e vida.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)


if __name__ == "__main__":
    build_post_01_mito_empresarial()
    build_post_02_mito_auto_terceiro()
    build_post_03_vale_a_pena_agro()
    build_post_04_caso_real_mora()
    build_post_05_papo_corretor_previdencia()
    print("Lote 4 gerado.")
