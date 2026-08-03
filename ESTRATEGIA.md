# Estratégia — Instituto do Seguro (@institutodoseguro)

Objetivo: ser o maior canal de seguros do Brasil, atendendo DOIS públicos que hoje ninguém
atende junto: consumidor final (massa, motor de crescimento) e corretores (autoridade, nicho
que o @cqcs domina com conteúdo fraco de engajamento).

## Posicionamento
"O canal que explica seguro para quem compra — e para quem vende."
- 80% do conteúdo: consumidor (linguagem simples, ganchos fortes) → é o que traz seguidores
- 20% do conteúdo: corretor (bastidor de mercado, dado técnico) → é o que constrói autoridade
  e rouba a audiência engajada do CQCS

## O que os dados mostraram (2026-07-28)
1. **CQCS (52,9 mil seg.)**: notícia seca = 21 curtidas; caso real com debate = 475 curtidas.
   Conclusão: mesmo público B2B engaja com HISTÓRIA, não com boletim.
2. **Demanda de busca** (padrão repetido em todos os ramos): "vale a pena?",
   "o que cobre?", "quanto custa?" — ninguém responde isso de forma acessível no Instagram.
3. **Algoritmo (ordem de peso)**: tempo de exibição/conclusão → compartilhamentos →
   salvamentos → comentários → curtidas. Otimizar pra compartilhamento e salvamento,
   nunca pra curtida.

## O sistema de conteúdo (lote semanal de 5 posts regulares Seg-Sex + 1 teste de domingo = 6)
| # | Série | Formato | Público | Função no algoritmo |
|---|-------|---------|---------|---------------------|
| 2x | "Mito ou Verdade" / "Isso NÃO é coberto" | Reel | Consumidor | Compartilhamento (choque/alerta) |
| 1x | "Vale a pena?" (um ramo por semana) | Carrossel | Consumidor | Salvamento (referência) |
| 1x | Caso real anonimizado (sinistro: pagou ou negou, e por quê) | Reel | Ambos | Comentário (debate) — formato validado no CQCS |
| 1x | "Papo de Corretor" (bastidor, dado, técnica de venda) | Carrossel | Corretor | Autoridade + nicho B2B |
| 1x | Teste de domingo (repete um dos pilares consumidor acima) | — | Consumidor | Testar se fim de semana performa bem no nicho |

+ Stories diários simples (enquete "mito ou verdade?", caixa de pergunta) — retenção.
As perguntas recebidas viram pauta do pilar 4 (flywheel: audiência gera conteúdo).

## Regras de formato (faceless)
- **Gancho nos 2 primeiros segundos**, sempre com texto na tela (maioria assiste sem som):
  - Padrão-interrupção: "Isso NÃO é coberto pelo seu seguro"
  - Custo escondido: "Você paga por uma cobertura que nunca vai usar"
  - Estatística: "9 em cada 10 sinistros negados são por isso"
- Reels: 15-30s, texto animado + b-roll/imagens, voz sintética PT-BR ou só texto+música
- Carrosséis: template da marca (azul-marinho #122A42 + dourado #C69B4A), 6-8 slides,
  último slide sempre CTA ("Salva pra não esquecer" / "Manda pra alguém que precisa saber")
- Legenda: 1ª linha repete o gancho com palavra-chave (SEO do Instagram indexa legenda)
- Hashtags: 3-5 específicas (#segurodevida #seguroauto...), não 30 genéricas

## SEO do Instagram
- Campo NOME do perfil (pesquisável): mudar para "Instituto do Seguro | Seguros Explicados"
  ou variação com palavra-chave (ex: "seguro auto, vida, saúde")
- Texto alternativo (alt text) preenchido em todo post
- Palavra-chave no início da legenda, não só hashtag

## Sistema visual (2026-07-28, v3 — validado com exemplos reais)
Pesquisa anterior (blog de tendências) só descrevia texto — não bastava. Baixei imagens reais de
posts de contas grandes pra examinar de verdade. Dois padrões vencedores confirmados, diferentes
entre si e ambos muito melhores que gradiente genérico ou "documento antigo":

1. **Foto real + degradê + texto bold** (referência: @nathfinancas, @nathaliaarcuri) — foto de alta
   qualidade em tela cheia, degradê escuro na base pra legibilidade, headline grande em negrito
   por cima, tag pequena de categoria no topo. Usar em: Mito ou Verdade, Caso Real — conteúdo
   narrativo/emocional. Fotos vêm de bancos gratuitos (Pexels), buscadas e baixadas por tema.
2. **Caderno anotado à mão + marca-texto** (referência: @mirna_economirna) — textura de caderno
   espiral, fonte estilo letra à mão, marca-texto amarelo nos números-chave, tabela/dado bem
   visível. Usar em: Vale a pena?, Papo de Corretor — conteúdo com número/dado que precisa gravar.

Motor técnico: HTML/CSS renderizado via Chromium headless (Edge) e capturado em PNG — não mais
Pillow/Python puro (tipografia e efeitos muito superiores).

**Logo/marca**: precisa aparecer com mais destaque em todo post (reconhecimento de marca,
principalmente importante agora que a conta é nova e o conteúdo pode ser compartilhado fora do
Instagram sem crédito automático). Mantém o escudo azul-marinho + "IS" dourado como âncora fixa
(bom porque não muda enquanto o fundo varia entre foto/gradiente/caderno), mas em tamanho maior
e posição mais visível, não só um selo pequeno no rodapé.

## Ritmo de aprovação semanal (2026-07-28)
Usuário não quer aprovar publicação todo dia. Modelo adotado:
- **Domingo 18h**: tarefa agendada gera o lote da semana seguinte (`instituto-do-seguro-lote-semanal`)
- **Segunda-feira 13:30**: lembrete automático por WhatsApp via CallMeBot
  (`instituto-do-seguro-lembrete-segunda`) avisando que o lote está pronto pra revisão
- **Usuário revisa e aprova uma vez** (mensagem tipo "aprovado" nesta conversa)
- **Depois da aprovação**: criar uma tarefa agendada `fireAt` (uma por post, no dia/hora exato)
  que roda `scripts/publish_buffer.py` (feed + `--story`) com a legenda já definida — sem pedir
  confirmação de novo, porque a aprovação já foi dada pro conteúdo específico daquele lote.
- Credenciais CallMeBot em `config/.env` (CALLMEBOT_PHONE, CALLMEBOT_APIKEY).
- **Preferência confirmada (2026-07-28): avisos vão por WhatsApp**, não só o lembrete de
  segunda — toda tarefa de publicação automática (fireAt) também manda uma mensagem de
  confirmação (sucesso ou erro) via CallMeBot ao terminar.
- **Teste em andamento**: adicionar 1 post de domingo (pilar consumidor, nunca "papo de
  corretor") a partir do próximo lote, pra testar se fim de semana performa bem pro nosso
  nicho — decidir com dado real do Buffer analytics depois de algumas semanas, não achismo.
  Sábado não entra (sinal fraco em todas as fontes pesquisadas).

## Processo semanal (institucionalizado a partir de agora)
Antes de gerar cada lote semanal novo:
1. Pesquisar 1-2 exemplos reais de alto engajamento no nicho ou correlatos (baixar imagem de
   verdade, não confiar só em descrição de blog).
2. Checar se algum padrão novo apareceu desde o último lote — testar, não descartar por hábito.
3. Cada post precisa ter um objetivo claro antes de ser produzido (educar, gerar debate, ser
   referência salvável, gerar lead) — nunca produzir "postagem de preencher calendário" sem função.
4. Legendas seguem o framework abaixo, não texto genérico.

## Framework de legenda (atualizado 2026-07-28, com pesquisa de gatilhos)
- **Linha 1 é SEO, não é só gancho**: em 2026 a 1ª linha da legenda pesa mais que hashtag pro
  alcance — precisa ter a palavra-chave do tema, não só ser "chamativa" (ex: "Seguro auto vale a
  pena?" já tem "seguro auto" logo de cara).
- **Gatilho de salvamento explícito**: gente salva quando sente que a informação é densa demais
  pra guardar de cabeça, mas tem medo de perder. CTA funciona melhor sendo literal:
  "Essa lista é grande demais pra decorar — salva pra consultar depois" bate mais que "salva aí".
- **Pergunta de fechamento precisa gerar resposta longa, não sim/não**: comentário com frase
  completa pesa mais no algoritmo que "1,2,3" ou "sim". Preferir "Qual dessas 3 você não sabia, e
  o que rolou?" a "Você sabia disso?".
- Sem enrolação de "oi eu sou..." — vai direto ao valor.
- Hashtags: 3-5 específicas do tema, nunca 20 genéricas.
- (Achado à parte, não aplicado ainda): legendas longas tipo microblog voltaram com força em 2026
  porque prendem no loop — vale testar num post por semana quando tivermos mais dado próprio.

## Feed → Story: por que fazer sempre os dois (2026-07-28)
Feed e Stories têm algoritmos separados que recompensam sinais diferentes:
- **Feed**: otimizado pra alcance (pode chegar a quem não segue ainda). Recompensa
  salvamento/compartilhamento/comentário longo.
- **Stories**: NÃO serve pra alcançar desconhecido — serve pra aprofundar vínculo com quem já
  segue. O que pesa é interação privada (responder, votar, DM), não visualização pública.
  Dado real: 1 em cada 5 Stories gera uma DM; elementos interativos aumentam retenção em até 35%.
  Postar Stories em excesso sem propósito é penalizado ("ruído cognitivo") — 1 Story com intenção
  clara por post, não vários soltos.

**Limite técnico confirmado (2026-07-28)**: elementos interativos de Story (enquete, caixa de
pergunta) E também o card de "compartilhar post pro Story" (que é só um link de volta pro post,
não o carrossel inteiro replicado) NUNCA podem ser publicados via API — bloqueio da própria
Meta, vale pra qualquer ferramenta (Buffer, Metricool, todas). Sempre exige ação manual no app,
sem exceção.

**Decisão final (2026-07-28): Story automático, versão simples.** Usuário pediu pra manter
automático mesmo sem o link/adesivo (que é impossível via API). Solução adotada: gerar um
"card" de Story (1080x1920, `scripts/templates.py::story_card`) com o gancho do post + selo
"Post completo no feed" — sem link clicável de verdade, só aviso visual. Publicado via
`scripts/publish_buffer.py --story` logo após o Feed (metadata.instagram.type=story,
shouldShareToFeed=false, imagem única, sem carrossel). Card gerado por
`scripts/build_stories_semana01.py` (adaptar pra gerar por lote nos próximos).
Quando a conta tiver uma base maior (referência: uns 500-1.000 seguidores), o usuário ajusta
manualmente pra usar o "compartilhar post pro Story" nativo com adesivo de enquete/pergunta
(mais engajamento, mas exige o passo manual de ~1 min por post).

**Bug corrigido (2026-07-28)**: o primeiro Story publicado falhou com erro 400 silencioso —
Buffer retornava "sending"/"sent" na hora, mas o status real (consultado depois via API) era
"error": "Failed to publish Instagram media: Request failed with status code 400". Causa raiz
(confirmada na documentação oficial da Meta): a API do Instagram exige **proporção de imagem
entre 4:5 e 1.91:1 e formato JPEG** pra qualquer mídia, inclusive Stories — nosso card estava em
9:16 (tela cheia) e PNG. Corrigido: `story_card` agora gera 1080x1350 (4:5, igual aos slides do
Feed) e `build_stories_semana01.py` converte pra JPEG antes de publicar. **Lição pro futuro**:
sempre conferir o status real do post via query direta na API alguns segundos depois de
publicar — "sending"/"sent" na resposta imediata do createPost NÃO garante que deu certo.

## Reels — expectativa realista
Não tenho gerador de vídeo nativo (não é IA de vídeo tipo Sora/Runway). O que é possível construir:
roteiro completo + storyboard, e futuramente montagem tipo slideshow (imagens/clipes de banco +
legenda + música) via ffmpeg, se decidirmos investir nisso. Vamos endereçar quando chegarmos lá —
por enquanto o foco é carrossel, que já cobre boa parte do potencial de alcance.

## Benchmark de contas de alto crescimento (2026-07-28)
Analisadas 3 contas indicadas pelo usuário (@thiagoconceroficial 1mi seg., @marcelaluzzio 269mil
seg., @brun0gpt): o mecanismo de crescimento em comum, em praticamente todo post de alto
engajamento, é **"comenta [palavra-chave] que eu te mando no direct"** — entrega real (aula,
checklist, comandos) via automação de DM disparada por comentário. Post do Thiago Concer:
989 comentários só com a palavra "Aula". Isso não é isca vazia — é lead magnet real automatizado.
**Pré-requisito não resolvido ainda**: precisa de uma ferramenta de automação de DM (ex: Manychat)
conectada à conta — sem isso, usar esse gatilho significa responder manualmente, o que contraria
o objetivo de baixo esforço. Ver tarefa pendente antes de usar esse CTA em qualquer post.

## Aceleradores de crescimento
1. **Trend-jacking**: seguro no noticiário (carro de luxo batido, enchente, incêndio) →
   post-reação em até 24-48h traduzindo pro consumidor. O CQCS noticia pra corretor;
   nós traduzimos pra todo mundo — mesma pauta, alcance 10x.
2. **Collabs (post em coautoria)**: criadores de finanças pessoais/educação financeira —
   o post aparece pras duas audiências. Ativar a partir de ~1k seguidores.
3. **Responder TODO comentário na 1ª hora** (sinal forte pro algoritmo + comunidade).
   Único trabalho diário do usuário: 5-10 min pelo celular.
4. **Comentário fixado com pergunta** em todo post (puxa debate).

## Operação "no automático" (fluxo real, com papéis)
1. **Geração (automática)** — Claude gera o lote semanal: 5 roteiros + legendas + artes
   (carrosséis via script Python com template da marca) → salvos em `content/semana-NN/`
2. **Revisão (humana, ~10 min/semana)** — usuário lê, aprova ou pede ajuste. Obrigatória:
   conteúdo regulado (SUSEP) + política de aprovação antes de publicar.
3. **Agendamento (semi-automático, ~10 min/semana)** — lote aprovado agendado no Metricool
   (plano Free publica sozinho no horário; API só no pago, então o input é via painel).
4. **Interação (humana, 5-10 min/dia)** — responder comentários/DMs pelo celular.
5. **Análise (automática, mensal)** — ler métricas do Metricool, identificar top/flop,
   ajustar a fórmula do lote seguinte.

Piso honesto de tempo do usuário: ~30-40 min/semana + 5-10 min/dia de interação.
Publicação 100% autônoma sem revisão: não — por política de aprovação e por risco regulatório.

## Horários e calendário semanal (ajustado 2026-08-03, testar e ajustar com dados)
Semana de postagem vai de segunda a domingo (sábado pulado) — 6 posts/semana:

| Dia | Horário | Tipo |
|---|---|---|
| Segunda | 12h | regular (movido de 19h pra 12h em 2026-08-03 — ver motivo abaixo) |
| Terça | 12h | regular |
| Quarta | 19h | regular |
| Quinta | 12h | regular |
| Sexta | 19h | regular |
| Sábado | — | sem post (sinal fraco em todas as fontes pesquisadas) |
| Domingo | 11h | teste — pilar consumidor, NUNCA papo de corretor |

**Por que Segunda mudou de 19h pra 12h:** o Buffer (plano grátis) limita a conta a 10 posts
agendados simultaneamente. O fluxo é: reunião de aprovação de manhã/começo da tarde de segunda →
agenda a semana toda no Buffer logo em seguida. Com o post de Segunda ainda marcado pras 19h,
o post de Segunda da semana ANTERIOR ainda estava "scheduled" (não tinha saído) na hora de
agendar a semana nova, ocupando 2 vagas (post + story) e travando o agendamento dos últimos itens
da semana. Com Segunda às 12h, o post da semana anterior já saiu antes da reunião de aprovação,
liberando as vagas a tempo.

Revisar após 1 mês de métricas reais do Buffer, principalmente o resultado do teste de domingo.

## Compliance (inegociável)
- Post fixado deixando claro: iniciativa privada de conteúdo educativo, sem vínculo com
  órgãos reguladores (por causa do nome "Instituto").
- Nunca recomendar seguradora específica em conteúdo de consumidor; nunca prometer
  resultado; enquadramento sempre educativo ("procure um corretor" como CTA aceitável).

## Metas e expectativa honesta
- 1.000 seguidores: prova de conceito (~2-3 meses de consistência)
- 10.000: autoridade consolidada, ativar collabs e monetização inicial
- 50.000+: paridade com CQCS — horizonte realista de 12-24 meses orgânico
- Métrica-guia semanal: compartilhamentos + salvamentos por post e conversão
  visita de perfil → seguidor. Curtida é vaidade, não guia decisão.
