"""Gera o Lote 11 — ramos da semana: Seguro Condomínio (ramo novo no canal, obrigatoriedade do art. 1.346
do Código Civil e o que cobre/não cobre), Seguro Obrigatório de veículos (DPVAT/SPVAT — status atual,
LC 211/2024), Seguro-Fiança Locatícia (ramo novo no canal, Lei 8.245/1991 art. 37), Caso prático sobre os
prazos de sinistro da Lei 15.040/2024 (arts. 86-87) e Papo de Corretor sobre a Consulta Pública Susep
05/2026 (sustentabilidade, IFRS S1/S2). Seguro saúde nunca entra."""

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
SEM = "semana-11"


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


def build_post_01_mito_condominio():
    out = os.path.join(CONTENT, SEM, "post-01-mito-seguro-condominio")
    photo = p("ref-pexels-house.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "O seguro do condomínio<br>já protege o <span class='hl'>interior do seu<br>apartamento</span>?",
                    "A taxa chega todo mês — mas o que ela realmente cobre costuma ser outra história.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Em regra, não</span> — cobre a estrutura e as áreas comuns",
                    "O Código Civil (art. 1.346) obriga o seguro da edificação contra incêndio e destruição, mas o que fica dentro da sua unidade depende do que a apólice descreve.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O QUE É OBRIGATÓRIO", "Seguro da edificação contra <span class='hl'>incêndio ou destruição</span>",
                    "Vale pra condomínio residencial, comercial e misto. A contratação é responsabilidade do síndico, que representa o condomínio.", 3, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "O PRAZO DA LEI", "<span class='hl'>120 dias</span> depois do habite-se",
                    "É o prazo previsto na legislação condominial pra contratar o seguro; descumprir sujeita o condomínio a multa. Síndico sem seguro assume um risco que não é só dele.", 4, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O QUE FICA DE FORA", "Móveis, eletrônicos e <span class='hl'>roubo</span> dentro do apê",
                    "O que você guarda dentro de casa só entra em seguro próprio. Seguro residencial e seguro condomínio são produtos diferentes, que se complementam.", 5, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Pede a <span class='hl'>apólice do condomínio</span> na próxima assembleia",
                    "Manda pra quem mora em apartamento e nunca viu o que o seguro do prédio cobre.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_02_mito_dpvat():
    out = os.path.join(CONTENT, SEM, "post-02-mito-dpvat-spvat")
    photo = p("ref-pexels-bmw-damaged.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "O DPVAT voltou e você<br>já <span class='hl'>paga junto com o<br>licenciamento</span>?",
                    "Muita gente ainda procura esse seguro no boleto do carro. A situação mudou duas vezes em dois anos.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span> — hoje ninguém paga seguro obrigatório de trânsito",
                    "O SPVAT, sucessor do DPVAT, foi criado pela Lei Complementar 207/2024 e revogado pela LC 211/2024, em 30/12/2024 — antes de começar a ser cobrado.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "E SE EU SOFRI ACIDENTE ANTES?", "Ainda dá pra pedir <span class='hl'>até R$ 13.500</span>",
                    "Quem sofreu acidente com morte ou invalidez no período em que o DPVAT estava ativo pode requerer indenização, dentro do prazo de 3 anos.", 3, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "E O FUTURO?", "Existe <span class='hl'>projeto</span> pra trazer o seguro de volta",
                    "O PL 1994/25 foi aprovado na comissão de Viação e Transportes da Câmara em março de 2026 — ainda precisa passar pelo Senado e ser sancionado.", 4, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "ATENÇÃO", "Sem DPVAT, a <span class='hl'>proteção é por sua conta</span>",
                    "Seguro auto com cobertura de danos pessoais e acidentes pessoais de passageiros (APP) passou a ser o caminho voluntário de proteção a vítimas.", 5, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Cobrança de <span class='hl'>'DPVAT' hoje</span> é golpe até prova em contrário",
                    "Manda pra quem recebeu boleto ou mensagem cobrando esse seguro. Confira sempre o licenciamento no site do Detran do seu estado.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_03_vale_a_pena_seguro_fianca():
    out = os.path.join(CONTENT, SEM, "post-03-vale-a-pena-seguro-fianca")
    total = 6
    slides = [
        notebook_slide(LOGO, "VALE A PENA?",
                        "Seguro-fiança no aluguel:<br>sem fiador, sem depósito —<br><span class='hl'>vale a pena</span>?",
                        [], "Os números e a lei, em 5 slides 👇", 1, total),
        notebook_slide(LOGO, "O QUE É", "Uma das garantias previstas na Lei do Inquilinato",
                        [{"label": "Lei", "value": "8.245/1991, art. 37", "highlight": True},
                         {"label": "Modalidades", "value": "caução, fiança, seguro-fiança, quotas de fundo"}],
                        "A seguradora garante o aluguel e encargos ao proprietário se o inquilino deixar de pagar.", 2, total),
        notebook_slide(LOGO, "REGRA DE OURO", "O proprietário só pode exigir <span class='hl'>uma</span> garantia",
                        [{"label": "Mais de uma modalidade", "value": "nulo", "highlight": True}],
                        "A lei veda mais de uma modalidade no mesmo contrato, sob pena de nulidade: não pode pedir fiador E caução ao mesmo tempo.", 3, total),
        notebook_slide(LOGO, "QUANTO CUSTA", "Em média, de 1 a 2,5 aluguéis por ano",
                        [{"label": "Prêmio anual", "value": "≈ 8% a 16% do aluguel anual", "highlight": True},
                         {"label": "Pagamento", "value": "pode ser parcelado"}],
                        "Faixa varia com o perfil de crédito do inquilino e a seguradora. Valor de referência de mercado, não tabela oficial.", 4, total),
        notebook_slide(LOGO, "O PEGA-RATÃO", "Não é um gasto que 'some' nem te livra da dívida",
                        [{"label": "Se você não pagar", "value": "a seguradora cobra de você", "highlight": True}],
                        "O prêmio é custo anual, sem devolução, e a dívida de aluguel atrasado continua sendo sua perante a seguradora.", 5, total),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Vale quando você <span class='hl'>não tem fiador</span> nem quer travar um caução",
                        [], "Compara o custo anual com os 3 meses de depósito. Salva pra consultar na hora de alugar e manda pra quem está procurando imóvel.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_04_caso_pratico_prazo_sinistro():
    out = os.path.join(CONTENT, SEM, "post-04-caso-pratico-prazo-sinistro")
    photo = p("ref-pexels-contract.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "CASO PRÁTICO",
                    "Avisou o sinistro e a<br>seguradora <span class='hl'>sumiu por<br>40 dias</span> — pode?",
                    "Caso ilustrativo, baseado em situação comum e na lei vigente desde dezembro de 2025.", 1, total),
        photo_slide(LOGO, photo, "O QUE DIZ A LEI", "A Lei 15.040/2024 fixou <span class='hl'>30 dias</span> pra seguradora se manifestar",
                    "Contados do aviso de sinistro com todos os documentos necessários (art. 86), a seguradora precisa dizer se há ou não cobertura.", 2, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "E SE ELA NÃO RESPONDER?", "Perde o <span class='hl'>direito de recusar</span>",
                    "A lei prevê decadência do direito de recusar a cobertura quando o prazo passa sem manifestação — um freio importante pra silêncio estratégico.", 3, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "RECONHECEU A COBERTURA", "Mais <span class='hl'>30 dias</span> pra pagar",
                    "Reconhecida a cobertura, o pagamento tem prazo máximo de 30 dias (art. 87). Pedido de documento extra pode suspender o prazo, no máximo 2 vezes.", 4, total, accent="#FFC93C"),
        photo_slide(LOGO, photo, "SE ATRASAR", "Multa de <span class='hl'>2%</span>, juros e perdas e danos",
                    "O atraso no pagamento gera multa, além de juros legais e eventuais perdas e danos, conforme a lei.", 5, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Aviso <span class='hl'>por escrito</span>, com protocolo, sempre",
                    "O prazo só conta com o aviso completo. Guarda o protocolo e manda pra quem já esperou resposta de seguradora.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_05_papo_corretor_susep_sustentabilidade():
    out = os.path.join(CONTENT, SEM, "post-05-papo-corretor-susep-cp-05-2026")
    total = 6
    slides = [
        notebook_slide(LOGO, "PAPO DE CORRETOR",
                        "Susep quer que o mercado <span class='hl'>reporte</span><br>risco climático como empresa grande",
                        [], "Consulta pública nova. O que já se sabe, com fonte.", 1, total),
        notebook_slide(LOGO, "O QUE É", "Consulta Pública Susep nº 05/2026",
                        [{"label": "Objeto", "value": "regras de sustentabilidade", "highlight": True},
                         {"label": "Substitui", "value": "Circular Susep 666/2022"}],
                        "Proposta de atualização das regras de divulgação de riscos e oportunidades ambientais, sociais e climáticos.", 2, total),
        notebook_slide(LOGO, "O PADRÃO", "Aproxima o setor das normas IFRS S1 e S2",
                        [{"label": "Referência", "value": "ISSB (padrão internacional)", "highlight": True}],
                        "Mais detalhe sobre riscos, impacto no modelo de negócio, resiliência e análise de cenários climáticos.", 3, total),
        notebook_slide(LOGO, "O CALENDÁRIO PROPOSTO", "Vigência em <span class='hl'>31/12/2026</span>, se aprovada",
                        [{"label": "Coleta de dados", "value": "2027", "highlight": True},
                         {"label": "Divulgação", "value": "2028"}],
                        "A minuta ficou aberta a contribuições do mercado por 30 dias. É proposta, não norma final.", 4, total),
        notebook_slide(LOGO, "O QUE ISSO MUDA PRA VOCÊ", "Cliente vai perguntar mais sobre <span class='hl'>risco climático</span>",
                        [{"label": "Efeito esperado", "value": "mais pergunta, mais transparência"}],
                        "Quem sabe explicar risco de enchente, vendaval e seca vira referência. Isto é uma leitura, não uma exigência da norma.", 5, total),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Acompanha o texto final no <span class='hl'>site da Susep</span>",
                        [], "Proposta pode mudar até a versão final. Manda pro colega corretor que acompanha regulação.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_06_teste_domingo(post_01_dir):
    """Teste de domingo: repete o pilar consumidor mais universal (Post 1 — seguro condomínio)."""
    out = os.path.join(CONTENT, SEM, "post-06-teste-domingo-seguro-condominio")
    os.makedirs(out, exist_ok=True)
    for i in range(1, 7):
        name = f"slide-{i:02d}.png"
        shutil.copyfile(os.path.join(post_01_dir, name), os.path.join(out, name))
    return out


if __name__ == "__main__":
    p1 = build_post_01_mito_condominio()
    build_post_02_mito_dpvat()
    build_post_03_vale_a_pena_seguro_fianca()
    build_post_04_caso_pratico_prazo_sinistro()
    build_post_05_papo_corretor_susep_sustentabilidade()
    build_post_06_teste_domingo(p1)
    print("Lote 11 gerado.")
