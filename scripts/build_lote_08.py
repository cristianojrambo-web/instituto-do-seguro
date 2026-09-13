"""Gera o Lote 8 — ramos da semana: Seguro Auto (furto/roubo em estacionamento),
Seguro Residencial (vendaval/queda de árvore), Seguro de Moto (vale a pena, ramo novo),
Seguro Empresarial (agravamento de risco por mudança de uso do imóvel/atividade) e
Marco Legal dos Seguros (Lei 15.040/2024) aplicado ao dia a dia do corretor (Papo de
Corretor). Seguro saúde nunca entra (fora do escopo real do usuário)."""

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


def build_post_01_mito_estacionamento():
    out = os.path.join(CONTENT, "semana-08", "post-01-mito-estacionamento")
    photo = p("ref-pexels-flood.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Carro roubado num estacionamento<br>pago: você precisa <span class='hl'>processar</span><br>o estabelecimento pra ser pago?",
                    "A resposta é mais simples — e mais rápida — do que parece.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span> — quem tem seguro não precisa disso",
                    "Com seguro auto, você aciona sua própria seguradora pelo roubo normalmente — não precisa esperar resolver nada com o estacionamento antes.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "A REGRA DO ESTACIONAMENTO", "Súmula 130 do STJ:<br>o estabelecimento <span class='hl'>responde</span>",
                    "Estacionamentos pagos — e também os gratuitos de shopping e mercado — têm o dever de indenizar o cliente por furto ou roubo ocorrido no local.", 3, total),
        photo_slide(LOGO, photo, "QUEM COBRA DE QUEM", "A seguradora vira<br><span class='hl'>sub-rogada</span> e cobra por você",
                    "Depois de te pagar, ela assume seu direito de cobrar o estacionamento e entra com a ação de regresso — brigar na Justiça deixa de ser problema seu.", 4, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "MAS ATENÇÃO", "Roubo à mão armada em área<br><span class='hl'>aberta e gratuita</span> pode mudar isso",
                    "Em estacionamento externo, gratuito e de livre acesso, a Justiça já reconheceu caso fortuito externo em alguns julgados — é analisado caso a caso.", 5, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Boletim de ocorrência<br>+ contato com seu <span class='hl'>corretor</span>",
                    "Você não precisa esperar resolver com o estabelecimento pra acionar seu seguro. Manda pra quem estaciona em shopping ou mercado todo dia.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_02_mito_residencial_vendaval():
    out = os.path.join(CONTENT, "semana-08", "post-02-mito-residencial-vendaval")
    photo = p("ref-pexels-house.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Se uma árvore cai na sua casa<br>num temporal, o seguro <span class='hl'>residencial</span><br>cobre o prejuízo?",
                    "Depende de duas coisas que quase ninguém confere na apólice.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Verdade</span> — mas só com a cobertura certa",
                    "É a cobertura de Vendaval, Furacão, Ciclone, Tornado e Granizo — opcional em várias apólices, não vem sempre no plano básico.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O CRITÉRIO TÉCNICO", "Só conta pra ventos<br>acima de <span class='hl'>54 km/h</span>",
                    "A seguradora exige um fenômeno natural de força comprovada — capaz de derrubar até uma árvore saudável, não só uma galhada fraca.", 3, total),
        photo_slide(LOGO, photo, "O DETALHE QUE PODE NEGAR TUDO", "Árvore <span class='hl'>doente ou mal cuidada</span><br>muda a história",
                    "Se já tinha sinal de apodrecimento, inclinação ou raiz comprometida, o caso deixa de ser 'fortuito' e vira responsabilidade de quem devia podar.", 4, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "E SE FOR A ÁRVORE DO VIZINHO?", "Seu seguro paga primeiro,<br>a discussão fica <span class='hl'>depois</span>",
                    "Sua própria apólice cobre o dano na sua casa — de quem é a culpa pela falta de poda se resolve depois, entre seguradora e responsável.", 5, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Chuva que entra pela goteira<br><span class='hl'>não</span> é a mesma cobertura",
                    "Vendaval cobre o vento direto — água de chuva entrando por conta própria é outra cobertura. Confere as duas na sua apólice.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_03_vale_a_pena_moto():
    out = os.path.join(CONTENT, "semana-08", "post-03-vale-a-pena-moto")
    total = 6
    slides = [
        notebook_slide(LOGO, "VALE A PENA?",
                        "Seguro de moto: vale o<br>preço ou é <span class='hl'>dinheiro jogado fora</span>?",
                        [], "Números que ajudam a decidir, não achismo 👇", 1, total),
        notebook_slide(LOGO, "O RISCO REAL", "Moto é o veículo mais visado<br>pra <span class='hl'>roubo</span> no Brasil",
                        [{"label": "Motos roubadas/furtadas em SP (1º tri/2024)", "value": "6.700+", "highlight": True}],
                        "Alta concentrada em capitais e regiões metropolitanas — moto é rápida de revender e difícil de rastrear.", 2, total),
        notebook_slide(LOGO, "DADO", "Recuperação depois do roubo<br>é bem mais <span class='hl'>rara</span>",
                        [{"label": "Motos roubadas não recuperadas", "value": "38%", "highlight": True},
                         {"label": "Carros roubados não recuperados", "value": "12%"}],
                        "Moto some 3x mais que carro depois de roubada — o item que você mais usa no dia a dia é também o mais fácil de perder de vez.", 3, total),
        notebook_slide(LOGO, "QUANTO CUSTA", "Preço varia com perfil,<br>não só com <span class='hl'>modelo</span>",
                        [{"label": "Seguro popular (só roubo/furto)", "value": "a partir de R$1.200/ano"},
                         {"label": "Seguro completo", "value": "R$1.500-3.000/ano", "highlight": True}],
                        "Idade do condutor, região e uso (entrega/aplicativo) pesam tanto quanto a moto em si no cálculo do prêmio.", 4, total),
        notebook_slide(LOGO, "QUANDO PESA MAIS PRA VALER A PENA", "Depende da moto pra<br>trabalhar ou mora em <span class='hl'>região de risco</span>?",
                        [], "Pra quem depende da moto pra trabalhar (entrega, aplicativo), o prejuízo de ficar sem ela costuma pesar mais que qualquer parcela.", 5, total),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Sim — principalmente pra quem<br>não teria como <span class='hl'>repor</span> a moto do bolso",
                        [], "Guarda esse carrossel e compara com um corretor antes de decidir. Manda pra quem anda de moto todo dia e nunca cotou um seguro.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_04_caso_real_agravamento_risco():
    out = os.path.join(CONTENT, "semana-08", "post-04-caso-real-agravamento-risco")
    photo = p("ref-pexels-contract.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "CASO REAL",
                    "Empresa trocou o estoque do galpão<br>por material mais <span class='hl'>inflamável</span> —<br>e avisou a seguradora antes",
                    "Caso ilustrativo, baseado em situação real e comum entre empresas seguradas.", 1, total),
        photo_slide(LOGO, photo, "A REGRA", "Mudança de risco tem<br>que ser <span class='hl'>comunicada</span>",
                    "O Código Civil (art. 769) obriga o segurado a avisar a seguradora assim que souber de qualquer fato que agrave o risco de forma considerável.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O QUE A SEGURADORA PODE FAZER", "Cobrar diferença de <span class='hl'>prêmio</span><br>ou encerrar o contrato",
                    "Recebendo o aviso a tempo, ela tem até 30 dias pra decidir — ajusta o valor pelo novo risco ou resolve o contrato, nunca pode só ficar calada.", 3, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "O QUE ELA NÃO PODE FAZER", "Ficar calada, receber o prêmio<br>e negar só na hora do <span class='hl'>sinistro</span>",
                    "Se a seguradora sabia da mudança e continuou cobrando normalmente, não pode usar isso como desculpa pra recusar a indenização depois.", 4, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "E SE NÃO TIVER AVISADO?", "Sem aviso, o risco de perder<br>tudo é <span class='hl'>real</span>",
                    "O art. 768 do Código Civil tira o direito à indenização se o segurado agravar o risco de forma intencional e não contar pra seguradora.", 5, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Mudou a atividade, o estoque<br>ou o uso do imóvel? <span class='hl'>Avisa</span> antes",
                    "Um telefonema ou e-mail pro corretor evita virar motivo de negativa depois. Manda pra quem administra um negócio com seguro empresarial.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_05_papo_corretor_marco_legal():
    out = os.path.join(CONTENT, "semana-08", "post-05-papo-corretor-marco-legal")
    total = 6
    slides = [
        notebook_slide(LOGO, "PAPO DE CORRETOR",
                        "O que muda na sua rotina<br>com a <span class='hl'>Lei 15.040/2024</span>",
                        [], "Com fonte. Não é achismo.", 1, total),
        notebook_slide(LOGO, "JÁ VALE", "Em vigor desde<br><span class='hl'>10/12/2025</span>",
                        [{"label": "Contratos novos, alterados ou renovação não automática", "value": "regra nova", "highlight": True}],
                        "Apólice vigente e renovação automática já firmada continuam na regra antiga até o próximo evento contratual.", 2, total),
        notebook_slide(LOGO, "SEU PAPEL MUDOU DE PATAMAR", "Você deixa de ser<br>só <span class='hl'>intermediário</span>",
                        [],
                        "A lei coloca o corretor como figura central na orientação do cliente — inclusive sobre o questionário de risco e as consequências de omissão.", 3, total),
        notebook_slide(LOGO, "RISCO NOVO PRA VOCÊ", "Falha na orientação vira<br><span class='hl'>responsabilidade civil</span>",
                        [{"label": "Mesmo por imprudência ou negligência", "value": "pode gerar indenização", "highlight": True}],
                        "Documentar a orientação dada ao cliente deixou de ser boa prática — virou proteção jurídica pra você.", 4, total),
        notebook_slide(LOGO, "PRAZO QUE VOCÊ PRECISA COBRAR", "Regulação de sinistro<br>em até <span class='hl'>30 dias</span>",
                        [{"label": "Casos mais complexos", "value": "até 120 dias"},
                         {"label": "Seguradora que não se manifesta", "value": "pode perder o direito de recusar", "highlight": True}],
                        "Vale acompanhar de perto o prazo do sinistro do seu cliente — o silêncio da seguradora agora conta contra ela.", 5, total),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Atualiza seu roteiro de<br>venda e <span class='hl'>renovação</span>",
                        [], "Cliente pergunta \"isso mudou pra mim?\" — agora você responde com prazo e artigo de lei. Manda pro colega corretor que ainda não leu a lei nova.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_06_teste_domingo(post_01_dir):
    """Teste de domingo: repete o pilar consumidor mais universal da semana
    (Post 1 — furto/roubo em estacionamento, se aplica a qualquer motorista,
    não só quem tem casa ou empresa), em pasta própria."""
    out = os.path.join(CONTENT, "semana-08", "post-06-teste-domingo-estacionamento")
    os.makedirs(out, exist_ok=True)
    for i in range(1, 7):
        name = f"slide-{i:02d}.png"
        shutil.copyfile(os.path.join(post_01_dir, name), os.path.join(out, name))
    return out


if __name__ == "__main__":
    p1 = build_post_01_mito_estacionamento()
    build_post_02_mito_residencial_vendaval()
    build_post_03_vale_a_pena_moto()
    build_post_04_caso_real_agravamento_risco()
    build_post_05_papo_corretor_marco_legal()
    build_post_06_teste_domingo(p1)
    print("Lote 8 gerado.")
