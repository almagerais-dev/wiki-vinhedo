---
tipo: exemplos-api
api: innovint
atualizado_em: 2026-07-14
---

# Exemplos HTTP — InnoVint / Sutter

Substituir `$INNOVINT_PAT` e `{wineryId}` pelos valores reais (ver
`dados-vivos/gestao-vinicola.md`). Auth recomendada: Personal Access Token.

## Listar vinícolas acessíveis

```bash
curl -sS -H "Authorization: Access-Token $INNOVINT_PAT" \
  "https://sutter.innovint.us/api/v1/wineries"
```

## Listar lotes

```bash
curl -sS -H "Authorization: Access-Token $INNOVINT_PAT" \
  "https://sutter.innovint.us/api/v1/wineries/{wineryId}/lots?limit=50&offset=0"
```

## Ações de adição (filtro por período)

```bash
curl -sS -H "Authorization: Access-Token $INNOVINT_PAT" \
  "https://sutter.innovint.us/api/v1/wineries/{wineryId}/additionActions?effectiveAtAfter=2026-01-01T00:00:00Z&effectiveAtBefore=2026-07-01T00:00:00Z&limit=50&offset=0"
```

## Ações de análise

```bash
curl -sS -H "Authorization: Access-Token $INNOVINT_PAT" \
  "https://sutter.innovint.us/api/v1/wineries/{wineryId}/actions/analysisActions?limit=50&offset=0"
```

## Recebimento de fruta

```bash
curl -sS -H "Authorization: Access-Token $INNOVINT_PAT" \
  "https://sutter.innovint.us/api/v1/wineries/{wineryId}/actions/receiveFruitActions?limit=50&offset=0"
```

## Análises de um lote

```bash
curl -sS -H "Authorization: Access-Token $INNOVINT_PAT" \
  "https://sutter.innovint.us/api/v1/wineries/{wineryId}/lots/{lotId}/analyses"
```

Paginação: se a resposta indicar próxima página, avançar `offset` até esgotar (respeitando o
rate limit de 120 req/min).
