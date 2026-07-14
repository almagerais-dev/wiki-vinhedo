---
tipo: dados-vivos
titulo: Estação meteorológica (WS Clima)
api: wsclima
atualizado_em: 2026-07-14
---

# Estação meteorológica — WS Clima (dados vivos)

Cada local tem estação própria (hoje só **Macaia**; São Geraldo é expansão futura). Os dados
**não** são copiados para o repo: o agente consulta a API em tempo real e arquiva apenas
**sínteses** na wiki (ex.: resumo climático em `wiki/safras/`).

Documentação oficial (detalhe de campos/erros):
https://wsclima.com.br/integrations/documentation

## Conexão

| Item | Valor |
|---|---|
| URL base | `https://api.wsclima.com.br/integrations` |
| Auth | Header `Authorization: Bearer $WSCLIMA_API_TOKEN` |
| Token | Variável de ambiente `WSCLIMA_API_TOKEN` (nunca no repo) |

## IDs Alma Gerais

_A preencher quando o token for liberado: rodar `GET /stations/list` e registrar aqui o `id` da
estação de Macaia._

| Local | station_id | nome na API | notas |
|---|---|---|---|
| macaia | _a preencher_ | _a preencher_ | |

## Endpoints que o agente usa

Preferir estes; não varrer a doc oficial a cada pergunta.

| Uso | Método e caminho |
|---|---|
| Listar estações da chave | `GET /stations/list` |
| Detalhes / lat-long / data_since | `GET /stations/{id}/details` |
| Leitura atual | `GET /stations/{id}/data/current` |
| Histórico | `GET /stations/{id}/data/historical/{start}/{end}` |

Datas do histórico no formato `YYYYMMDD`. Intervalo máximo: **366 dias**.

Agrupamento automático da API:

- até 7 dias → leituras brutas (`grouping: raw`)
- 8–31 dias → a cada 4 h (`min`/`avg`/`max`)
- > 31 dias → diário (`min`/`avg`/`max`)

## Como o agente deve usar

1. Leia este playbook (e `dados-vivos/queries/exemplos-wsclima.md`) antes de montar a chamada.
2. Consulte para números atuais/históricos (temperatura, chuva, geada, veranico, graus-dia).
3. Abra a documentação oficial só se faltar um parâmetro/campo não coberto aqui.
4. Ao usar numa síntese, registre a **data da consulta**, o endpoint e o período como `fontes`.
5. Em `429`, respeitar o limite; não martelar a API.

## Erros comuns

| Código | Significado |
|---|---|
| `400` | Parâmetros inválidos (data, intervalo) |
| `401` | Token ausente/inválido/expirado |
| `404` | Estação inexistente ou sem permissão |
| `429` | Rate limit |
