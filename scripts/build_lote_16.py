"""Gera o Lote 16 — Mito: bonus do seguro auto; Mito: seguro viagem cancelamento; Vale a pena: garantia estendida;
Caso pratico: arvore/granizo x compreensiva; Papo de Corretor: reforma tributaria IBS/CBS. Seguro saude nunca entra."""


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
SEM = "semana-16"


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
    photo = p("ref-pexels-rideapp.jpg")
    t = 6
    return build("post-01-mito-bonus-seguro-auto", [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "O <span class='hl'>bônus</span> do seguro vai<br>junto com o carro?",
                    "Vendeu o carro? Veja o que acontece com o seu desconto.", 1, t),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span> — o bônus é do segurado",
                    "Em regra, o bônus fica atrelado a quem contratou (CPF ou CNPJ), não ao veículo. Pode ser levado para o próximo carro.", 2, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "TRANSFERÊNCIA", "Para outra pessoa é <span class='hl'>exceção</span>",
                    "Manuais de seguradoras citam casos específicos, como falecimento do titular, com vínculo como cônjuge, pais ou filhos. As regras variam.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "TROCA DE SEGURADORA", "Leve o <span class='hl'>código do bônus</span>",
                    "Ao renovar em outra seguradora, o código de identificação do bônus precisa ir na proposta. Ele fica impresso na apólice.", 4, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "ATENÇÃO", "As regras <span class='hl'>já mudaram antes</span>",
                    "Em 2024 a Susep suspendeu mudanças nos critérios de bônus que valeriam em agosto. Peça a política vigente à sua seguradora.", 5, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Você sabe qual é o seu <span class='hl'>código de bônus</span>?",
                    "Manda pra quem vai trocar de carro ou de seguradora.", 6, t),
    ])


def post_02():
    photo = p("ref-pexels-travel.jpg")
    t = 6
    return build("post-02-mito-seguro-viagem-cancelamento", [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Seguro viagem devolve o dinheiro se você<br><span class='hl'>desistir de viajar</span>?",
                    "Depende do motivo. E nem todo plano tem essa cobertura.", 1, t),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span> — só motivos previstos",
                    "A cobertura de cancelamento depende da lista de motivos da apólice, como doença grave, acidente ou morte de familiar próximo.", 2, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "MUDOU DE IDEIA?", "Motivo pessoal <span class='hl'>não costuma entrar</span>",
                    "Desistir sem um motivo previsto na apólice geralmente não é coberto, segundo corretoras e condições gerais consultadas.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "EXCLUSÕES COMUNS", "Pandemia e <span class='hl'>desastres naturais</span>",
                    "Eventos decorrentes de pandemia reconhecida por autoridade e desastres naturais costumam aparecer como exclusões. Confira a sua.", 4, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "DOENÇA PREEXISTENTE", "Declare na <span class='hl'>contratação</span>",
                    "A definição varia por seguradora. Doença conhecida e não declarada na proposta pode virar problema na hora do sinistro.", 5, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Qual motivo de cancelamento seu seguro <span class='hl'>realmente cobre</span>?",
                    "Manda pra quem tem viagem marcada.", 6, t),
    ])


def post_03():
    t = 6
    return build("post-03-vale-a-pena-garantia-estendida", [
        notebook_slide(LOGO, "VALE A PENA?",
                       "Garantia estendida:<br><span class='hl'>vale a pena</span>?",
                       [], "Antes de pagar no caixa, veja isso 👇", 1, t),
        notebook_slide(LOGO, "GARANTIA LEGAL", "O CDC já dá <span class='hl'>90 dias</span> (duráveis)",
                       [{"label": "Produto durável", "value": "90 dias", "highlight": True},
                        {"label": "Não durável", "value": "30 dias"}],
                       "Defeito oculto: o prazo conta de quando o problema aparece.", 2, t),
        notebook_slide(LOGO, "GARANTIA DO FABRICANTE", "Costuma somar <span class='hl'>cerca de 1 ano</span>",
                       [{"label": "Contratual", "value": "~12 meses", "highlight": True},
                        {"label": "Soma com a legal", "value": "1 ano + 90 dias"}],
                       "O prazo varia por fabricante e produto.", 3, t),
        notebook_slide(LOGO, "A ESTENDIDA", "Cobre o período <span class='hl'>depois dessas duas</span>",
                       [{"label": "Pode incluir", "value": "roubo, furto, dano acidental", "highlight": True},
                        {"label": "Depende", "value": "do contrato"}],
                       "Leia o que está dentro e fora da cobertura.", 4, t),
        notebook_slide(LOGO, "O QUE DIZEM", "Idec: em geral, <span class='hl'>não compensa</span>",
                       [{"label": "Pode compensar", "value": "uso diário, preço alto", "highlight": True},
                        {"label": "Arrependimento", "value": "7 dias"}],
                       "Veja também se o cartão já oferece proteção na compra.", 5, t),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Só se cobrir <span class='hl'>o que as outras não cobrem</span>",
                       [], "Compare preço e cobertura. Salva pra consultar antes da próxima compra.", 6, t),
    ])


def post_04():
    photo = p("ref-pexels-rain.jpg")
    t = 6
    return build("post-04-caso-pratico-arvore-granizo-compreensiva", [
        photo_slide(LOGO, photo, "CASO PRÁTICO",
                    "Árvore caiu no carro e o seguro<br><span class='hl'>não pagou</span>. Por quê?",
                    "Caso ilustrativo, baseado em dúvida comum. Não é caso real identificável.", 1, t),
        photo_slide(LOGO, photo, "A SITUAÇÃO", "Temporal à noite, <span class='hl'>carro amassado</span>",
                    "Imagine um motorista que acordou com um galho grande sobre o capô e acionou o seguro.", 2, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O PROBLEMA", "Ele tinha só cobertura de <span class='hl'>terceiros</span>",
                    "A RCF-V cobre danos causados a terceiros. Os danos ao próprio veículo por árvore, granizo ou enchente exigem a cobertura compreensiva.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "SE FOSSE COMPREENSIVA", "Árvore, granizo e <span class='hl'>alagamento</span> costumam entrar",
                    "Guias de corretoras citam queda de objetos, granizo e enchente na compreensiva. Confira as cláusulas da sua apólice.", 4, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "ALAGAMENTO", "Água no painel pode virar <span class='hl'>perda total</span>",
                    "Fontes do setor indicam que, se a água passa do painel ou atinge o motor, o carro costuma ser tratado como perda total. Cada caso é analisado.", 5, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Sua apólice é <span class='hl'>compreensiva</span>?",
                    "Manda pra quem mora em região de temporal.", 6, t),
    ])


def post_05():
    t = 6
    return build("post-05-papo-corretor-reforma-tributaria-ibs-cbs", [
        notebook_slide(LOGO, "PAPO DE CORRETOR",
                       "Reforma tributária: o que muda<br>pra <span class='hl'>seguros e corretoras</span>",
                       [], "Cliente já pergunta. Vale chegar preparado. 👇", 1, t),
        notebook_slide(LOGO, "ENQUADRAMENTO", "Seguros entram em regime de <span class='hl'>serviços financeiros</span>",
                       [{"label": "LC 214/2025", "value": "IBS e CBS", "highlight": True},
                        {"label": "Também", "value": "resseguro, previdência, capitalização"}],
                       "Lei alterada depois pela LC 227/2026, segundo a Revista Apólice.", 2, t),
        notebook_slide(LOGO, "ALÍQUOTA", "Soma IBS+CBS parte de <span class='hl'>10,85%</span>",
                       [{"label": "Em 2033", "value": "12,50%", "highlight": True},
                        {"label": "Fonte", "value": "EY, art. 233"}],
                       "Regime específico: não segue a alíquota geral.", 3, t),
        notebook_slide(LOGO, "CORRETORAS", "Alíquota da corretora ainda gera <span class='hl'>debate</span>",
                       [{"label": "Corrente", "value": "vinculada à alíquota-base", "highlight": True},
                        {"label": "Status", "value": "interpretação, não consolidada"}],
                       "Confirme com seu contador antes de precificar.", 4, t),
        notebook_slide(LOGO, "SIMPLES E IOF", "Simples mantém regras; <span class='hl'>IOF sai em 2027</span>",
                       [{"label": "Simples Nacional", "value": "mantém regime, salvo opção", "highlight": True},
                        {"label": "IOF seguros", "value": "fim a partir de 2027"}],
                       "Fontes de 2025/2026 divergem em detalhes. Confira o texto vigente.", 5, t),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Quem se prepara antes <span class='hl'>vende com segurança</span>",
                       [], "Confirme normas atualizadas antes de orientar. Manda pro colega corretor.", 6, t),
    ])


def post_06(src):
    out = os.path.join(CONTENT, SEM, "post-06-teste-domingo-bonus-seguro-auto")
    os.makedirs(out, exist_ok=True)
    for i in range(1, 7):
        shutil.copyfile(os.path.join(src, f"slide-{i:02d}.png"), os.path.join(out, f"slide-{i:02d}.png"))


if __name__ == "__main__":
    s1 = post_01()
    post_02(); post_03(); post_04(); post_05()
    post_06(s1)
    print("Lote 16 gerado.")
