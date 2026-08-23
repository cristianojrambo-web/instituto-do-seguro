"""Gera o Lote 5 — ramos da semana: Seguro Auto (condutor não declarado), Seguro Residencial
(Responsabilidade Civil Familiar), Seguro de Equipamentos/Máquinas (negócio, não agrícola),
Prescrição de ação contra seguradora (Lei 15.040/2024), RC Profissional (Papo de Corretor).
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


def build_post_01_mito_condutor():
    out = os.path.join(CONTENT, "semana-05", "post-01-mito-auto-condutor-nao-declarado")
    photo = p("ref-pexels-navigation.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Emprestar seu carro pra<br>alguém <span class='hl'>anula</span> o seguro?",
                    "Depende de um detalhe que a maioria só descobre depois de bater.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Depende</span> da frequência, não do empréstimo",
                    "Emprestar o carro uma vez pra alguém habilitado normalmente não tira sua cobertura.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "O RISCO REAL", "Virou <span class='hl'>condutor habitual</span>? Aí muda tudo",
                    "Se outra pessoa passa a usar o carro com frequência sem estar declarada, isso é agravamento de risco — motivo real de negativa na hora do sinistro.", 3, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O QUE A LEI NOVA DIZ", "Seguradora tem <span class='hl'>20 dias</span> pra agir",
                    "Pela Lei 15.040/2024, ao saber do agravamento de risco a seguradora tem 20 dias pra cobrar a diferença de prêmio ou resolver o contrato — que perde validade 30 dias depois disso.", 4, total),
        photo_slide(LOGO, photo, "ANTES QUE ACONTEÇA", "Exija <span class='hl'>CNH válida</span> e avise a seguradora",
                    "Se o carro passou a ser usado com frequência por outra pessoa, comunicar evita perder a indenização inteira depois.", 5, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Não é sobre desconfiar de<br>quem <span class='hl'>pede emprestado</span>",
                    "É sobre não descobrir sem cobertura na hora que você mais precisa. Manda pra quem empresta o carro sem pensar duas vezes.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_02_mito_rc_familiar():
    out = os.path.join(CONTENT, "semana-05", "post-02-mito-residencial-rc-familiar")
    photo = p("ref-pexels-house.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "MITO OU VERDADE",
                    "Seu seguro residencial só<br>cobre <span class='hl'>a sua</span> casa?",
                    "Tem uma cobertura que protege você quando o problema é o contrário.", 1, total),
        photo_slide(LOGO, photo, "A RESPOSTA", "<span class='hl'>Mito</span> — existe cobertura pro dano que você causa",
                    "É a Responsabilidade Civil Familiar: indeniza terceiros por dano acidental causado por você, sua família ou até empregados domésticos.", 2, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "NA PRÁTICA", "Vazamento que <span class='hl'>estraga</span> o apê debaixo",
                    "Infiltração, vaso que cai da sacada, bola que quebra o vidro do vizinho — sem essa cobertura, a conta do acidente sai do seu bolso.", 3, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "TAMBÉM VALE PRA", "<span class='hl'>Empregada doméstica</span> que se machucou em casa",
                    "Acidente de quem trabalha registrado na sua residência também pode entrar na cobertura, dependendo da apólice contratada.", 4, total),
        photo_slide(LOGO, photo, "ATENÇÃO", "Não vem de <span class='hl'>graça</span> no plano básico",
                    "É cobertura adicional — o valor de indenização (LMI) é escolhido na contratação; especialistas recomendam no mínimo R$100 mil.", 5, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Confere se seu plano<br><span class='hl'>já tem</span> essa proteção",
                    "Manda pra quem mora em prédio ou tem filho pequeno em casa.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_03_vale_a_pena_equipamentos():
    out = os.path.join(CONTENT, "semana-05", "post-03-vale-a-pena-equipamentos")
    total = 6
    slides = [
        notebook_slide(LOGO, "VALE A PENA?",
                        "Seguro de Equipamentos<br>e Máquinas: vale a <span class='hl'>pena</span>?",
                        [], "Ferramenta, gerador, computador, máquina de produção — separamos o que entra na proteção antes de você decidir.", 1, total),
        notebook_slide(LOGO, "COBERTURA", "O que costuma entrar<br>na <span class='hl'>proteção</span>",
                        [{"label": "Incêndio", "value": "cobre"},
                         {"label": "Roubo/furto qualificado", "value": "cobre"},
                         {"label": "Danos elétricos", "value": "cobre", "highlight": True},
                         {"label": "Quebra/falha mecânica", "value": "depende da apólice"}],
                        "A cobertura exata varia por seguradora e tipo de equipamento — vale conferir item a item.", 2, total),
        notebook_slide(LOGO, "O RISCO REAL", "Furto e roubo pesam<br>nos <span class='hl'>prejuízos</span>",
                        [{"label": "Roubo, furto e fraude", "value": "~11% dos riscos monitorados", "highlight": True}],
                        "Empresa que ainda não segurou máquina e equipamento está exposta a um risco que já é dado, não hipótese.", 3, total),
        notebook_slide(LOGO, "POR QUE FICA DE FORA", "Baixa <span class='hl'>procura</span>, não baixo risco",
                        [],
                        "O seguro de máquinas e equipamentos ainda tem baixa penetração no Brasil — mesmo crescendo, a maioria das empresas segura só o que está financiado (alienado), não o resto do parque.", 4, total),
        notebook_slide(LOGO, "QUEM PRECISA", "Qualquer negócio com<br><span class='hl'>equipamento essencial</span>",
                        [],
                        "Oficina, gráfica, obra, clínica, estúdio — se um equipamento parar, o negócio para. Isso já justifica cotar.", 5, total),
        notebook_slide(LOGO, "ENTÃO, VALE A PENA?", "Sim — principalmente pro<br>que <span class='hl'>não</span> está financiado",
                        [], "Guarda esse carrossel e revisa com o corretor o que já está protegido na sua empresa.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_04_caso_real_prescricao():
    out = os.path.join(CONTENT, "semana-05", "post-04-caso-real-prescricao")
    photo = p("ref-pexels-contract.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "ATENÇÃO",
                    "Perder o prazo pode acabar<br>com seu direito à <span class='hl'>indenização</span>",
                    "Caso ilustrativo, baseado em situação real e comum entre segurados.", 1, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "O PRAZO", "Você tem <span class='hl'>1 ano</span> pra cobrar da seguradora",
                    "A Lei 15.040/2024 (Marco Legal dos Seguros, art. 126) fixa esse prazo pra reclamar indenização, capital ou restituição de prêmio.", 2, total),
        photo_slide(LOGO, photo, "O QUE JÁ EXISTIA", "1 ano contado da <span class='hl'>recusa</span> não é novidade",
                    "Isso já vinha da Súmula 101 do STJ. A Lei 15.040/2024 agora torna essa regra lei — e mais clara pra cada tipo de seguro.", 3, total),
        photo_slide(LOGO, photo, "O QUE É NOVO DE VERDADE", "Pedido de reconsideração<br><span class='hl'>pausa</span> o prazo",
                    "Enquanto a seguradora reanalisa seu pedido, o prazo de 1 ano fica suspenso — só volta a correr quando ela decidir de novo. Isso não estava garantido antes com essa clareza.", 4, total, accent="#7BFFC0"),
        photo_slide(LOGO, photo, "FIQUE ATENTO", "Isso <span class='hl'>não</span> vale pra sempre",
                    "Mesmo com a suspensão, nenhuma pretensão pode passar de 10 anos no total (art. 205 do Código Civil) — mas o prazo de 1 ano ainda decide a maioria dos casos.", 5, total, accent="#FF8A65"),
        photo_slide(LOGO, photo, "GUARDA ISSO", "Guardou a recusa por escrito?<br><span class='hl'>Isso conta</span>",
                    "Guarda a data da recusa da seguradora — é dali que o prazo de 1 ano começa a valer de verdade.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_05_papo_corretor_rc_profissional():
    out = os.path.join(CONTENT, "semana-05", "post-05-papo-corretor-rc-profissional")
    photo = p("ref-pexels-doctor.jpg")
    total = 6
    slides = [
        photo_slide(LOGO, photo, "PAPO DE CORRETOR",
                    "O seguro que protege quem<br><span class='hl'>presta serviço</span> — não só quem contrata",
                    "Com fonte. Não é achismo.", 1, total),
        notebook_slide(LOGO, "DADO", "Seguros de Danos e RC<br>não param de <span class='hl'>crescer</span>",
                        [{"label": "Crescimento em 2025", "value": "+7,5%", "highlight": True},
                         {"label": "Prêmios arrecadados", "value": "R$144,5 bi"}],
                        "Dado do setor (CNseg) — RC Profissional é um dos ramos dentro dessa conta que ainda tem pouco corretor de olho.", 2, total),
        notebook_slide(LOGO, "O QUE É", "Protege de <span class='hl'>erro</span>,<br>não só de acidente",
                        [],
                        "Médico, advogado, engenheiro, arquiteto, contador — qualquer profissional que presta serviço técnico pode ser processado por erro ou omissão, mesmo sem culpa grave.", 3, total),
        notebook_slide(LOGO, "SINAL DE MERCADO", "Até o <span class='hl'>Sincor-SP</span><br>lançou o produto",
                        [],
                        "A entidade que representa corretores criou um RC Profissional específico pros próprios associados — sinal de que a demanda é real dentro da categoria.", 4, total),
        notebook_slide(LOGO, "O QUE FAZER COM ISSO", "Pergunte antes de<br>fechar <span class='hl'>outro seguro</span>",
                        [],
                        "Cliente que é profissional liberal (médico, advogado, engenheiro, autônomo com CNPJ) já tem RC Profissional, ou nunca ninguém ofereceu?", 5, total),
        notebook_slide(LOGO, "GUARDA ESSE POST", "Um produto a mais<br>na <span class='hl'>carteira</span>",
                        [], "Manda pra um colega corretor que ainda não oferece RC Profissional pros clientes PJ.", 6, total),
    ]
    for i, html in enumerate(slides, 1):
        make_html_and_render(out, f"slide-{i:02d}", html)
    return out


def build_post_06_teste_domingo(post_01_dir):
    """Teste de domingo: repete o pilar consumidor mais universal da semana
    (Post 1 — mito seguro auto x condutor não declarado), em pasta própria."""
    out = os.path.join(CONTENT, "semana-05", "post-06-teste-domingo-condutor")
    os.makedirs(out, exist_ok=True)
    for i in range(1, 7):
        name = f"slide-{i:02d}.png"
        shutil.copyfile(os.path.join(post_01_dir, name), os.path.join(out, name))
    return out


if __name__ == "__main__":
    p1 = build_post_01_mito_condutor()
    build_post_02_mito_rc_familiar()
    build_post_03_vale_a_pena_equipamentos()
    build_post_04_caso_real_prescricao()
    build_post_05_papo_corretor_rc_profissional()
    build_post_06_teste_domingo(p1)
    print("Lote 5 gerado.")
