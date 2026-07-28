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

**O que continua local (por enquanto):** a geração semanal de conteúdo (domingo 18h,
`mcp__scheduled-tasks`), porque depende de renderização via Chromium headless (Windows) — mover
isso pra nuvem exigiria instalar um navegador no ambiente Linux da nuvem, não foi feito ainda.
**Por isso a tarefa de geração agora faz `git commit` + `git push` ao final** — as rotinas de
nuvem só enxergam o que estiver no GitHub, não o disco local.

Credenciais (Buffer, CallMeBot) são passadas embutidas no prompt de cada rotina de nuvem (não há
outro jeito de injetar segredo nesse mecanismo) — aceitável pra uso pessoal, mas vale saber que
ficam armazenadas do lado do Anthropic associadas à rotina.

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
