"""Gera o Lote 10 — ramos da semana: Seguro Residencial (seguro-incêndio na locação, Lei do
Inquilinato — ramo já usado, ângulo inteiramente novo: locação), Seguro Rural (ramo inteiramente
novo no canal, cobertura climática via PSR), Seguro Prestamista (ramo inteiramente novo no canal,
direitos do consumidor em financiamento/empréstimo), Seguro de Transporte de Cargas — RCTR-C/RC-DC/
RC-V (ramo inteiramente novo no canal, Lei 14.599/2023 + Resolução ANTT 6.068/2025) e Papo de
Corretor sobre a Resolução CNSP 493/2026 (educação continuada como dever formal, vigência
17/01/2027). Seguro saúde nunca entra (fora do escopo real do usuário)."""

import os
import shutil
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


def build_post_01_mito_inquilinato():
    out = os.path.join(CONTENT, "semana-10", "post-01-mito-seguro-incendio-locacao")
    photo = p("ref-pexels-house.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Mora de aluguel? O seguro<br>contra incêndio do imóvel é<br><span class='hl'>obrigação sua</span>, não do dono?",
                    "A resposta é mais específica do que parece — e pode estar custando dinheiro do jeito errado.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Depende do contrato</span> — mas a lei aponta pro dono",
                    "A Lei do Inquilinato (art. 22, VIII) diz que é o locador quem paga o seguro complementar contra fogo do imóvel, salvo cláusula em contrário no contrato.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "NA PRÁTICA", "Quase todo contrato <span class='hl'>transfere</span> essa conta pro inquilino",
                    "A lei permite a transferência por cláusula expressa — e é isso que a maioria dos contratos padrão de locação já inclui.", 3, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "ANTES DE ASSINAR", "Confira se essa cláusula <span class='hl'>está mesmo</span> no seu contrato",
                    "Sem cláusula expressa transferindo a obrigação, a conta continua sendo do proprietário — não do inquilino, por lei.", 4, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "ATENÇÃO", "Seguro-incêndio da locação <span class='hl'>não é</span> seguro residencial completo",
                    "Ele cobre só o imóvel contra fogo; conteúdo, roubo e responsabilidade civil exigem uma apólice residencial separada, por fora do contrato de aluguel.", 5, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Confirma no contrato <span class='hl'>quem paga</span> o quê antes do próximo boleto",
                    "Manda pra quem mora de aluguel e nunca leu essa cláusula até hoje.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_02_mito_seguro_rural():
    out = os.path.join(CONTENT, "semana-10", "post-02-mito-seguro-rural-clima")
    photo = p("ref-pexels-colheitadeira.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Geada, seca ou granizo<br>destruíram a lavoura — o seguro<br>rural cobre <span class='hl'>automaticamente</span>?",
                    "Poucos produtores sabem o que realmente precisa estar na apólice pra esse prejuízo virar indenização.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span> — só cobre o que está descrito na apólice",
                    "Seguro rural cobre risco climático (seca, geada, granizo, tempestade) só quando essa cobertura específica está contratada e documentada com laudo técnico da lavoura.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O SUBSÍDIO DO GOVERNO", "De <span class='hl'>30% a 40%</span> do prêmio, pago pela União",
                    "É o PSR (Programa de Subvenção ao Prêmio do Seguro Rural) — cobre parte do custo do seguro agrícola, pecuário, florestal e aquícola pra quem contrata a cobertura certa.", 3, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "MAS O DADO PREOCUPA", "Em 2025, a área protegida <span class='hl'>caiu 56%</span> em 1 ano",
                    "Só 42 mil produtores foram beneficiados e cerca de 3,2 milhões de hectares protegidos em 2025 — bem abaixo da real exposição do agro brasileiro ao clima.", 4, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "NA PRÁTICA", "Sem laudo técnico da lavoura, <span class='hl'>não tem</span> seguro pra acionar",
                    "A contratação exige documentação da área plantada e do histórico de produtividade — quanto antes no ciclo da safra, melhor a condição de cobertura.", 5, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Seguro rural <span class='hl'>não é</span> genérico — é risco por risco, safra por safra",
                    "Manda pra quem trabalha com produção rural e nunca conferiu se a cobertura climática está mesmo na apólice.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_03_vale_a_pena_prestamista():
    out = os.path.join(CONTENT, "semana-10", "post-03-vale-a-pena-prestamista")
    total = 6
    slides = [
        notebook_slide(LOGO, "VALE A PENA?",
                        "Seguro Prestamista: o seguro<br>que quita sua dívida —<br><span class='hl'>vale a pena</span> mesmo?",
                        [], "3 direitos que pouca gente exerce 👇", 1, total),
        notebook_slide(LOGO, "O QUE ELE FAZ", "Em caso de morte, invalidez ou perda de renda",
                        [{"label": "Função do seguro", "value": "quitar ou amortizar a dívida", "highlight": True}],
                        "O prestamista assume o saldo devedor do financiamento, consórcio ou empréstimo — total ou parcialmente, conforme o contrato.", 2, total),
        notebook_slide(LOGO, "DIREITO 1", "Ninguém pode te obrigar a contratar",
                        [{"label": "Contratação do seguro", "value": "sempre facultativa", "highlight": True}],
                        "O banco não pode negar ou dificultar o crédito só porque você recusou o seguro — isso é venda casada, prática abusiva pelo CDC e já pacificada pelo STJ.", 3, total),
        notebook_slide(LOGO, "DIREITO 2", "A seguradora do banco não é a única opção",
                        [{"label": "Escolha da seguradora", "value": "é sua, não do banco", "highlight": True}],
                        "A Resolução CNSP nº 439/2022 regula o produto, mas nenhuma norma te obriga a contratar com a seguradora indicada pelo próprio banco — cotação externa costuma sair mais barata.", 4, total),
        notebook_slide(LOGO, "DIREITO 3", "Se você já caiu na venda casada",
                        [{"label": "Cláusula abusiva", "value": "nula"},
                         {"label": "Se comprovada em juízo", "value": "reembolso integral do prêmio", "highlight": True}],
                        "Jurisprudência do STJ garante devolução total do valor pago quando fica comprovado que a contratação foi condição pra liberar o crédito.", 5, total),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Sim — <span class='hl'>quando você escolhe</span>, não quando empurram",
                        [], "Guarda esse carrossel antes de fechar o próximo financiamento. Manda pra quem já contratou sem perguntar se podia recusar.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_04_caso_real_transporte_cargas():
    out = os.path.join(CONTENT, "semana-10", "post-04-caso-real-transporte-cargas")
    photo = p("ref-pexels-crash.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "CASO REAL",
                    "Caminhão tombou na estrada<br>com a carga toda — quem<br><span class='hl'>paga o prejuízo</span>?",
                    "Caso ilustrativo, baseado em situação real e comum no transporte rodoviário de cargas.", 1, total),
        photo_slide(LOGO, photo, "A REGRA DESDE 2023", "3 seguros <span class='hl'>obrigatórios</span> pra quem transporta carga",
                    "A Lei 14.599/2023 tornou obrigatórios RCTR-C, RC-DC e RC-V pra toda transportadora registrada no RNTRC — sem eles, a empresa fica irregular.", 2, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O QUE CADA UM COBRE", "RCTR-C cobre acidente; RC-DC cobre <span class='hl'>roubo e desaparecimento</span>",
                    "RCTR-C: colisão, tombamento, incêndio e explosão. RC-DC: roubo, furto, apropriação indébita ou extorsão da carga. RC-V: dano a terceiros causado pelo veículo.", 3, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "FISCALIZAÇÃO NOVA", "Desde 2026, a ANTT <span class='hl'>verifica isso direto no sistema</span>",
                    "A Resolução ANTT 6.068/2025 tornou a comprovação dos 3 seguros condição pra manter o registro (RNTRC) — fiscalização eletrônica automática, sem depender de blitz.", 4, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "QUEM FICA DE FORA DESSA REGRA", "Transportador autônomo <span class='hl'>subcontratado</span>, com RNTRC no CPF",
                    "A obrigatoriedade dos três seguros é da empresa transportadora (ETC) — o autônomo vinculado a ela por CPF não precisa contratar por conta própria.", 5, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Sem os 3 seguros em dia, a empresa <span class='hl'>perde o registro</span> pra transportar",
                    "Manda pro colega transportador ou embarcador que ainda não conferiu isso na própria operação.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_05_papo_corretor_cnsp493():
    out = os.path.join(CONTENT, "semana-10", "post-05-papo-corretor-cnsp-493")
    total = 6
    slides = [
        notebook_slide(LOGO, "PAPO DE CORRETOR",
                        "Virou <span class='hl'>dever formal</span> se atualizar<br>— pela 1ª vez na história do CNSP",
                        [], "Resolução nova, vigência em janeiro. Com fonte.", 1, total),
        notebook_slide(LOGO, "O QUE MUDOU", "Consolida 13 resoluções antigas num só ato",
                        [{"label": "Resolução", "value": "CNSP nº 493/2026", "highlight": True},
                         {"label": "Publicada em", "value": "21/07/2026"}],
                        "Reúne num único normativo regras que antes estavam espalhadas em 13 resoluções diferentes do CNSP sobre corretores de seguros.", 2, total),
        notebook_slide(LOGO, "O ARTIGO QUE IMPORTA", "Educação continuada vira dever, não sugestão",
                        [{"label": "Art. 15", "value": "atualização técnica obrigatória", "highlight": True}],
                        "O corretor passa a ter o dever formal de manter conhecimento técnico, regulatório e multidisciplinar atualizado — acompanhando legislação, mercado e tecnologia.", 3, total),
        notebook_slide(LOGO, "QUANDO ENTRA EM VIGOR", "180 dias depois da publicação",
                        [{"label": "Vigência", "value": "17/01/2027", "highlight": True}],
                        "Ainda dá tempo de se organizar — mas o relógio já está correndo.", 4, total),
        notebook_slide(LOGO, "SEM PUNIÇÃO PREVISTA — POR ENQUANTO", "Mercado já trata como diferencial competitivo",
                        [{"label": "Penalidade formal na norma", "value": "nenhuma ainda"}],
                        "A norma não prevê multa direta pra quem não cumprir — mas quem não se atualizar tende a perder espaço primeiro pro cliente, depois pra fiscalização.", 5, total),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Também incorpora mudanças da <span class='hl'>Lei 14.430/2022</span> e da LC 213/2025",
                        [], "Vale reler a resolução inteira antes de janeiro. Manda pro colega corretor que ainda não ouviu falar da 493.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_06_teste_domingo(post_01_dir):
    """Teste de domingo: repete o pilar consumidor mais universal da semana
    (Post 1 — seguro-incêndio na locação, se aplica a qualquer inquilino,
    muito mais universal que produtor rural ou empresa de transporte)."""
    out = os.path.join(CONTENT, "semana-10", "post-06-teste-domingo-seguro-incendio-locacao")
    os.makedirs(out, exist_ok=True)
    for i in range(1, 7):
        name = f"slide-{i:02d}.png"
        shutil.copyfile(os.path.join(post_01_dir, name), os.path.join(out, name))
    return out


if __name__ == "__main__":
    p1 = build_post_01_mito_inquilinato()
    build_post_02_mito_seguro_rural()
    build_post_03_vale_a_pena_prestamista()
    build_post_04_caso_real_transporte_cargas()
    build_post_05_papo_corretor_cnsp493()
    build_post_06_teste_domingo(p1)
    print("Lote 10 gerado.")
