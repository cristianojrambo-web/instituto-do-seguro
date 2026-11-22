"""Gera o Lote 18 — Mito: carencia no seguro de vida (Lei 15.040/2024); Mito: protecao veicular
x seguro auto (LC 213/2025 e Res. CNSP 491/2026); Vale a pena: seguro empresarial para MEI;
Caso pratico: mala extraviada na viagem de fim de ano; Papo de Corretor: dezembro e o PGBL.
Seguro saude nunca entra."""

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
SEM = "semana-18"


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
    photo = p("ref-pexels-contract.jpg")
    t = 7
    return build("post-01-mito-carencia-seguro-de-vida", [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Seguro de vida:<br>no começo <span class='hl'>não paga nada</span>?",
                    "A carência existe, mas a nova Lei de Seguros colocou limites.", 1, t),
        photo_slide(LOGO, photo, "A RESPOSTA", "Depende, e a <span class='hl'>carência tem teto</span>",
                    "A Lei 15.040/2024 permite carência para morte e invalidez por doença. Em muitas apólices, acidente não tem carência. Confira a sua.", 2, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O LIMITE", "Nunca mais que <span class='hl'>metade da vigência</span>",
                    "A lei proíbe carência que deixe a garantia inútil. Numa apólice de 1 ano, o máximo é 6 meses.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "DOENÇA PREEXISTENTE", "Com carência, <span class='hl'>não pode negar</span> por isso",
                    "Se a seguradora combinou carência, não pode recusar o pagamento alegando doença que você já tinha.", 4, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "TROCOU DE SEGURO?", "Renovação <span class='hl'>sem nova carência</span>",
                    "Na renovação ou na substituição do contrato, mesmo com outra seguradora, a lei não permite exigir nova carência.", 5, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "EXCEÇÃO", "Suicídio tem <span class='hl'>regra própria</span>",
                    "Nos 2 primeiros anos de vigência, o capital não é pago em caso de suicídio. A regra foi mantida. Contratos antigos seguem a lei da época.", 6, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Você sabe a <span class='hl'>carência</span> da sua apólice?",
                    "Manda pra quem acha que seguro de vida novo não vale nada.", 7, t),
    ])


def post_02():
    photo = p("ref-pexels-crash.jpg")
    t = 7
    return build("post-02-mito-protecao-veicular-x-seguro-auto", [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Proteção veicular é a<br>mesma coisa que <span class='hl'>seguro auto</span>?",
                    "Muita gente assina achando que é igual. Veja a diferença.", 1, t),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span>: são modelos diferentes",
                    "A própria Lei Complementar 213/2025, que trouxe as associações para a supervisão da Susep, não transformou proteção veicular em seguro.", 2, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "PROTEÇÃO VEICULAR", "Prejuízo dividido entre <span class='hl'>associados</span>",
                    "Funciona por rateio: os custos dos eventos do grupo são divididos entre os participantes, por isso o valor pode variar.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "SEGURO AUTO", "A obrigação é da <span class='hl'>seguradora</span>",
                    "A seguradora assume o risco e responde pela indenização prevista na apólice, com regras da Susep e da Lei de Seguros.", 4, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "O QUE MUDOU", "Regra nova da <span class='hl'>Susep</span> em 2026",
                    "A Resolução CNSP 491/2026 exige que as operações sejam geridas por administradora autorizada pela Susep. As associações têm prazo de adaptação.", 5, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "ANTES DE ASSINAR", "Leia o <span class='hl'>regulamento</span>",
                    "Veja como funciona o rateio, os limites e o prazo de pagamento. Compare com uma cotação de seguro feita por corretor.", 6, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "O seu carro tem <span class='hl'>seguro ou proteção</span>?",
                    "Manda pra quem vai renovar a proteção do carro este mês.", 7, t),
    ])


def post_03():
    t = 7
    return build("post-03-vale-a-pena-seguro-empresarial-mei", [
        notebook_slide(LOGO, "VALE A PENA?",
                       "Seguro empresarial pra MEI:<br><span class='hl'>vale a pena</span>?",
                       [], "Estoque cheio de fim de ano? Leia antes. 👇", 1, t),
        notebook_slide(LOGO, "COMO FUNCIONA", "Um produto, <span class='hl'>várias coberturas</span>",
                       [{"label": "Base", "value": "incêndio", "highlight": True},
                        {"label": "Opcionais", "value": "roubo, danos elétricos"},
                        {"label": "Também", "value": "vendaval, RC"}],
                       "Monta-se conforme o risco do negócio.", 2, t),
        notebook_slide(LOGO, "A MAIS ESQUECIDA", "<span class='hl'>Lucros cessantes</span>",
                       [{"label": "Incêndio paga", "value": "a reconstrução", "highlight": True},
                        {"label": "Lucros cessantes", "value": "despesas na parada"}],
                       "Sem ela, a loja fechada para obra não fatura e as contas continuam.", 3, t),
        notebook_slide(LOGO, "NÃO CONFUNDA", "Multirrisco <span class='hl'>não é RC profissional</span>",
                       [{"label": "Multirrisco", "value": "protege o local e bens", "highlight": True},
                        {"label": "RC profissional", "value": "erro no serviço"}],
                       "Quem presta serviço técnico pode precisar dos dois.", 4, t),
        notebook_slide(LOGO, "QUANTO CUSTA", "Há produtos a partir de <span class='hl'>~R$ 45/mês</span>",
                       [{"label": "Varia por", "value": "atividade e local", "highlight": True},
                        {"label": "Também", "value": "valor dos bens"}],
                       "Exemplo citado em reportagem, não tabela oficial. Peça cotação.", 5, t),
        notebook_slide(LOGO, "PRA QUEM FAZ SENTIDO", "Ponto físico, estoque ou <span class='hl'>equipamento</span>",
                       [{"label": "Loja, oficina, salão", "value": "faz sentido", "highlight": True},
                        {"label": "Só notebook em casa", "value": "veja outro produto"}],
                       "Informe o valor real dos bens na cotação.", 6, t),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Vale se o negócio <span class='hl'>não aguenta parar</span>",
                       [], "Essa lista é grande demais pra decorar: salva pra consultar depois.", 7, t),
    ])


def post_04():
    photo = p("ref-pexels-travel.jpg")
    t = 7
    return build("post-04-caso-pratico-mala-extraviada", [
        photo_slide(LOGO, photo, "CASO PRÁTICO",
                    "A mala não chegou<br>na viagem de fim de ano. <span class='hl'>E agora?</span>",
                    "Caso ilustrativo, baseado em dúvida comum. Não é caso real identificável.", 1, t),
        photo_slide(LOGO, photo, "A SITUAÇÃO", "Esteira vazia, <span class='hl'>férias começando</span>",
                    "Imagine alguém que desembarca para o Réveillon e descobre que a bagagem despachada não veio.", 2, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "PASSO 1", "Registre <span class='hl'>ainda no aeroporto</span>",
                    "Faça o Registro de Irregularidade de Bagagem (RIB) no balcão da companhia. Os prazos contam a partir dele.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "O PRAZO DA COMPANHIA", "<span class='hl'>7 dias</span> no Brasil, <span class='hl'>21</span> no exterior",
                    "Pela Resolução 400/2016 da ANAC, esse é o prazo para devolver a mala. Depois disso, a companhia deve indenizar.", 4, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "ENQUANTO ISSO", "Guarde as <span class='hl'>notas fiscais</span>",
                    "Fora da sua cidade, gastos de emergência (roupa, higiene) podem ser ressarcidos pela companhia. Sem comprovante, fica difícil.", 5, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "E O SEGURO VIAGEM?", "Pode ter cobertura de <span class='hl'>bagagem</span>",
                    "Muitos planos incluem extravio de bagagem, com limites próprios. Em geral, pedem o RIB da companhia. Leia as condições.", 6, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Já ficou <span class='hl'>sem a mala</span> numa viagem?",
                    "Manda pra quem vai viajar de avião nas festas.", 7, t),
    ])


def post_05():
    t = 7
    return build("post-05-papo-corretor-pgbl-dezembro", [
        notebook_slide(LOGO, "PAPO DE CORRETOR",
                       "Dezembro é o mês do <span class='hl'>PGBL</span>:<br>roteiro de abordagem",
                       [], "Prazo do ano-calendário acaba em 31/12. 👇", 1, t),
        notebook_slide(LOGO, "PARA QUEM", "Filtre o cliente <span class='hl'>antes de ligar</span>",
                       [{"label": "Declara IR", "value": "modelo completo", "highlight": True},
                        {"label": "Contribui para", "value": "INSS ou regime próprio"}],
                       "Fora disso, a dedução não se aplica.", 2, t),
        notebook_slide(LOGO, "O NÚMERO", "Até <span class='hl'>12%</span> da renda bruta tributável",
                       [{"label": "Renda de R$ 100 mil", "value": "aporte até R$ 12 mil", "highlight": True},
                        {"label": "Onde declarar", "value": "Pagamentos Efetuados"}],
                       "O teto de 12% é aplicado na declaração.", 3, t),
        notebook_slide(LOGO, "O PRAZO", "Aporte dentro do <span class='hl'>ano-calendário</span>",
                       [{"label": "Vale para o IR de 2027", "value": "aporte até 31/12/2026", "highlight": True},
                        {"label": "Fonte comum", "value": "13º salário"}],
                       "Oriente a não deixar para o último dia útil.", 4, t),
        notebook_slide(LOGO, "SEJA TRANSPARENTE", "No resgate, o IR incide sobre o <span class='hl'>total</span>",
                       [{"label": "PGBL", "value": "IR sobre tudo", "highlight": True},
                        {"label": "VGBL", "value": "IR só no rendimento"}],
                       "É diferimento de imposto, não isenção.", 5, t),
        notebook_slide(LOGO, "PASSOU DOS 12%?", "Excedente costuma ir pro <span class='hl'>VGBL</span>",
                       [{"label": "Acima do teto", "value": "avaliar VGBL", "highlight": True},
                        {"label": "Aporte alto em VGBL", "value": "confira regra de IOF"}],
                       "Cada caso tem que passar pelo contador do cliente.", 6, t),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Monte sua lista de <span class='hl'>clientes PGBL</span> hoje",
                       [], "Confirme as regras na Receita Federal. Manda pro colega corretor.", 7, t),
    ])


def post_06(src, n):
    out = os.path.join(CONTENT, SEM, "post-06-teste-domingo-protecao-veicular-x-seguro-auto")
    os.makedirs(out, exist_ok=True)
    for i in range(1, n + 1):
        shutil.copyfile(os.path.join(src, f"slide-{i:02d}.png"), os.path.join(out, f"slide-{i:02d}.png"))


if __name__ == "__main__":
    post_01()
    s2 = post_02()
    post_03(); post_04(); post_05()
    post_06(s2, 7)
    print("Lote 18 gerado.")
