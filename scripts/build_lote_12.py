"""Gera o Lote 12 — Mito: seguro de vida x inventário (Lei 15.040/2024, art. 116, revogou o art. 794 do CC);
Mito: seguro de celular x furto simples/quebra; Vale a pena: seguro de bicicleta/e-bike; Caso prático: sub-rogação
(art. 94 da Lei 15.040/2024, Súmula 188 STF); Papo de Corretor: números CNseg 2026. Seguro saúde nunca entra."""

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
SEM = "semana-12"


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
    photo = p("ref-pexels-house.jpg")
    t = 6
    return build("post-01-mito-seguro-vida-inventario", [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "O dinheiro do seguro de vida<br><span class='hl'>fica preso no inventário</span>?",
                    "Muita família acredita nisso — e adia pedir a indenização por medo da burocracia.", 1, t),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span> — o capital segurado não é herança",
                    "A Lei 15.040/2024 (art. 116) diz que o capital segurado devido em razão de morte não é considerado herança para nenhum efeito.", 2, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "QUEM RECEBE", "Quem o segurado <span class='hl'>indicou na apólice</span>",
                    "A indicação do beneficiário é livre (art. 113), com exceções como concubinato e beneficiário que seja credor do segurado.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "SEM BENEFICIÁRIO", "Metade pro <span class='hl'>cônjuge</span>, metade pros herdeiros",
                    "Se não houver beneficiário válido, o art. 115 divide o capital: metade ao cônjuge, se houver, e metade aos herdeiros.", 4, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "ATENÇÃO NA LEI", "O <span class='hl'>art. 794</span> do Código Civil foi revogado",
                    "Conteúdo antigo ainda cita esse artigo. Desde 10/12/2025 a regra está na Lei 15.040/2024. Prazo pra cobrar: 3 anos da ciência do fato (arts. 126 e 127).", 5, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Mantenha o <span class='hl'>beneficiário atualizado</span>",
                    "Manda pra alguém que tem seguro de vida e nunca revisou a apólice.", 6, t),
    ])


def post_02():
    photo = p("ref-pexels-rideapp.jpg")
    t = 6
    return build("post-02-mito-seguro-celular", [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "O seguro do celular cobre se<br>levarem do seu bolso <span class='hl'>sem<br>você ver</span>?",
                    "Antes de pagar caro por um plano, confira o que a apólice entende por 'furto'.", 1, t),
        photo_slide(LOGO, photo, "A RESPOSTA", "Em geral, <span class='hl'>não</span> — o núcleo é roubo e furto qualificado",
                    "Na maioria dos planos, furto qualificado exige arrombamento ou rompimento de obstáculo. O furto simples (descuido) costuma ficar de fora.", 2, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "QUEBRA DA TELA", "Quebra acidental costuma ser <span class='hl'>cobertura à parte</span>",
                    "Planos descrevem quedas, oscilações de energia, curto-circuito e oxidação por líquidos como cobertura opcional, com preço próprio.", 3, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "O CUSTO ESCONDIDO", "<span class='hl'>Franquia</span> a cada acionamento",
                    "Há planos com franquia em percentual do valor segurado (exemplo de mercado: 25%), cobrada sempre que o seguro é usado.", 4, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "CARÊNCIA", "Alguns planos têm <span class='hl'>30 dias</span> pra danos",
                    "Varia por seguradora: há quem tenha carência e quem não tenha. Está sempre nas condições gerais registradas na Susep.", 5, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Leia as <span class='hl'>exclusões</span> antes de contratar",
                    "Manda pra quem está pensando em assinar seguro de celular.", 6, t),
    ])


def post_03():
    t = 6
    return build("post-03-vale-a-pena-seguro-bicicleta", [
        notebook_slide(LOGO, "VALE A PENA?",
                       "Seguro de bicicleta e<br>bike elétrica: <span class='hl'>vale a pena</span>?",
                       [], "Os números de referência, em 5 slides 👇", 1, t),
        notebook_slide(LOGO, "O QUE COBRE", "Núcleo: roubo e furto qualificado",
                       [{"label": "Mais comum", "value": "roubo + furto qualificado", "highlight": True},
                        {"label": "Opcional", "value": "acidentes, RC, transporte"}],
                       "Planos variam: algumas seguradoras incluem responsabilidade civil (danos a terceiros) e acidentes pessoais.", 2, t),
        notebook_slide(LOGO, "QUANTO CUSTA", "Referência de mercado: <span class='hl'>≈ R$ 800/ano</span>",
                       [{"label": "Bike de R$ 10 mil", "value": "≈ R$ 800/ano", "highlight": True},
                        {"label": "Plano básico", "value": "a partir de R$ 31,90/mês"}],
                       "Valores de reportagens, sem tabela oficial. O preço depende do valor declarado da bike.", 3, t),
        notebook_slide(LOGO, "A PARTIR DE QUANTO", "Faz mais sentido em bike acima de <span class='hl'>R$ 3 mil</span>",
                       [{"label": "Indicação de seguradora", "value": "alto valor agregado", "highlight": True}],
                       "É a leitura de um gerente de seguradora, não uma regra. Bike barata costuma não compensar.", 4, t),
        notebook_slide(LOGO, "ATENÇÃO NA E-BIKE", "Confira se o <span class='hl'>seu modelo</span> entra",
                       [{"label": "Exemplo de produto", "value": "sem acelerador, < 800 W", "highlight": True}],
                       "Há produtos voltados a modelos de bike elétrica com limite de potência. Seguradoras podem exigir cadeado e outras medidas de segurança, vale checar.", 5, t),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Vale se a bike <span class='hl'>custa caro</span> e você a deixa na rua",
                       [], "Compara o prêmio anual com o valor da bike e as exclusões. Salva pra consultar e manda pra quem pedala.", 6, t),
    ])


def post_04():
    photo = p("ref-pexels-crash.jpg")
    t = 6
    return build("post-04-caso-pratico-sub-rogacao", [
        photo_slide(LOGO, photo, "CASO PRÁTICO",
                    "Bateram no seu carro, a<br>seguradora pagou — e <span class='hl'>o culpado<br>paga o quê</span>?",
                    "Caso ilustrativo, baseado em situação comum e na lei vigente desde dezembro de 2025.", 1, t),
        photo_slide(LOGO, photo, "O QUE DIZ A LEI", "Seguradora assume seus direitos contra o <span class='hl'>causador</span>",
                    "É a sub-rogação, prevista no art. 94 da Lei 15.040/2024 (antes, art. 786 do Código Civil). Vale pros seguros de dano.", 2, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O LIMITE", "Só até o <span class='hl'>valor que ela pagou</span>",
                    "A Súmula 188 do STF fixa: a seguradora cobra do causador o que pagou, até o limite do contrato. E só nasce depois do pagamento ao segurado.", 3, t, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "E A SUA FRANQUIA?", "Parte não paga <span class='hl'>continua sendo sua</span>",
                    "Tribunais já trataram o caso em que a seguradora cobriu o dano menos a franquia: o segurado segue com direito sobre o que ficou de fora.", 4, t, accent="#FFC93C"),
        photo_slide(LOGO, photo, "CUIDADO", "Acordo que prejudica a seguradora é <span class='hl'>ineficaz</span>",
                    "A lei não aceita ato do segurado que reduza ou extinga a sub-rogação. Dar quitação ao causador sem avisar a seguradora gera problema.", 5, t, accent="#FF8A65"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Antes de <span class='hl'>fechar acordo</span>, fala com a seguradora",
                    "Manda pra quem já foi batido no trânsito.", 6, t),
    ])


def post_05():
    t = 6
    return build("post-05-papo-corretor-numeros-cnseg-2026", [
        notebook_slide(LOGO, "PAPO DE CORRETOR",
                       "O que os números da <span class='hl'>CNseg</span><br>dizem pro corretor em 2026",
                       [], "Projeção revisada, rural em queda e previdência pesando.", 1, t),
        notebook_slide(LOGO, "A PROJEÇÃO", "CNseg cortou o crescimento de <span class='hl'>8% pra 5,7%</span>",
                       [{"label": "Arrecadação 2026", "value": "R$ 808 bi", "highlight": True},
                        {"label": "Revisão feita em", "value": "abril/2026"}],
                       "Estimativa para o setor, apresentada em coletiva da CNseg em 15/04/2026.", 2, t),
        notebook_slide(LOGO, "PRIMEIRO BIMESTRE", "Pessoas <span class='hl'>+6,8%</span>, Danos estável",
                       [{"label": "Setor arrecadou", "value": "R$ 68,3 bi", "highlight": True},
                        {"label": "Danos e Resp.", "value": "−0,1%"}],
                       "Pessoas puxou o resultado do início do ano.", 3, t),
        notebook_slide(LOGO, "SEGURO RURAL", "Projeção de queda de <span class='hl'>3,9%</span> em 2026",
                       [{"label": "2025", "value": "−8,8% (R$ 12,9 bi)", "highlight": True},
                        {"label": "Subvenção prevista", "value": "≈ R$ 1 bi"}],
                       "A CNseg cita risco climático e restrição orçamentária. Em 2025, R$ 445,1 mi dos R$ 1,06 bi foram bloqueados.", 4, t),
        notebook_slide(LOGO, "ATÉ JULHO", "Arrecadação <span class='hl'>−1%</span>, pressionada pela previdência",
                       [{"label": "Pagamentos (sem saúde)", "value": "R$ 150,3 bi", "highlight": True},
                        {"label": "Previdência Aberta", "value": "R$ 84,1 bi"}],
                       "Pagamentos de indenizações, benefícios, resgates e sorteios caíram 2,7% no acumulado.", 5, t),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Cada ramo anda numa <span class='hl'>velocidade</span> diferente",
                       [], "Quem diversifica a carteira dilui o risco. Manda pro colega corretor.", 6, t),
    ])


def post_06(src):
    out = os.path.join(CONTENT, SEM, "post-06-teste-domingo-seguro-vida-inventario")
    os.makedirs(out, exist_ok=True)
    for i in range(1, 7):
        shutil.copyfile(os.path.join(src, f"slide-{i:02d}.png"), os.path.join(out, f"slide-{i:02d}.png"))


if __name__ == "__main__":
    s1 = post_01()
    post_02(); post_03(); post_04(); post_05()
    post_06(s1)
    print("Lote 12 gerado.")
