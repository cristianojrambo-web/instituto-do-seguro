# Setup — Instituto do Seguro (automação de publicação no Instagram)

Marca: **Instituto do Seguro** | Usuário: **@institutodoseguro**
(nome verificado livre no Instagram e sem marca registrada conflitante no INPI em 2026-07-27)

E-mail da conta: `institutodosegurobr@gmail.com`

Estas partes só você pode fazer, porque exigem login nas suas contas.
Depois disso, a última parte (publicação) já está pronta em `scripts/publish.py`.

## PARTE 0 — Criar a conta no Instagram ✅ CONCLUÍDA (2026-07-27)
- Conta criada: @institutodoseguro
- Logo aplicada: `content/logo.png` (escudo azul-marinho + monograma "IS" dourado)
- Bio aplicada:
  ```
  Referência em seguros no Brasil
  Especialista traduzindo seguro pra linguagem simples
  👇 Manda sua dúvida nos comentário
  ```
- PENDENTE: adicionar um aviso de que é iniciativa privada, sem vínculo com órgãos reguladores (por causa do nome "Instituto") — decidido (2026-07-28) NÃO colocar isso no post de apresentação (usuário achou desnecessário/óbvio); colocar em um destaque de Stories em vez disso

## PARTE 1 — Conta profissional + Página do Facebook ✅ CONCLUÍDA (2026-07-27)
- Conta virou profissional (categoria: Corretor de seguros)
- Página do Facebook criada: "Instituto do Seguro" (logo aplicada, 0 seguidores)
- Página conectada ao Instagram @institutodoseguro via Configurações da Página → Permissões → Contas vinculadas → Instagram
- Nota: o admin da Página é o perfil pessoal do Facebook do usuário (não aparece publicamente vinculado à marca)

## PLANO C (ATIVO, 2026-07-28) — Buffer API, substitui o Metricool
Motivo da troca: usuário queria automação de verdade sem custo mensal. Metricool grátis exigia
upload manual (API só no plano pago, US$53-67/mês). Pesquisamos alternativas: Buffer tem API
**incluída no plano grátis** (1 chave, 3.000 requisições/mês) e suporta agendamento direto de
carrossel no Instagram (sem "lembrete"/cópia manual), até 10 imagens por post.

**Como funciona:**
- Conta Buffer criada e conectada (Facebook + Instagram) pelo usuário em buffer.com
- Chave de API salva em `config/.env` (`BUFFER_API_KEY=...`)
- Canal Instagram ID: `6a68eeba4b2d03035f58a0e6` (hardcoded em `scripts/publish_buffer.py`)
- A API do Buffer não hospeda mídia — cada imagem é subida temporariamente pro
  litterbox.catbox.moe (anônimo, sem conta, grátis) só o tempo de o Buffer buscar/processar
- Script: `scripts/publish_buffer.py --post <pasta> --caption "..." [--due ISO8601] [--draft]`
  - Sem `--due`: publica imediatamente (shareNow)
  - Com `--due`: agenda pro horário (schedulingType=automatic, publica sozinho, sem notificação)
  - Com `--draft`: salva como rascunho no Buffer pra revisão, não publica — usar sempre pra
    testar antes de publicar de verdade
- **Toda publicação real (sem --draft) exige confirmação explícita do usuário antes de rodar**
  (política de permissão — publicar é ação pública e irreversível)
- Primeiro post real (Apresentação) publicado com sucesso em 2026-07-28

Buffer supera o Metricool e o Upload-Post (que tinha cap de 10/mês) pro nosso volume de 4-5
posts/semana. Postiz também foi avaliado — só é grátis se auto-hospedado (exige servidor
próprio rodando sempre), não valeu a complexidade.

**Limite descoberto em 2026-08-03**: o plano grátis do Buffer permite no máximo **10 posts
agendados simultaneamente** na conta toda (feed + Stories contam juntos). Com 6 posts/semana
(12 itens contando Stories), dá pra travar se o agendamento da semana nova acontecer antes do
último post da semana anterior sair do ar. Mitigado movendo o post de Segunda de 19h pra 12h
(ver ESTRATEGIA.md) — assim ele sai antes da reunião de aprovação, liberando vagas a tempo de
agendar a semana inteira de uma vez.

As Partes 1-4 abaixo (Metricool e API direta da Meta) ficam registradas como histórico —
não são mais o caminho ativo.

## PLANO D (ATIVO, 2026-07-28) — Migração pra nuvem (RemoteTrigger)
Motivo: as tarefas agendadas locais (`mcp__scheduled-tasks`) só rodam com o computador ligado e
o app aberto — se o PC estivesse desligado num horário de post, ele só sairia quando o usuário
ligasse de novo. Solução: repositório público no GitHub
(https://github.com/cristianojrambo-web/instituto-do-seguro) + rotinas de nuvem (RemoteTrigger)
que clonam o repo e rodam independente do computador do usuário.

**O que roda na nuvem agora:**
- Lembrete de domingo 17:30 BRT (`30 20 * * 0` UTC) — WhatsApp lembrando de ligar o PC antes da geração das 18h (que ainda é local)
- Lembrete de segunda-feira (WhatsApp via CallMeBot) — cron `30 16 * * 1` UTC (13:30 BRT)
- As 4 publicações do Lote 1 desta semana (post + story via `scripts/publish_buffer.py`), cada
  uma como rotina `run_once_at` no horário exato, lendo o conteúdo do repositório

## PLANO E (ATIVO, 2026-08-03) — Geração semanal também migrada pra nuvem
Motivo: na semana de 2026-08-02/03, o lembrete de domingo (17:30 BRT) disparou normalmente, mas
o usuário não recebeu a mensagem (falha de entrega do WhatsApp/CallMeBot) — sem o aviso, o PC
não foi ligado, e a tarefa local de geração simplesmente não rodou no horário (só rodou tarde,
segunda de manhã, sem gerar nada, sem avisar). Causa raiz: a geração dependia do PC ligado
(Plano D deixava isso de fora por achar que precisava de navegador só existente no Windows).

**Testado e confirmado em 2026-08-03**: o ambiente de nuvem (RemoteTrigger) já tem Chromium
pré-instalado via Playwright em `/opt/pw-browsers` — só precisa da flag `--no-sandbox` (container
roda como root). `scripts/render_html.py` foi adaptado pra detectar o ambiente sozinho (Edge no
Windows local, Chromium na nuvem) — sem regressão no fluxo local, testado nos dois.

**O que mudou:**
- Nova rotina de nuvem `instituto-do-seguro-lote-semanal-nuvem`, cron `0 21 * * 0` UTC (domingo
  18h BRT) — mesmas instruções de pesquisa/geração/fact-checking da tarefa local antiga, roda
  `pip install -r requirements.txt`, cria `config/.env` embutido, gera o lote e faz commit+push.
  Manda WhatsApp de início (diagnóstico de falha no meio) e de conclusão (sucesso ou erro).
- Tarefa local `instituto-do-seguro-lote-semanal` (`mcp__scheduled-tasks`) **desativada**
  (`enabled: false`, não deletada — dá pra reativar se precisar).
- Lembrete de domingo "ligar o PC" (`instituto-do-seguro-lembrete-domingo-pc`) **desativado** —
  deixou de fazer sentido, a geração não depende mais do PC ligado.
- Lembrete de segunda-feira (`instituto-do-seguro-lembrete-segunda`) continua ativo, mas agora
  verifica de fato se o lote foi gerado (data do último commit na pasta `semana-NN` mais recente)
  antes de avisar — evita confiar cegamente que "deu tudo certo".

**O que ainda é local:** só a reunião de revisão/aprovação de segunda-feira em si (o usuário abre
o Claude Code e conversa) — isso é inerentemente humano, não dá (nem faz sentido) automatizar.

## PLANO F (ATIVO, 2026-08-04) — Check-in diário de publicação por WhatsApp
Motivo: a confirmação por WhatsApp depois que um post realmente sai do ar tinha sido combinada
várias vezes, mas nunca virou uma rotina permanente — só existiam avisos manuais enviados nessa
conversa. Criada a rotina de nuvem `instituto-do-seguro-checkin-diario`, cron `0 0 * * 1-6` UTC
(21h BRT, todo dia exceto sábado — cobre Seg/Ter/Qua/Qui/Sex/Dom, que são os dias com post).
Ela consulta o Buffer pelos posts com `dueAt` nas últimas ~30h, confere o `status` real
(`sent`/`error`), e manda um resumo por WhatsApp — só avisa se havia algo esperado pra aquele
dia, e destaca claramente se algo falhou (`status: error`).

Credenciais (Buffer, CallMeBot) são passadas embutidas no prompt de cada rotina de nuvem (não há
outro jeito de injetar segredo nesse mecanismo) — aceitável pra uso pessoal, mas vale saber que
ficam armazenadas do lado do Anthropic associadas à rotina.

## PLANO G (achado, 2026-08-09) — bloqueio de rede a bancos de imagem no ambiente de nuvem
Na geração do lote 3 (primeira rodada 100% na nuvem via RemoteTrigger), `images.pexels.com` e
`images.unsplash.com` retornaram 403 (bloqueio de política de egress da rede do ambiente) tanto
via `curl` direto quanto via `WebFetch` — diferente do ambiente local, que baixa fotos novas do
Pexels normalmente a cada lote. Não é um erro pontual: o endpoint de status do proxy confirma
"policy denial" pros dois domínios. Impacto: não dá pra baixar fotos novas por tema toda semana
enquanto essa política não mudar — a rotina de nuvem precisa reaproveitar fotos já commitadas em
`content/assets/` (mesmo que o tema não seja um encaixe perfeito) ou usar o estilo caderno
(`notebook_slide`, que não depende de foto) nos posts sem uma foto adequada já disponível.
Pendência pro usuário: liberar esses domínios na política de egress do ambiente de nuvem (se
possível) para retomar fotos novas por tema, ou manter um estoque maior de fotos pré-baixadas
localmente e commitadas com antecedência, cobrindo os ramos ainda não fotografados (viagem,
empresarial, previdência).

## PLANO B (histórico, substituído pelo Plano C) — Metricool em vez da API direta
Motivo da troca (2026-07-28): a verificação de conta de desenvolvedor da Meta (Parte 2 abaixo)
travou num bug conhecido e sem solução publicada (SMS de verificação nunca chega — confirmado
em fóruns oficiais da Meta e Reclame Aqui, sem resposta da Meta). Decidido seguir por
Metricool (plano Free: 1 marca, publicação automática até 50 posts/mês) em vez de insistir.

Diferença no fluxo de publicação: como a API do Metricool só existe em planos pagos, o
agendamento no plano Free é feito pela interface deles. Fluxo adotado: conteúdo gerado por IA
→ revisão em lote semanal do usuário → agendamento feito no painel do Metricool (por mim, via
navegador, ou pelo usuário direto) → publicação automática pelo Metricool no horário certo.

As Partes 2-4 abaixo (API direta da Meta) ficam registradas pra retomar no futuro, se quiser
tentar de novo ou se a Meta corrigir o bug — mas não são o caminho ativo agora.

## PARTE 2 — App em developers.facebook.com (PAUSADO — ver Plano B acima)
Fluxo atual (baseado em "casos de uso", 2026):
1. Acesse https://developers.facebook.com/apps/creation/
2. **Detalhes do app**: nome (ex: "Instituto do Seguro - Automação") + e-mail de contato → Avançar
3. **Casos de uso**: selecione **"Gerenciar mensagens e conteúdo no Instagram"** (já traz as permissões `instagram_business_content_publish`, `instagram_content_publish`, `pages_show_list`, `pages_read_engagement`, etc.) → Avançar
4. **Empresas**: escolha **"Ainda não quero me conectar a um portfólio empresarial"** (mais simples por enquanto) → Avançar
5. **Requisitos**: revise → Avançar
6. **Visão geral**: revise e clique em **"Ir para o painel"**
7. No painel do app, vá em **Configurações do app → Básico** e anote em local seguro (NÃO envie por chat):
   - **App ID**
   - **App Secret**

## PARTE 3 — Token de acesso de longa duração
1. Em https://developers.facebook.com/tools/explorer, selecione seu app, gere um **User Token** com as permissões:
   `instagram_basic`, `instagram_content_publish`, `pages_show_list`, `pages_read_engagement`, `business_management`
2. Troque esse token de curta duração por um de **60 dias** (endpoint `oauth/access_token` com `grant_type=fb_exchange_token`) — evita ficar renovando toda hora.
3. Descubra o **Instagram Business Account ID** (via `GET /me/accounts` depois `GET /{page-id}?fields=instagram_business_account`).
4. Salve tudo em `config/.env` (arquivo local, nunca sobe pra lugar nenhum):
   ```
   IG_ACCESS_TOKEN=...
   IG_BUSINESS_ACCOUNT_ID=...
   ```

## PARTE 4 — já está pronta
Ver `scripts/publish.py`. Assim que o `.env` estiver preenchido, rode:
```
python scripts/publish.py --image content/exemplo.jpg --caption "teste"
```
