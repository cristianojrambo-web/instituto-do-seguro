"""Gera o Lote 17 — Mito: CNH vencida x seguro auto; Mito: seguro auto na Argentina / Carta Verde;
Vale a pena: seguro de acidentes pessoais; Caso pratico: notebook furtado de dentro do carro;
Papo de Corretor: Resolucao CNSP 496/2026 (seguros de danos). Seguro saude nunca entra."""


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
SEM = "semana-17"


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
    t = 7
    return build("post-01-mito-cnh-vencida-seguro-auto", [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "CNH vencida: o seguro<br>auto <span class='hl'>não paga</span>?",
                    "Antes de entrar em pânico, veja o que os tribunais têm decidido.", 1, t),
        photo_slide(LOGO, photo, "A RESPOSTA", "Em regra, <span class='hl'>mito</span>",
                    "Decisões de tribunais estaduais tratam a CNH vencida, sozinha, como infração administrativa, insuficiente para negar a indenização.", 2, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O QUE PESA", "Relação com o <span class='hl'>acidente</span>",
                    "Nessas decisões, a negativa só se sustenta se ficar demonstrado que a situação teve ligação com o sinistro ou agravou o risco.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "CUIDADO", "Vencida não é <span class='hl'>suspensa</span>",
                    "CNH suspensa ou cassada é tratada como dirigir sem habilitação. Há decisão negando o seguro nesse caso, como uma divulgada pelo TJMG.", 4, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "MARCO LEGAL DOS SEGUROS", "Agravamento precisa ser <span class='hl'>intencional e relevante</span>",
                    "A Lei 15.040/2024 (art. 13) diz que perde a garantia quem agrava o risco de forma intencional e relevante. Em vigor desde 10/12/2025.", 5, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "NA PRÁTICA", "Não existe <span class='hl'>garantia</span> de pagamento",
                    "Cada caso é analisado pela seguradora e, se houver disputa, pela Justiça. Renovar a CNH em dia evita a discussão.", 6, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Quando vence a <span class='hl'>sua CNH</span>?",
                    "Manda pra quem está com a carteira vencida na gaveta.", 7, t),
    ])


def post_02():
    photo = p("ref-pexels-navigation.jpg")
    t = 6
    return build("post-02-mito-seguro-auto-argentina-carta-verde", [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Vai de carro pra Argentina?<br>Seu seguro auto <span class='hl'>vale lá</span>?",
                    "Férias chegando: confira antes de pegar a estrada.", 1, t),
        photo_slide(LOGO, photo, "A RESPOSTA", "Em geral, <span class='hl'>mito</span>",
                    "O seguro auto costuma valer só no Brasil. Algumas apólices oferecem extensão de cobertura para países vizinhos. Confira a sua.", 2, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "CARTA VERDE", "Seguro <span class='hl'>obrigatório</span> no Mercosul",
                    "Para circular com carro brasileiro em países como Argentina, Uruguai e Paraguai, a Carta Verde é exigida. Sem ela, a aduana pode barrar.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "O QUE ELA COBRE", "Só danos a <span class='hl'>terceiros</span>",
                    "Danos materiais e corporais causados a outras pessoas em acidente de trânsito. O seu próprio carro fica de fora.", 4, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "E O SEU CARRO?", "Pergunte pela <span class='hl'>extensão</span> antes",
                    "Roubo e colisão lá fora dependem da sua apólice. E saúde e bagagem de quem viaja são outro produto: o seguro viagem.", 5, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Carta Verde <span class='hl'>na mala</span>?",
                    "Manda pra quem vai viajar de carro nas férias.", 6, t),
    ])


def post_03():
    t = 7
    return build("post-03-vale-a-pena-acidentes-pessoais", [
        notebook_slide(LOGO, "VALE A PENA?",
                       "Seguro de acidentes pessoais:<br><span class='hl'>vale a pena</span>?",
                       [], "O primo mais barato do seguro de vida. Veja 👇", 1, t),
        notebook_slide(LOGO, "O QUE COBRE", "Só eventos causados por <span class='hl'>acidente</span>",
                       [{"label": "Básica", "value": "morte acidental", "highlight": True},
                        {"label": "Comum", "value": "invalidez por acidente"},
                        {"label": "Opcionais", "value": "despesas médicas, diárias"}],
                       "Coberturas e limites variam por produto.", 2, t),
        notebook_slide(LOGO, "O QUE NÃO COBRE", "Morte por <span class='hl'>doença</span> fica de fora",
                       [{"label": "Infarto, AVC", "value": "não cobre", "highlight": True},
                        {"label": "Exclusões", "value": "lista da apólice"}],
                       "É aqui que muita gente se confunde.", 3, t),
        notebook_slide(LOGO, "AP x VIDA", "A diferença está na <span class='hl'>causa</span>",
                       [{"label": "Acidentes pessoais", "value": "só acidente", "highlight": True},
                        {"label": "Seguro de vida", "value": "doença + acidente"},
                        {"label": "Preço", "value": "AP costuma ser menor"}],
                       "Cobre menos, custa menos.", 4, t),
        notebook_slide(LOGO, "QUANTO CUSTA", "Blogs citam <span class='hl'>R$ 10 a R$ 80</span>/mês",
                       [{"label": "Varia por", "value": "capital e coberturas", "highlight": True},
                        {"label": "Ex. de produto", "value": "despesas médicas até R$ 10 mil"}],
                       "Estimativas de mercado, não tabela oficial. Peça cotação.", 5, t),
        notebook_slide(LOGO, "PRA QUEM FAZ SENTIDO", "Orçamento curto ou <span class='hl'>rotina de risco</span>",
                       [{"label": "Porta de entrada", "value": "sim", "highlight": True},
                        {"label": "Tem dependentes?", "value": "compare com vida"}],
                       "Quem depende da sua renda precisa de proteção também contra doença.", 6, t),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Vale como <span class='hl'>complemento</span>, não substituto",
                       [], "Essa comparação é longa demais pra decorar: salva pra consultar depois.", 7, t),
    ])


def post_04():
    photo = p("ref-pexels-bmw-damaged.jpg")
    t = 6
    return build("post-04-caso-pratico-objetos-furtados-no-carro", [
        photo_slide(LOGO, photo, "CASO PRÁTICO",
                    "Notebook furtado de dentro do carro<br>e o seguro <span class='hl'>não pagou</span>. Por quê?",
                    "Caso ilustrativo, baseado em dúvida comum. Não é caso real identificável.", 1, t),
        photo_slide(LOGO, photo, "A SITUAÇÃO", "Vidro quebrado, <span class='hl'>mochila levada</span>",
                    "Imagine alguém que deixou a mochila com o notebook no banco e, ao voltar, encontrou o vidro estourado.", 2, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O PONTO", "O seguro auto protege <span class='hl'>o carro</span>",
                    "Em geral, objetos pessoais deixados no veículo não entram na cobertura. O vidro pode ser indenizado, conforme a apólice e a franquia.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "ACESSÓRIOS", "Som, rodas, kit: <span class='hl'>declare</span>",
                    "Acessórios instalados depois da compra precisam ser declarados e segurados à parte para ter cobertura.", 4, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "ONDE PROTEGER", "Notebook tem <span class='hl'>seguro próprio</span>",
                    "Equipamentos portáteis podem ter apólice específica. Em qualquer caso: registre o B.O. o quanto antes e não deixe nada à vista.", 5, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "O que você costuma <span class='hl'>deixar no carro</span>?",
                    "Manda pra quem usa o porta-malas de escritório.", 6, t),
    ])


def post_05():
    t = 7
    return build("post-05-papo-corretor-resolucao-cnsp-496", [
        notebook_slide(LOGO, "PAPO DE CORRETOR",
                       "Resolução CNSP 496/2026:<br>o que muda nos <span class='hl'>seguros de danos</span>",
                       [], "Prazo de adaptação vence em janeiro. 👇", 1, t),
        notebook_slide(LOGO, "O QUE É", "Nova regra geral dos <span class='hl'>seguros de danos</span>",
                       [{"label": "Publicada", "value": "agosto/2026", "highlight": True},
                        {"label": "Revoga", "value": "Res. CNSP 407/2021"},
                        {"label": "Base", "value": "Lei 15.040/2024"}],
                       "Deixa de reproduzir a antiga separação massificados x grandes riscos.", 2, t),
        notebook_slide(LOGO, "SINISTRO", "Regulação em até <span class='hl'>30 dias</span>",
                       [{"label": "Regulação", "value": "até 30 dias", "highlight": True},
                        {"label": "Pagamento após cobertura", "value": "até 30 dias"},
                        {"label": "Petróleo, aero, marítimo, nuclear", "value": "até 120 dias"}],
                       "Contados da apresentação da reclamação.", 3, t),
        notebook_slide(LOGO, "REGRAS PRÓPRIAS", "<span class='hl'>7 grupos</span> com disciplina específica",
                       [{"label": "Riscos nomeados e operacionais", "value": "acima de R$ 15 mi", "highlight": True},
                        {"label": "Também", "value": "BBB, crédito, petróleo"},
                        {"label": "E", "value": "aero, marítimo, nuclear"}],
                       "Limite de R$ 15 mi segundo análise jurídica publicada.", 4, t),
        notebook_slide(LOGO, "CALENDÁRIO", "Adaptação até <span class='hl'>04/01/2027</span>",
                       [{"label": "Planos já registrados", "value": "até 04/01/2027", "highlight": True},
                        {"label": "Contratos e renovações", "value": "a partir de 05/01/2027"}],
                       "Renovações de janeiro já entram na regra nova.", 5, t),
        notebook_slide(LOGO, "AINDA FALTA", "Susep ainda vai editar <span class='hl'>normas complementares</span>",
                       [{"label": "Condições personalizadas", "value": "aguardam Susep", "highlight": True},
                        {"label": "Mercado", "value": "há críticas de especialistas"}],
                       "Acompanhe as circulares antes de orientar o cliente.", 6, t),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Revise sua carteira de danos <span class='hl'>antes de janeiro</span>",
                       [], "Confirme o texto oficial. Manda pro colega corretor.", 7, t),
    ])


def post_06(src, n):
    out = os.path.join(CONTENT, SEM, "post-06-teste-domingo-cnh-vencida-seguro-auto")
    os.makedirs(out, exist_ok=True)
    for i in range(1, n + 1):
        shutil.copyfile(os.path.join(src, f"slide-{i:02d}.png"), os.path.join(out, f"slide-{i:02d}.png"))


if __name__ == "__main__":
    s1 = post_01()
    post_02(); post_03(); post_04(); post_05()
    post_06(s1, 7)
    print("Lote 17 gerado.")
