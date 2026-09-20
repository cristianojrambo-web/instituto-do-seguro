"""Gera o Lote 9 — ramos da semana: Seguro Auto (buraco na via + responsabilidade do poder
público), Seguro de Vida em Grupo (portabilidade após demissão), Previdência Privada
(PGBL x VGBL, ramo novo no pilar "Vale a pena?"), Seguro Auto (agravamento de risco por mudança
de endereço não comunicada, ângulo distinto do Post 1) e Seguro Garantia — Lei 14.133/2021
(ramo inteiramente novo no canal, Papo de Corretor). Seguro saúde nunca entra (fora do escopo
real do usuário)."""

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


def build_post_01_mito_buraco_via():
    out = os.path.join(CONTENT, "semana-09", "post-01-mito-buraco-via")
    photo = p("ref-pexels-bmw-damaged.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Bateu num buraco e estourou<br>o pneu? Esse prejuízo é<br><span class='hl'>só seu</span> pra resolver?",
                    "Tem mais de um caminho possível — poucos motoristas conhecem os dois.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span> — dá pra acionar seu seguro",
                    "Com cobertura de colisão ou compreensiva, dano por buraco entra como sinistro comum, mesmo sem outro veículo envolvido — respeitando a franquia da apólice.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "TAMBÉM CABE PEDIR", "Reparação direto da <span class='hl'>prefeitura</span>",
                    "A manutenção das vias é dever do poder público — buraco mal sinalizado ou nunca reparado pode virar pedido de indenização contra o município.", 3, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "MAS ATENÇÃO", "Aqui a prova pesa <span class='hl'>mais</span> pro seu lado",
                    "A jurisprudência trata como omissão do Estado — responsabilidade subjetiva: você precisa comprovar a falha do serviço, não só mostrar o prejuízo.", 4, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "NA PRÁTICA", "Foto do buraco + B.O. +<br><span class='hl'>orçamento</span> do conserto",
                    "Documentar na hora ajuda tanto o pedido ao seguro quanto uma eventual ação contra o poder público depois.", 5, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Acionar o seguro <span class='hl'>não</span> tira seu direito de cobrar da prefeitura",
                    "São caminhos diferentes e podem andar juntos. Manda pra quem já rodou por cima de um buraco essa semana.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_02_mito_vida_portabilidade():
    out = os.path.join(CONTENT, "semana-09", "post-02-mito-vida-portabilidade")
    photo = p("ref-pexels-contract.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Ao ser demitido, o seguro de<br>vida em grupo da empresa<br><span class='hl'>acaba na hora</span> pra sempre?",
                    "Tem uma decisão que só depende de você — e tem prazo.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span> — dá pra levar a cobertura junto",
                    "É a portabilidade: transforma o seguro de vida em grupo num plano individual, sem depender mais do vínculo com a empresa.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O PRAZO", "Janela curta pra pedir —<br>em geral até <span class='hl'>30 dias</span> após o desligamento",
                    "Perdeu o prazo, perde o direito de portar sem burocracia extra — confirme o prazo exato direto com a seguradora da sua apólice.", 3, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "O QUE MUDA", "Na maioria dos casos,<br><span class='hl'>sem novo exame médico</span>",
                    "A ideia é manter a cobertura que você já tinha — mas o prêmio inteiro passa a sair do seu bolso, sem o rateio da empresa.", 4, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "FIQUE ESPERTO", "O valor da parcela<br>pode <span class='hl'>subir</span>",
                    "Sem o rateio coletivo, o prêmio individual tende a ficar mais alto — vale comparar com uma cotação de seguro de vida individual do zero.", 5, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Antes de sair da empresa,<br><span class='hl'>pergunta</span> pelo RH sobre a portabilidade",
                    "Ninguém avisa isso na hora do desligamento. Manda pra quem está de saída de um emprego agora.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_03_vale_a_pena_previdencia():
    out = os.path.join(CONTENT, "semana-09", "post-03-vale-a-pena-previdencia")
    total = 6
    slides = [
        notebook_slide(LOGO, "VALE A PENA?",
                        "Previdência privada: PGBL<br>ou VGBL — o que realmente<br><span class='hl'>vale a pena</span>?",
                        [], "3 fatores que decidem, não achismo 👇", 1, total),
        notebook_slide(LOGO, "FATOR 1 — SEU IMPOSTO DE RENDA", "Declara IR completo?",
                        [{"label": "PGBL deduz até", "value": "12% da renda bruta", "highlight": True}],
                        "Só quem faz declaração completa aproveita esse abatimento — na declaração simplificada, o PGBL perde a graça.", 2, total),
        notebook_slide(LOGO, "FATOR 2 — SE NÃO É O SEU CASO", "Declaração simplificada ou já usou os 12%?",
                        [{"label": "Melhor opção", "value": "VGBL", "highlight": True}],
                        "No VGBL, o Imposto de Renda incide só sobre o rendimento no resgate — não sobre o valor total que você aplicou.", 3, total),
        notebook_slide(LOGO, "FATOR 3 — O CUSTO QUE NINGUÉM MOSTRA", "Taxa de administração",
                        [{"label": "Aceitável", "value": "até 1% ao ano"},
                         {"label": "Corrói o rendimento no longo prazo", "value": "acima de 1,5% ao ano", "highlight": True}],
                        "Compare a taxa antes do nome bonito do plano — é o detalhe que mais pesa depois de 20-30 anos de contribuição.", 4, total),
        notebook_slide(LOGO, "ESTRATÉGIA COMUM", "Dá pra usar os <span class='hl'>dois</span> ao mesmo tempo",
                        [], "PGBL até o limite de 12% da renda tributável, e o excedente vai pro VGBL — não precisa escolher só um dos dois.", 5, total),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Sim — quando <span class='hl'>taxa baixa</span> encontra o tipo certo pro seu IR",
                        [], "Guarda esse carrossel antes de contratar qualquer plano. Manda pra quem já tem previdência e nunca conferiu a taxa.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_04_caso_real_endereco():
    out = os.path.join(CONTENT, "semana-09", "post-04-caso-real-endereco-nao-comunicado")
    photo = p("ref-pexels-navigation.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "CASO REAL",
                    "Motorista mudou de cidade,<br>manteve o endereço antigo<br>na apólice — carro foi <span class='hl'>roubado</span>",
                    "Caso ilustrativo, baseado em situação real e comum entre segurados.", 1, total),
        photo_slide(LOGO, photo, "O QUE A SEGURADORA ALEGOU", "Mudança de <span class='hl'>perfil de risco</span> não avisada",
                    "O endereço onde o carro fica guardado à noite influencia direto o cálculo do prêmio — é informação que precisa ser atualizada na apólice.", 2, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "A REGRA (art. 769 do CC)", "Agravar o risco sem avisar<br>pode custar a <span class='hl'>cobertura</span>",
                    "O Código Civil obriga o segurado a comunicar qualquer fato que aumente consideravelmente o risco assim que tomar conhecimento dele.", 3, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "MAS A JUSTIÇA FOI MAIS RESTRITA", "Só a divergência de endereço<br><span class='hl'>não bastou</span> pra negar",
                    "Sem má-fé comprovada e sem ligação direta entre a mudança e o sinistro, a jurisprudência do STJ não aceita negar a indenização só por isso.", 4, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O QUE PRECISA PRA NEGAR DE VERDADE", "Prova de <span class='hl'>má-fé</span> + nexo com o sinistro",
                    "A seguradora só pode recusar o pagamento se comprovar as duas coisas juntas — não basta apontar que o endereço estava desatualizado.", 5, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Mudou de cidade ou de bairro?<br><span class='hl'>Avisa</span> seu corretor",
                    "Evita discussão na Justiça e mantém o prêmio calculado no risco certo. Manda pra quem mudou de endereço e esqueceu de avisar o seguro.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_05_papo_corretor_garantia():
    out = os.path.join(CONTENT, "semana-09", "post-05-papo-corretor-seguro-garantia")
    total = 6
    slides = [
        notebook_slide(LOGO, "PAPO DE CORRETOR",
                        "O ramo que cresce <span class='hl'>13,6%</span><br>em 2026 e pouco corretor<br>ainda vende",
                        [], "Com fonte. Não é achismo.", 1, total),
        notebook_slide(LOGO, "O QUE É", "Substitui caução em dinheiro<br>e <span class='hl'>fiança bancária</span>",
                        [{"label": "Previsto na", "value": "Lei 14.133/2021, art. 96", "highlight": True}],
                        "Protege o contratante (público ou privado) contra inadimplência, abandono de obra ou descumprimento de contrato — sem travar o caixa da empresa segurada.", 2, total),
        notebook_slide(LOGO, "QUANTO PODE GARANTIR", "Percentual sobre o valor do contrato",
                        [{"label": "Regra geral", "value": "até 5%"},
                         {"label": "Alta complexidade/risco", "value": "até 10%", "highlight": True}],
                        "Em obras de grande vulto com cláusula de retomada, o percentual pode chegar a 30% do valor contratual.", 3, total),
        notebook_slide(LOGO, "QUEM PRECISA", "Toda empresa que <span class='hl'>disputa licitação</span> ou contrato de obra/serviço público",
                        [], "Também existe a versão judicial — substitui depósito em juízo, penhora e fiança em processo cível, trabalhista ou tributário. São produtos diferentes.", 4, total),
        notebook_slide(LOGO, "POR QUE VALE A PENA OFERECER", "Comissão recorrente + mercado <span class='hl'>em expansão</span>",
                        [{"label": "Crescimento projetado do ramo (CNseg, 2026)", "value": "13,6%", "highlight": True}],
                        "Construtoras, prestadoras de serviço público e empresas que disputam licitação costumam ser clientes que ainda não te procuraram por isso.", 5, total),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Antes da próxima licitação de um cliente, <span class='hl'>oferece</span> a cotação",
                        [], "Não espera o cliente perguntar — ele provavelmente nem sabe que esse seguro existe. Manda pro colega corretor que só trabalha ramos massificados.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_06_teste_domingo(post_01_dir):
    """Teste de domingo: repete o pilar consumidor mais universal da semana
    (Post 1 — buraco na via, se aplica a qualquer motorista, não só quem tem
    vida em grupo, previdência ou faz licitação)."""
    out = os.path.join(CONTENT, "semana-09", "post-06-teste-domingo-buraco-via")
    os.makedirs(out, exist_ok=True)
    for i in range(1, 7):
        name = f"slide-{i:02d}.png"
        shutil.copyfile(os.path.join(post_01_dir, name), os.path.join(out, name))
    return out


if __name__ == "__main__":
    p1 = build_post_01_mito_buraco_via()
    build_post_02_mito_vida_portabilidade()
    build_post_03_vale_a_pena_previdencia()
    build_post_04_caso_real_endereco()
    build_post_05_papo_corretor_garantia()
    build_post_06_teste_domingo(p1)
    print("Lote 9 gerado.")
