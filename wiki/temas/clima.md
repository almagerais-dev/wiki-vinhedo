---
tipo: tema
titulo: Clima
tags: [meteorologia]
fontes: [dados-vivos/estacao-meteorologica.md]
atualizado_em: 2026-07-14
---

# Clima

Síntese do clima de [[macaia]]. Dados quantitativos vêm da estação `966` na API WS Clima (ver
`dados-vivos/estacao-meteorologica.md`).

## Resumo operacional

Em 2026-07-14, a estação estava online e a leitura atual funcionava. A API informou coordenadas
`-21.123929, -44.909792`, elevação de 827 m e fuso `America/Sao_Paulo`.

O histórico retornou zero linhas em todos os intervalos testados, inclusive no próprio dia, nos
últimos 7 e 31 dias e de 2026-01-01 a 2026-07-14. Por isso, ainda não há base nessa API para
calcular resumo climático da safra, chuva acumulada, extremos, geadas, veranicos ou graus-dia.
Ausência de linhas não significa ausência desses fenômenos.

## O que sabemos (das fontes)

- Fonte viva ativa: WS Clima, estação `966`.
- Campos disponíveis na leitura atual: temperatura, índice de calor, ponto de orvalho, sensação
  térmica, vento, pressão, taxa e acumulado de precipitação, umidade e radiação solar.
- Não há publicações nem registros de manejo ou dos ciclos da videira ingeridos em `raw/` até esta
  atualização.

## Onde o clima entra na conferência de aplicações

A leitura atual da estação cobre exatamente os três parâmetros que as bulas dos produtos exigem para a
aplicação terrestre — vento, temperatura e umidade relativa. Como o histórico da API volta vazio, a
conferência só é possível **no momento da operação**; depois, o dado não é recuperável.

- [[registrar-vento-temperatura-e-umidade-nas-pulverizacoes]] — as faixas exigidas por produto e o fato
  de que nenhuma pulverização registrada em Macaia anota esses valores.
- Janelas por titular: [[catalogo-produtos]].

## Como se manifesta no nosso vinhedo

- Resumos por safra: [[safra-2026]].
- Eventos climáticos factuais devem entrar em `wiki/eventos/` somente quando houver medição ou
  observação datada.
