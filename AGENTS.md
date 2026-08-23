# AGENTS.md — Schema da wiki-vinhedo (Alma Gerais)

Este é o arquivo de configuração que transforma o agente em um **mantenedor disciplinado da wiki**,
e não em um chatbot genérico. Leia este arquivo inteiro antes de qualquer operação.

Padrão de referência: [LLM Wiki (Karpathy)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

---

## 1. Papéis e camadas

- `raw/` — **fontes brutas, imutáveis**. Você lê, **nunca edita nem apaga**. É a fonte da verdade.
- `raw/publicacoes/` reúne as publicações curadas pelo time, sem subdivisões temáticas. Essa coleção
  local é uma base preferencial, mas **não limita a pesquisa**: o agente tem liberdade para buscar
  conhecimento externo sempre que isso ajudar a responder, interpretar ou recomendar.
- `wiki/` — **conhecimento que você gera e mantém**. Você é o dono desta camada.
- `dados-vivos/` — **documentação de acesso** às APIs vivas (clima via WS Clima; gestão da vinícola
  via InnoVint/Sutter). Aqui ficam playbooks de consulta, IDs da Alma Gerais e exemplos HTTP
  reutilizáveis — **não** a documentação oficial completa (essa fica no link externo).
  **Não** copie dados crus das APIs para o repositório; consulte em tempo real e **arquive apenas
  as sínteses** na `wiki/`.
- `AGENTS.md` — este schema. Coevolui com o time.

Navegação: `index.md` (catálogo de conteúdo) e `log.md` (histórico cronológico da wiki).

---

## 2. Idioma e escopo

- **Todo o conteúdo em português.** Nomes de pastas, arquivos e páginas em português, sem acentos e
  em `kebab-case` (ex.: `sao-geraldo.md`, `fitossanidade.md`).
- Esta wiki é **exclusiva da Alma Gerais**. Não generalizar para "template replicável".
- **Foco atual: apenas Macaia** (`macaia`). A estrutura é **multi-local** por design (campos
  `local`/`locais`, pasta `wiki/locais/`). **São Geraldo** (`sao-geraldo`) é expansão futura: quando
  entrar, basta criar `wiki/locais/sao-geraldo.md` e incluir o slug nos frontmatters — nada mais muda.

---

## 3. Regra de ouro: FATO ≠ INTERPRETAÇÃO

Este é o princípio mais importante da wiki.

- **Fatos** (o que aconteceu, quando, onde) vivem em `wiki/eventos/`, `wiki/safras/` e nas páginas
  de entidade. Nunca embuta causa em um fato.
- **Interpretações** (por que pode ter acontecido, o que se relaciona com o quê) vivem em
  `wiki/correlacoes/` e `wiki/hipoteses/`. Toda interpretação **deve**:
  - citar os eventos/fontes datados que a sustentam;
  - explicitar a **defasagem temporal** quando houver (ex.: "~2 meses depois");
  - registrar um **nível de confiança** (`baixa` | `media` | `alta`);
  - deixar claro que **correlação não implica causalidade**.

Nunca contamine o registro factual com suposição.

---

## 4. Ancoragem temporal (obrigatória)

Para o agente conseguir ligar os pontos no tempo ("isto hoje pode ter relação com aquilo de 2 meses
atrás"), **toda página factual carrega âncoras temporais** no frontmatter:

- `data` (ou `data_inicio` + `data_fim` para períodos), no formato `AAAA-MM-DD`.
- `safra` (ano da safra).
- `estagio_fenologico` — âncora tão importante quanto a data. Valores: `dormencia`, `brotacao`,
  `floracao`, `pegamento`, `crescimento-baga`, `veraison`, `maturacao`, `colheita`, `pos-colheita`.
- `local`, `quadra(s)`, `variedade(s)` quando aplicável.

Nomes de arquivos de evento **começam pela data** para ordenarem sozinhos no tempo:
`AAAA-MM-DD-local-descricao-curta.md`.

---

## 5. Frontmatter por tipo de página (YAML)

Sempre inicie páginas com frontmatter YAML. Campos comuns: `tipo`, `titulo`, `tags`, `fontes`
(lista de caminhos em `raw/` ou `dados-vivos/` e/ou URLs externas), `atualizado_em`.

**Evento** (`wiki/eventos/`):
```yaml
---
tipo: evento
categoria: clima        # clima | manejo | analise | fitossanidade | qualidade | colheita | observacao
data: 2026-06-15
local: macaia
quadras: [q3]
variedades: [syrah]
safra: 2026
estagio_fenologico: maturacao
tags: [geada]
fontes: [raw/registros-ciclos-videira/2026-06-15-macaia.md]
atualizado_em: 2026-06-16
---
```

**Quadra** (`wiki/quadras/`): `tipo: quadra`, `local`, `variedades`, `porta_enxerto`, `ano_plantio`,
`area_ha`, `espacamento`, `sistema_conducao`.

**Variedade** (`wiki/variedades/`): `tipo: variedade`, `locais`, `quadras`, `tags`.

**Safra** (`wiki/safras/`): `tipo: safra`, `ano`, `locais`.

**Vinho** (`wiki/vinhos/`): `tipo: vinho`, `variedades`, `safras`.

**Tema** (`wiki/temas/`): `tipo: tema`.

**Correlação** (`wiki/correlacoes/`): `tipo: correlacao`, `defasagem`, `confianca`, `eventos: [...]`.

**Hipótese** (`wiki/hipoteses/`): `tipo: hipotese`, `status` (`aberta` | `em-teste` | `apoiada` |
`refutada`), `confianca`.

**Recomendação** (`wiki/recomendacoes/`): `tipo: recomendacao`, `origem` (`agronomica` |
`enologica` | `agente`), `status` (`questionada` | `validada` | `sugerida` | `aplicada`).

---

## 6. Ligações (grafo)

- Use wikilinks `[[nome-do-arquivo]]` (compatível com Obsidian) para conectar páginas.
- **Ligações bidirecionais**: ao criar uma correlação/hipótese, adicione um link de volta a partir
  das páginas de quadra/variedade/safra/evento envolvidas.
- Toda página nova entra no `index.md`.

---

## 7. Estrutura de pastas

```
raw/            fontes brutas imutáveis (espelha as fontes do caderno)
  publicacoes/  todas as publicações, sem subdivisões temáticas
  fichas-tecnicas/
    comercial/  fichas de produtos comerciais
    biologicos/ fichas de produtos biológicos
  analises/     análises de solo, planta e outras matrizes
  qualidade-uva/    resultados físico-químicos, sanitários e sensoriais
  qualidade-vinho/  resultados de flor, prensa e outras avaliações
  consultoria/  relatórios de consultoria atualmente agronômica
  registros-manejo/ registros datados das operações de manejo
  registros-ciclos-videira/ registros datados dos ciclos e estágios fenológicos
  mapa-plantio/ mapas, fotos de drone, variedades plantadas
  assets/       imagens/anexos
wiki/
  overview.md   síntese geral
  locais/       macaia (São Geraldo = expansão futura)
  quadras/      páginas por quadra/talhão
  variedades/   páginas por variedade
  safras/       hub temporal: uma página por ano
  vinhos/       páginas por produto
  temas/        solo, clima, irrigacao, nutricao, fitossanidade, poda-desfolha...
  eventos/      linha do tempo factual e datada
  correlacoes/  correlações descobertas (com defasagem e confiança)
  hipoteses/    hipóteses em acompanhamento
  recomendacoes/ recomendações questionadas | validadas | sugeridas
dados-vivos/    estacao-meteorologica.md | gestao-vinicola.md | queries/
tools/          scripts opcionais (busca/ingestão) quando a wiki crescer
```

Arquivos `_modelo-*.md` são **gabaritos**; copie-os ao criar páginas novas.

---

## 8. Operações

### Ingerir
1. Leia a fonte em `raw/` (ou puxe o registro de voz via MCP Granola e salve em
   `raw/registros-manejo/` ou `raw/registros-ciclos-videira/`, conforme o conteúdo).
2. Discuta os pontos-chave com o humano.
3. Se for um fato datado, crie/atualize a página em `wiki/eventos/` com ancoragem temporal.
4. Atualize as páginas de entidade afetadas (quadra, variedade, safra, vinho) e de tema.
5. Adicione a linha do tempo da `safra` correspondente.
6. Proponha correlações/hipóteses candidatas em suas pastas (sem alterar os fatos).
7. Atualize `index.md` e adicione entrada em `log.md`.

### Consultar
1. Leia primeiro o `index.md` para achar páginas relevantes; depois aprofunde.
2. Para perguntas temporais, varra `wiki/eventos/` por data/estágio fenológico e a linha do tempo
   da(s) safra(s).
3. Consulte as APIs vivas quando precisar de números atuais (ver `dados-vivos/`).
4. Responda **com citações** (links para páginas e caminhos de fontes).
5. Arquive boas respostas de volta como páginas novas (ex.: uma correlação descoberta).

### Pesquisar conhecimento externo
- O agente pode pesquisar fontes externas sempre que julgar útil; `raw/publicacoes/` não é uma
  fronteira do conhecimento.
- Dê preferência a estudos revisados por pares, instituições técnicas e fontes primárias ligadas à
  viticultura em **clima tropical**, especialmente quando forem aplicáveis às condições de Minas
  Gerais. Referências de clima subtropical, temperado ou de outros países também podem ser usadas
  quando ajudarem a estabelecer padrões ou trouxerem conhecimento transferível.
- Registre título, autoria ou instituição, URL/DOI e data da consulta. Quando uma síntese usar fonte
  externa, inclua a URL em `fontes` e descreva no corpo da página por que ela é aplicável a Macaia.
- Conhecimento externo embasa interpretações e recomendações, mas não transforma uma generalização
  bibliográfica em fato observado na Alma Gerais. Fatos do vinhedo continuam exigindo fonte datada.

### Revisar (lint)
- Contradições entre páginas; afirmações vencidas por fontes novas; páginas órfãs; conceitos sem
  página própria; referências cruzadas faltando; lacunas que uma consulta às APIs preencheria.
- Sugira novas perguntas e fontes a buscar.

---

## 9. Dados vivos (APIs — WS Clima e InnoVint)

- Clima (WS Clima) e gestão da vinícola (InnoVint/Sutter) são consultados **em tempo real**, não
  copiados para o repo.
- O agente **não** deve reinventar a integração a cada pergunta: leia primeiro o playbook em
  `dados-vivos/` (auth, URL base, endpoints úteis, IDs Alma Gerais, exemplos). Use a documentação
  oficial só para detalhes de parâmetros/campos que o playbook não cobre.
- Credenciais vivem em variáveis de ambiente/secrets — **nunca** em arquivos do repositório.
- Ao usar dados vivos numa síntese, registre a **data da consulta**, a API e o endpoint/parâmetros
  como `fontes` (ex.: `dados-vivos/estacao-meteorologica.md` + `GET .../data/historical/...`).
- Exemplos HTTP reutilizáveis em `dados-vivos/queries/`.

---

## 10. Log

`log.md` é **append-only** e cronológico. Cada entrada começa com um prefixo consistente para ser
filtrável por ferramentas unix:

```
## [AAAA-MM-DD] ingest | <título da fonte>
## [AAAA-MM-DD] query  | <pergunta>
## [AAAA-MM-DD] lint   | <resumo>
```

`grep "^## \[" log.md | tail -5` mostra as 5 últimas entradas.

---

## Cursor Cloud specific instructions

Este repositório é uma **base de conhecimento em Markdown**, não uma aplicação com build/testes.
Não há dependências para instalar, nem serviço para subir, nem suíte de testes automatizados.

- Não existe "servidor" para rodar. Trabalhe editando os arquivos `.md` conforme as convenções acima.
- Validação = coerência do conteúdo: âncoras temporais presentes, `index.md`/`log.md` atualizados,
  wikilinks válidos e separação fato/interpretação respeitada.
- Preserve `raw/` como imutável.
