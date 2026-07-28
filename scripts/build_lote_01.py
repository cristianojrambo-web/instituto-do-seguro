"""Gera as artes do Lote 1 (5 posts) em content/semana-01/."""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from make_carousel import build_carousel  # noqa: E402

POSTS = {
    "post-00-apresentacao": [
        {"kicker": "BEM-VINDO", "title": "Instituto do Seguro", "body": ""},
        {"title": "Seguro de todos os ramos,\nexplicado sem segurês", "body": ""},
        {"title": "Por quem trabalha\ncom isso todo dia", "body": "Traduzindo o mercado de seguros pra linguagem simples — pra quem compra e pra quem vende."},
        {"title": "Aqui é pra quem\ncompra seguro", "body": "E pra quem vende também. Consumidor e corretor, no mesmo lugar."},
        {"title": "Toda semana:", "body": "Mitos, casos reais e as perguntas que você sempre teve sobre seguro.", "cta": "Segue e ativa o sininho"},
    ],
    "post-01-vale-a-pena-auto": [
        {"kicker": "VALE A PENA?", "title": "Seguro Auto", "body": ""},
        {"title": "O que realmente cobre", "body": "Colisão, roubo, furto e incêndio são o básico. Mas tem 3 coisas que quase ninguém lê no contrato."},
        {"title": "1. Carro reserva", "body": "Nem toda apólice inclui. Sem isso, você fica sem carro durante o reparo — às vezes semanas."},
        {"title": "2. Vidros e faróis", "body": "Muita gente acha que é automático. Na maioria das apólices, é cobertura à parte."},
        {"title": "3. Terceiros (RCF-V)", "body": "O seguro cobre o SEU carro. Bater no carro de outra pessoa exige cobertura de responsabilidade civil separada."},
        {"title": "Então, vale a pena?", "body": "Sim — mas só se você souber exatamente o que está (e o que não está) na sua apólice.", "cta": "Salva pra revisar sua apólice"},
    ],
    "post-02-mito-enchente": [
        {"kicker": "MITO OU VERDADE", "title": "Seguro de carro\ncobre enchente?", "body": ""},
        {"title": "VERDADE.", "body": "Se você tiver cobertura compreensiva (o \"seguro total\")."},
        {"title": "O que já vem incluso", "body": "Colisão, incêndio, roubo, furto E danos por fenômenos da natureza — enchente e alagamento por água doce já contam como padrão, não é opcional à parte."},
        {"title": "A pegadinha", "body": "Só não cobre água do mar, e não cobre se você forçar a passagem por uma via já alagada — isso conta como agravamento de risco."},
        {"title": "Na próxima chuva forte", "body": "Desligue o carro se a água subir, não tente atravessar. Sem cobertura compreensiva, seu carro não tem essa proteção — RCF isolado cobre só danos a terceiros, nunca o seu veículo.", "cta": "Salva antes da próxima chuva forte"},
    ],
    "post-03-caso-real": [
        {"kicker": "CASO ILUSTRATIVO", "title": "O sinistro que quase\nnão foi pago", "body": ""},
        {"title": "O que aconteceu", "body": "Um segurado teve perda total do carro após um acidente. A seguradora inicialmente negou o pagamento."},
        {"title": "O motivo da negativa", "body": "Ele tinha alterado o veículo (som automotivo) e não informou a seguradora — mudança de risco não declarada."},
        {"title": "Por que isso importa", "body": "Pelo Código Civil (art. 768-769), agravar o risco sem avisar a seguradora pode reduzir ou anular a indenização."},
        {"title": "A lição", "body": "Qualquer modificação no carro precisa ser informada. Esconder isso pode custar caro na hora do sinistro.", "cta": "Salva e revisa sua apólice"},
    ],
    "post-04-papo-corretor": [
        {"kicker": "PAPO DE CORRETOR", "title": "2 dados que valem\nmais que curso de vendas", "body": ""},
        {"title": "1. A hora de ouro", "body": "42% dos clientes que não renovam o fariam se a cobertura fosse revista pras necessidades atuais deles (McKinsey, 2024). Renovação não é cobrança de boleto — é a melhor chance de revisão consultiva."},
        {"title": "2. Indicação > anúncio", "body": "84% dos consumidores confiam mais em indicação de amigos e família do que em qualquer propaganda (Nielsen). Peça indicação ativamente — não espere ela acontecer sozinha."},
        {"title": "Guarda esse post", "body": "Vale mais que a maioria dos treinamentos de venda por aí.", "cta": "Manda pra um corretor que precisa ler isso"},
    ],
}


def main():
    for slug, slides in POSTS.items():
        paths = build_carousel(f"semana-01/{slug}", slides)
        print(f"{slug}: {len(paths)} slides gerados")


if __name__ == "__main__":
    main()
