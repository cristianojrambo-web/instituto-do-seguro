"""Gera o Lote 6 — ramos da semana: Seguro de Vida (atividade de risco/esporte radical),
Seguro de Moto (capacete e acessórios), Seguro Viagem (vale a pena?), Seguro Residencial
(imóvel fechado por longo período), Seguro Cyber/D&O empresarial (Papo de Corretor).
Seguro saúde nunca entra (fora do escopo real do usuário)."""

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


def build_post_01_mito_vida_esporte_radical():
    out = os.path.join(CONTENT, "semana-06", "post-01-mito-vida-esporte-radical")
    total = 6
    slides = [
        notebook_slide(LOGO, "MITO OU VERDADE",
                        "Seguro de vida não paga se<br>você morre praticando<br><span class='hl'>esporte radical</span>?",
                        [], "Trilha, mergulho, paraquedismo, moto trilha — a lei mudou o que a seguradora pode fazer com isso.", 1, total),
        notebook_slide(LOGO, "A RESPOSTA", "<span class='hl'>Mito</span>, na maioria dos casos —<br>mudou com a lei nova",
                        [], "Antes, era comum a apólice excluir de vez a cobertura por esporte radical, atividade militar ou profissão de risco. A Lei 15.040/2024 proibiu essa exclusão automática.", 2, total),
        notebook_slide(LOGO, "O QUE MUDOU", "Seguro de <span class='hl'>pessoas</span> não pode<br>mais negar só por isso",
                        [{"label": "Seguro de danos", "value": "pode negar cobertura"},
                         {"label": "Seguro de pessoas (vida)", "value": "não pode negar", "highlight": True}],
                        "Em seguro de vida, mesmo com agravamento de risco comprovado, a seguradora só pode reajustar o prêmio — nunca recusar a indenização por esse motivo isolado.", 3, total),
        notebook_slide(LOGO, "MAS ATENÇÃO", "Existe uma <span class='hl'>exceção real</span>",
                        [], "Se você omitiu a prática de propósito na Declaração Pessoal de Saúde (DPS), ou agiu de forma extremamente imprudente (ex: sem nenhum equipamento de segurança), isso pode ser tratado como agravamento intencional — aí a discussão muda de figura.", 4, total),
        notebook_slide(LOGO, "O PRAZO DA SEGURADORA", "<span class='hl'>20 dias</span> pra cobrar a<br>diferença de prêmio",
                        [{"label": "Prazo pra reajustar prêmio", "value": "20 dias", "highlight": True},
                         {"label": "Contrato perde validade em", "value": "+30 dias"}],
                        "Se a seguradora ficar sabendo da atividade de risco depois da contratação, a Lei 15.040/2024 dá esse prazo pra ela agir — sem isso, o contrato segue valendo do jeito que estava.", 5, total),
        notebook_slide(LOGO, "GUARDA ISSO", "Declare a atividade —<br>é o que te <span class='hl'>protege</span> de verdade",
                        [], "Praticar esporte radical não te tira do seguro de vida. Esconder isso na contratação é que pode. Manda pra quem pratica algo assim e nunca avisou o corretor.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_02_mito_moto_acessorios():
    out = os.path.join(CONTENT, "semana-06", "post-02-mito-moto-acessorios")
    photo = p("ref-pexels-doorlock.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Seu seguro de moto NÃO<br>cobre capacete e <span class='hl'>acessórios</span><br>roubados junto?",
                    "Depende de uma coisa que quase ninguém confere na hora de contratar.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Depende</span> — não vem de graça<br>no plano básico",
                    "Cobertura de acessórios (capacete, jaqueta, luvas, baú) costuma ser adicional, contratada à parte — nem toda apólice de moto já inclui.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O QUE COSTUMA ENTRAR", "Capacete, jaqueta,<br><span class='hl'>luvas e baú</span>",
                    "Quando contratada, essa cobertura costuma pagar reparo ou reposição desses itens dentro de um limite definido na apólice — não é valor livre.", 3, total),
        photo_slide(LOGO, photo, "SE A MOTO VOLTAR", "Recuperada, mas<br><span class='hl'>sem</span> os acessórios?",
                    "Se a moto for recuperada com peças ou acessórios levados, a seguradora cobre o reparo até o limite contratado — mas só se essa cobertura específica existir na apólice.", 4, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "ANTES DE CONTRATAR", "Pede a <span class='hl'>lista</span> exata<br>do que está incluso",
                    "Plano mais barato costuma trazer só roubo/furto da moto em si. Confirma com o corretor se capacete e acessório entram, e qual o limite de cada item.", 5, total),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Não assuma que<br>\"tudo que tava na moto\"<br>está <span class='hl'>coberto</span>",
                    "Manda pra quem anda de moto e nunca conferiu isso na própria apólice.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_03_vale_a_pena_viagem():
    out = os.path.join(CONTENT, "semana-06", "post-03-vale-a-pena-viagem")
    photo = p("ref-pexels-travel.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "VALE A PENA?",
                    "Seguro viagem vale a pena<br>— mesmo perto de <span class='hl'>casa</span>?",
                    "Nacional ou internacional, o cálculo muda menos do que parece.", 1, total),
        notebook_slide(LOGO, "QUANTO CUSTA", "Menos do que a maioria<br><span class='hl'>imagina</span>",
                        [{"label": "Viagem nacional", "value": "R$8-20/dia"},
                         {"label": "Viagem internacional", "value": "R$15-60/dia", "highlight": True}],
                        "Faixa de preço 2026 pros planos mais comuns — varia com destino, idade e cobertura escolhida.", 2, total),
        notebook_slide(LOGO, "POR QUE VALE A PENA", "Seu plano de saúde<br><span class='hl'>não sai</span> do Brasil",
                        [{"label": "Consulta de emergência (Miami)", "value": "~US$3.500"},
                         {"label": "Diária de UTI nos EUA", "value": "+US$10.000", "highlight": True}],
                        "Nenhum plano de saúde brasileiro cobre atendimento fora do país — o seguro viagem é o que resolve isso.", 3, total),
        notebook_slide(LOGO, "QUANDO É OBRIGATÓRIO", "Zona <span class='hl'>Schengen</span> (Europa)<br>exige por lei",
                        [{"label": "Cobertura mínima exigida", "value": "€30 mil", "highlight": True}],
                        "Pra entrar na maioria dos países europeus, o seguro com essa cobertura mínima não é opcional — é documento de entrada.", 4, total),
        notebook_slide(LOGO, "O QUE COSTUMA COBRIR", "Além da <span class='hl'>emergência médica</span>",
                        [{"label": "Atendimento médico/odontológico", "value": "cobre"},
                         {"label": "Bagagem extraviada", "value": "cobre"},
                         {"label": "Cancelamento de viagem", "value": "depende do plano"}],
                        "A cobertura exata varia por plano — vale conferir item a item antes de embarcar, mesmo em viagem curta.", 5, total),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Sim — inclusive na<br>viagem <span class='hl'>mais simples</span>",
                        [], "Guarda esse carrossel antes de fechar a próxima passagem, nacional ou internacional.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_04_caso_real_imovel_fechado():
    out = os.path.join(CONTENT, "semana-06", "post-04-caso-real-imovel-fechado")
    photo = p("ref-pexels-house.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "ATENÇÃO",
                    "Deixar a casa fechada por<br>muito tempo pode zerar sua<br><span class='hl'>indenização</span>?",
                    "Caso ilustrativo, baseado em situação real e comum entre segurados.", 1, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O QUE A APÓLICE PEDE", "Avisar quando o imóvel<br>fica <span class='hl'>desocupado</span>",
                    "A maioria das apólices exige comunicar a seguradora quando a casa fica fechada por mais de 30 ou 60 dias seguidos — o prazo exato varia por seguradora.", 2, total),
        photo_slide(LOGO, photo, "MAS TEM UM DETALHE", "A prova é <span class='hl'>da seguradora</span>,<br>não sua",
                    "O STJ decidiu, em 2024, que é a seguradora quem tem o dever de provar que a desocupação teve relação direta com o sinistro — negar de forma automática não vale.", 3, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O QUE A LEI NOVA REFORÇA", "Precisa de <span class='hl'>nexo causal</span><br>comprovado",
                    "Pela Lei 15.040/2024, a perda do direito só é válida se o agravamento de risco for relevante E tiver ligação direta e provada com o que causou o sinistro.", 4, total),
        photo_slide(LOGO, photo, "O RISCO REAL", "Casa de <span class='hl'>praia</span>, herança,<br>viagem longa",
                    "Imóvel de veraneio, casa herdada parada, mudança que demora — são as situações mais comuns em que ninguém pensa em avisar a seguradora.", 5, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Avisa <span class='hl'>antes</span> de fechar<br>a casa por muito tempo",
                    "Uma ligação pro corretor evita meses de discussão depois. Manda pra quem tem casa de praia ou imóvel parado.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_05_papo_corretor_cyber():
    out = os.path.join(CONTENT, "semana-06", "post-05-papo-corretor-cyber")
    total = 6
    slides = [
        notebook_slide(LOGO, "PAPO DE CORRETOR",
                        "O ramo que mais cresce e<br>quase nenhum corretor está<br><span class='hl'>oferecendo</span>",
                        [], "Com fonte. Não é achismo.", 1, total),
        notebook_slide(LOGO, "DADO", "Indenizações de seguro<br><span class='hl'>cibernético</span> dispararam",
                        [{"label": "Indenizações (jan-abr/26 x ano ant.)", "value": "+253,1%", "highlight": True},
                         {"label": "Prêmios arrecadados (mesmo período)", "value": "R$134,6 mi"}],
                        "Dado do setor — o risco parou de ser hipotético e virou sinistro pagável, todo mês.", 2, total),
        notebook_slide(LOGO, "AINDA MAIS", "A arrecadação <span class='hl'>já vinha</span><br>subindo forte",
                        [{"label": "Arrecadação até fev/2026", "value": "+185%", "highlight": True}],
                        "Salto na comparação anual — mercado em curva de crescimento rápido, com pouco corretor especializado nele ainda.", 3, total),
        notebook_slide(LOGO, "O QUE É", "Protege a empresa de<br><span class='hl'>ataque</span> e vazamento",
                        [], "Ransomware, invasão de sistema, vazamento de dados com exigência da LGPD — cobertura pensada pra empresa que depende de sistema pra funcionar (ou seja, quase toda empresa hoje).", 4, total),
        notebook_slide(LOGO, "SINAL DE MERCADO", "O setor já monitora<br><span class='hl'>o risco de perto</span>",
                        [{"label": "Alertas de incidente compartilhados em 2025", "value": "527"},
                         {"label": "Só no 1º trimestre de 2026", "value": "123", "highlight": True}],
                        "A CNseg criou uma plataforma pras seguradoras trocarem informação sobre ataques — sinal de que o setor trata isso como risco real, não moda.", 5, total),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Pergunta antes da<br>próxima <span class='hl'>renovação PJ</span>",
                        [], "Cliente com CNPJ que depende de sistema, site ou dado de cliente já tem isso, ou nunca ninguém ofereceu? Manda pro colega corretor que só vende seguro empresarial tradicional.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_06_teste_domingo(post_04_dir):
    """Teste de domingo: repete o pilar consumidor mais universal da semana
    (Post 4 — caso real seguro residencial x imóvel fechado, praticamente todo mundo
    tem casa/apartamento que pode ficar vazio em algum momento), em pasta própria."""
    out = os.path.join(CONTENT, "semana-06", "post-06-teste-domingo-imovel-fechado")
    os.makedirs(out, exist_ok=True)
    for i in range(1, 7):
        name = f"slide-{i:02d}.png"
        shutil.copyfile(os.path.join(post_04_dir, name), os.path.join(out, name))
    return out


if __name__ == "__main__":
    build_post_01_mito_vida_esporte_radical()
    build_post_02_mito_moto_acessorios()
    build_post_03_vale_a_pena_viagem()
    p4 = build_post_04_caso_real_imovel_fechado()
    build_post_05_papo_corretor_cyber()
    build_post_06_teste_domingo(p4)
    print("Lote 6 gerado.")
