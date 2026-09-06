"""Gera o Lote 7 — ramos da semana: Seguro Auto (perda total/Tabela FIPE), golpe do
"corretor fantasma" (protecao ao consumidor + a propria marca), Seguro de Vida (grupo x
individual), Seguro Residencial (dano eletrico/queda de raio), Seguro de Frota para PME
(Papo de Corretor). Seguro saude nunca entra (fora do escopo real do usuario)."""

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


def build_post_01_mito_perda_total():
    out = os.path.join(CONTENT, "semana-07", "post-01-mito-perda-total-fipe")
    photo = p("ref-pexels-crash.jpg")
    total = 7
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Seu seguro sempre paga<br><span class='hl'>100% da Tabela FIPE</span><br>na perda total?",
                    "A resposta está no tipo de apólice que você assinou, não numa regra única.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Depende</span> do tipo de indenização contratado",
                    "Valor de Mercado Referenciado (VMR) paga pela Tabela FIPE do sinistro. Valor Determinado paga uma quantia fixa combinada na apólice — usado em carro raro ou sem boa cotação na FIPE.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O LIMITE DA SUSEP", "Perda total só com dano<br>de até <span class='hl'>75% do veículo</span>",
                    "A seguradora não pode exigir um percentual de dano maior que esse pra reconhecer perda total — é regra da SUSEP, não decisão da seguradora.", 3, total),
        photo_slide(LOGO, photo, "DÁ PRA CONTRATAR MAIS", "Cobertura de <span class='hl'>105% ou 110%</span><br>da FIPE existe",
                    "Comum em carro com acessórios ou equipamentos que a FIPE sozinha não cobre — depende do plano escolhido na contratação.", 4, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "A DATA QUE CONTA", "FIPE do <span class='hl'>dia do sinistro</span>,<br>não do pagamento",
                    "Entendimento consolidado do STJ: o carro se deprecia com o tempo, então o cálculo usa a tabela vigente na data do acidente ou furto.", 5, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O QUE É DESCONTADO", "IPVA, multas e<br><span class='hl'>alienação</span> saem do valor",
                    "Débitos em aberto do veículo e o saldo de financiamento (se houver) costumam ser descontados da indenização antes de cair na sua conta.", 6, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Confira o tipo de<br><span class='hl'>indenização</span> da sua apólice",
                    "VMR ou Valor Determinado? Saber isso agora evita surpresa na hora que você mais precisa do seguro.", 7, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_02_mito_corretor_fantasma():
    out = os.path.join(CONTENT, "semana-07", "post-02-mito-corretor-fantasma")
    photo = p("ref-pexels-contract.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Se seu corretor manda boleto<br>pelo WhatsApp, pagar é<br><span class='hl'>sempre seguro</span>?",
                    "Depende de uma checagem de 1 minuto que quase ninguém faz.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span> — o golpe do<br>\"corretor fantasma\" é real",
                    "Casos confirmados: perfis falsos usando foto de funcionário real de seguradora, e até invasão do sistema de uma corretora pra contatar clientes de verdade via WhatsApp.", 2, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "COMO ACONTECE", "Boleto de <span class='hl'>renovação falso</span><br>já fez vítimas em 5 estados",
                    "O golpista pede o pagamento via Pix ou boleto pra uma conta de pessoa física — o dinheiro some e o veículo ou a casa ficam sem cobertura nenhuma.", 3, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O ALERTA É OFICIAL", "Seguradoras confirmam:<br>nunca pedem dado por <span class='hl'>WhatsApp</span>",
                    "Porto Seguro e MAPFRE já emitiram alerta público — nenhuma delas solicita dado pessoal ou de corretora por mensagem.", 4, total),
        photo_slide(LOGO, photo, "COMO CONFERIR DE VERDADE", "Consulta de <span class='hl'>Corretores</span><br>no site da SUSEP",
                    "Busca gratuita por nome, CPF ou CNPJ em susep.gov.br — mostra se o corretor está ativo. Se não aparecer, não está autorizado a operar.", 5, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Nunca paga boleto pra<br>conta de <span class='hl'>pessoa física</span>",
                    "Na dúvida, liga direto pro 0800 oficial da seguradora antes de pagar qualquer coisa. Manda pra quem já recebeu boleto de seguro por WhatsApp.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_03_vale_a_pena_vida_grupo_individual():
    out = os.path.join(CONTENT, "semana-07", "post-03-vale-a-pena-vida-grupo-individual")
    total = 6
    slides = [
        notebook_slide(LOGO, "VALE A PENA?",
                        "O seguro de vida da<br>empresa já <span class='hl'>basta</span>?",
                        [], "Grupo e individual resolvem problemas diferentes — vale entender antes de contar só com um deles.", 1, total),
        notebook_slide(LOGO, "A DIFERENÇA BÁSICA", "Quem contrata muda<br>o que você <span class='hl'>controla</span>",
                        [{"label": "Seguro em grupo", "value": "empresa contrata"},
                         {"label": "Seguro individual", "value": "você contrata", "highlight": True}],
                        "Grupo costuma ser mais barato e com adesão mais simples. Individual dá mais controle sobre capital, prazo e beneficiários.", 2, total),
        notebook_slide(LOGO, "O RISCO DO GRUPO", "Saiu do emprego,<br>o seguro pode <span class='hl'>sair junto</span>",
                        [],
                        "A apólice em grupo normalmente se encerra com o desligamento. Algumas seguradoras oferecem migrar pra individual sem nova carência — mas isso é prática comercial de cada empresa, não uma garantia legal.", 3, total),
        notebook_slide(LOGO, "O QUE A LEI NOVA PROTEGE", "Mudar as regras do grupo<br>não é <span class='hl'>simples</span>",
                        [{"label": "Aprovação exigida p/ reduzir direito", "value": "75% do grupo", "highlight": True}],
                        "A Lei 15.040/2024 exige concordância de pelo menos três quartos dos segurados pra qualquer mudança que reduza direito no seguro coletivo, e proíbe cancelamento unilateral pela seguradora.", 4, total),
        notebook_slide(LOGO, "O SETOR ESTÁ CRESCENDO", "Seguro de vida puxa o<br>avanço dos seguros de <span class='hl'>pessoas</span>",
                        [{"label": "Seguro de vida (até set/2025)", "value": "+12%", "highlight": True},
                         {"label": "Seguros de pessoas em 2025", "value": "+8,3%"}],
                        "Dado da SUSEP e da Fenaprevi/CNseg — o crescimento recente vem puxado principalmente pelo seguro individual.", 5, total),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Os dois se <span class='hl'>completam</span>,<br>não competem",
                        [], "Quem depende do próprio salário fica mais protegido com os dois — o grupo cobre o dia a dia, o individual cobre o dia em que você não tiver mais o emprego. Guarda esse carrossel e revisa sua própria cobertura.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_04_caso_real_dano_eletrico():
    out = os.path.join(CONTENT, "semana-07", "post-04-caso-real-dano-eletrico")
    photo = p("ref-pexels-house.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "CASO REAL",
                    "Uma queda de energia queimou<br>a geladeira e a TV — e o seguro<br><span class='hl'>resolveu</span> em poucos dias",
                    "Caso ilustrativo, baseado em situação real e comum entre segurados.", 1, total),
        photo_slide(LOGO, photo, "NÃO É RARO", "Mais da metade dos sinistros<br>residenciais é <span class='hl'>dano elétrico</span>",
                    "Levantamento de uma seguradora (2023-2026) mostra dano elétrico como a causa nº1 de acionamento — à frente de dano por água e vento/granizo.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O QUE A SEGURADORA PEDIU", "Nota fiscal dos aparelhos<br>+ <span class='hl'>laudo técnico</span>",
                    "Um laudo de eletricista com ART (registro no CREA) comprovando que a causa foi elétrica — sem isso, o pedido costuma ser recusado.", 3, total),
        photo_slide(LOGO, photo, "O DETALHE DA APÓLICE", "Dano elétrico costuma ser<br>cobertura <span class='hl'>adicional</span>",
                    "Já a queda de raio direta costuma vir na cobertura básica (incêndio/explosão/raio) — mas isso varia de seguradora pra seguradora, vale conferir a sua.", 4, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O ALÍVIO", "Com laudo e nota fiscal,<br>o processo <span class='hl'>andou rápido</span>",
                    "O Brasil é o país com mais raios do mundo (dado INPE/NASA) — é exatamente pra esse tipo de imprevisto que o seguro existe.", 5, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Confira se sua apólice tem<br>dano elétrico <span class='hl'>à parte</span>",
                    "Guarda a nota fiscal dos eletrônicos de casa e considera instalar um DPS (protetor contra surto) no quadro de energia. Manda pra quem já perdeu aparelho numa queda de luz.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_05_papo_corretor_frota():
    out = os.path.join(CONTENT, "semana-07", "post-05-papo-corretor-frota")
    total = 6
    slides = [
        notebook_slide(LOGO, "PAPO DE CORRETOR",
                        "O cliente PJ com 3 carros<br>separados pode estar pagando<br><span class='hl'>mais caro</span> do que precisa",
                        [], "Com fonte. Não é achismo.", 1, total),
        notebook_slide(LOGO, "DADO", "A maior parte da frota<br>nacional roda <span class='hl'>sem seguro</span>",
                        [{"label": "Frota nacional segurada (dez/2025)", "value": "~30%", "highlight": True}],
                        "FenSeg/Senatran: 7 em cada 10 veículos em circulação no Brasil não têm apólice — inclusive frota de empresa.", 2, total),
        notebook_slide(LOGO, "E NO PJ NÃO É DIFERENTE", "A maioria só busca seguro<br><span class='hl'>depois</span> do sinistro",
                        [{"label": "Pequenos empresários com algum seguro no negócio", "value": "26,7%", "highlight": True}],
                        "Dado CNseg/SindsegSP — a maior parte das PMEs só procura cobertura depois de um roubo, incêndio ou por exigência de contrato.", 3, total),
        notebook_slide(LOGO, "O QUE MUDA NUMA APÓLICE DE FROTA", "Gestão única e<br><span class='hl'>desconto de volume</span>",
                        [{"label": "Desconto vs. apólices individuais", "value": "15-25%", "highlight": True},
                         {"label": "RCF-V", "value": "com limite ampliado"}],
                        "Uma apólice, um vencimento, gestão centralizada de sinistro — e seguradoras já usam telemetria pra baratear ainda mais quem tem rastreamento ativo.", 4, total),
        notebook_slide(LOGO, "O RISCO DE NÃO TER", "Roubo de carga custou<br>mais de <span class='hl'>R$1,2 bi</span> em 2024",
                        [{"label": "Roubos de carga registrados (2024)", "value": "10.478"},
                         {"label": "Média por dia", "value": "27 ocorrências", "highlight": True}],
                        "Direto ligado a quem depende de veículo pra entregar ou prestar serviço — o tipo de cliente PJ que todo corretor já atende.", 5, total),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Pergunta antes da<br>próxima <span class='hl'>renovação PJ</span>",
                        [], "Cliente com 3 ou mais veículos na empresa: já tem apólice de frota, ou paga separado sem saber que existe desconto? Manda pro colega corretor que só vende seguro auto individual.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_06_teste_domingo(post_02_dir):
    """Teste de domingo: repete o pilar consumidor mais universal da semana
    (Post 2 -- golpe do corretor fantasma, que se aplica a qualquer segurado de
    qualquer ramo, mais universal que perda total de carro), em pasta propria."""
    out = os.path.join(CONTENT, "semana-07", "post-06-teste-domingo-corretor-fantasma")
    os.makedirs(out, exist_ok=True)
    for i in range(1, 7):
        name = f"slide-{i:02d}.png"
        shutil.copyfile(os.path.join(post_02_dir, name), os.path.join(out, name))
    return out


if __name__ == "__main__":
    build_post_01_mito_perda_total()
    p2 = build_post_02_mito_corretor_fantasma()
    build_post_03_vale_a_pena_vida_grupo_individual()
    build_post_04_caso_real_dano_eletrico()
    build_post_05_papo_corretor_frota()
    build_post_06_teste_domingo(p2)
    print("Lote 7 gerado.")
