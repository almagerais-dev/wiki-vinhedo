---
tipo: indice
atualizado_em: 2026-08-29
---

# Índice da wiki-vinhedo

Catálogo de todas as páginas da wiki. O agente lê este arquivo primeiro ao responder perguntas e o
atualiza a cada ingestão. Veja as convenções em `AGENTS.md`.

## Visão geral

- [[overview]] — síntese geral do vinhedo.

## Fontes brutas

- `raw/publicacoes/` — publicações em uma coleção única.
- `raw/fichas-tecnicas/comercial/` e `raw/fichas-tecnicas/biologicos/` — fichas de produtos.
- `raw/analises/`, `raw/qualidade-uva/`, `raw/qualidade-vinho/` e `raw/consultoria/` — documentos
  consolidados, sem subdivisões.
- `raw/registros-manejo/` e `raw/registros-ciclos-videira/` — registros datados de campo. As 14
  gravações do Granola de 2026-08-28 estão em `raw/registros-manejo/`.
- `raw/mapa-plantio/` — mapa georreferenciado e confirmações cadastrais dos setores.

## Locais

- [[macaia]] — local de cultivo Macaia (ativo).
- _São Geraldo: expansão futura (a estrutura já suporta múltiplos locais)._

## Quadras

- `_modelo-quadra` — gabarito para páginas de quadra.

## Setores

- [[_modelo-setor]] — gabarito para o cadastro canônico de setor.
- [[setor-01]] — Sauvignon Blanc; ruas 1–47; 0,4669 ha.
- [[setor-02]] — Syrah; ruas 1–39; 1,2918 ha.
- [[setor-03]] — Syrah; ruas 1–36; 1,2088 ha.
- [[setor-04]] — Sauvignon Blanc; ruas 1–38; 1,0799 ha.
- [[setor-05]] — Cabernet Franc; ruas 1–42; 1,0614 ha.
- [[setor-06]] — Cabernet Franc e Cabernet Sauvignon; ruas 1–38; 1,0759 ha.
- [[setor-07]] — Cabernet Franc; ruas 1–24; 0,9067 ha.
- [[setor-08]] — Cabernet Sauvignon; ruas 1–18 plantadas, 19–42 sem plantio; 0,2711 ha.
- [[setor-09]] — PIWI'S e Cabernet Franc; ruas 1–71, com 10–41 sem plantio; 1,0859 ha.
- [[setor-10]] — Sauvignon Blanc, Cabernet Franc e Syrah; ruas 1–10; 1,3468 ha.
- [[setor-11]] — Margoth, Cabernet Franc e Marselan; ruas 1–46; 0,3498 ha.
- [[setor-12]] — Marselan; ruas 1–47; 0,6191 ha.

## Variedades

- `_modelo-variedade` — gabarito para páginas de variedade.
- [[cabernet-franc]] — 8.536 plantas; setores 05, 06, 07, 09, 10 e 11.
- [[cabernet-sauvignon]] — 5.689 plantas; setores 06 e 08.
- [[margoth]] — 250 plantas; setor 11.
- [[marselan]] — 2.965 plantas; setores 11 e 12.
- [[piwis]] — 500 plantas; rótulo `PIWI´S` na fonte, cultivar não informado.
- [[sauvignon-blanc]] — 8.870 plantas; setores 01, 04 e 10.
- [[syrah]] — 9.111 plantas; setores 02, 03 e 10.

## Safras

- `_modelo-safra` — gabarito para páginas de safra.
- [[safra-2026]] — exemplo de hub temporal de safra.
- [[safra-2027]] — ciclo aberto pela poda de agosto de 2026 (convenção de numeração a confirmar).

## Vinhos

- `_modelo-vinho` — gabarito para páginas de vinho.

## Temas

- `_modelo-tema` — gabarito para páginas de tema.
- [[clima]] — cobertura e limites atuais da estação de Macaia.
- [[operacao-de-adega]] — modelo dos dados e retrato operacional do InnoVint.
- [[poda-desfolha]] — protocolo de preparo, poda e quebra de dormência observado em Macaia.
- [[irrigacao]] — lâminas do ciclo de poda e fertirrigações registradas.

## Eventos (linha do tempo)

- `_modelo-evento` — gabarito para eventos datados.
- [[2026-01-14-macaia-recebimentos-uva-safra-2026]] — recebimentos consolidados da safra 2026.
- [[2026-06-15-macaia-geada-q3]] — exemplo de evento.

## Históricos mensais por setor

- [[_modelo-historico-mensal-setor]] — gabarito de índice cronológico mensal.
- 2026-08: [[2026-08-setor-01]], [[2026-08-setor-02]], [[2026-08-setor-03]], [[2026-08-setor-04]],
  [[2026-08-setor-05]], [[2026-08-setor-06]], [[2026-08-setor-07]], [[2026-08-setor-08]],
  [[2026-08-setor-09]], [[2026-08-setor-10]], [[2026-08-setor-11]] e [[2026-08-setor-12]].

## Correlações

- `_modelo-correlacao` — gabarito para correlações.

## Hipóteses

- `_modelo-hipotese` — gabarito para hipóteses.

## Recomendações

- `_modelo-recomendacao` — gabarito para recomendações.
- [[irrigacao-pre-e-pos-poda-2026]] — 30 mm antes da poda e 21 mm por semana depois (agronômica).

## Dados vivos

- `dados-vivos/estacao-meteorologica.md` — WS Clima (clima)
- `dados-vivos/gestao-vinicola.md` — InnoVint / Sutter (vinícola)
- `dados-vivos/queries/exemplos-wsclima.md`
- `dados-vivos/queries/exemplos-innovint.md`

## Ferramentas

- `tools/granola-ingeridos.py` — registro de idempotência do Granola: lista as gravações já
  ingeridas, o estado de cada uma e a janela a consultar. Rodar **antes** de cada ingestão.
- `tools/validar-wiki.py` — lint estrutural (frontmatter, wikilinks, âncoras temporais, fontes
  citadas). Rodar **ao fechar** cada ingestão.
