---
tipo: dados-vivos
titulo: Gestão da vinícola (InnoVint / Sutter)
api: innovint
atualizado_em: 2026-07-14
---

# Gestão da vinícola — InnoVint / Sutter (dados vivos)

API da gestão da vinícola (lotes, vasos, ações de adição/análise, recebimento de fruta, blocos,
vinhedos, etc.). Consultado em tempo real; apenas sínteses vão para a wiki.

Documentação oficial (Redoc / OpenAPI):
https://sutter.innovint.us/api/v1/docs/

Schema OpenAPI (máquina): `https://sutter.innovint.us/api/v1/schema/`

> InnoVint é software de **vinícola/adega** (cellar), não um ERP de manejo de campo. Eventos de
> manejo no vinhedo (pulverização, poda, irrigação) podem não existir aqui — quando faltarem,
> buscar em `raw/` / observações de campo.

## Conexão

| Item | Valor |
|---|---|
| URL base | `https://sutter.innovint.us` |
| Auth (recomendado) | Header `Authorization: Access-Token $INNOVINT_PAT` |
| Auth (alternativo) | Header `Authorization: Bearer <token de login>` — evita em produção |
| Token | Variável de ambiente `INNOVINT_PAT` (Personal Access Token; nunca no repo) |
| Rate limit | 120 req/min → `429` + header `Retry-After` |
| Paginação | `limit`/`offset` (padrão até 200 por página) |

PATs são gerenciados em:
https://cellar.innovint.us/#/developer/personal-access-token

## IDs Alma Gerais

_A preencher quando o acesso for liberado: `GET /api/v1/wineries` e registrar o `wineryId`._

| Local / contexto | wineryId | notas |
|---|---|---|
| Alma Gerais (Macaia) | _a preencher_ | |

## Endpoints que o agente usa com frequência

Preferir estes; a API tem dezenas de recursos — não explorar o catálogo inteiro a cada pergunta.

| Uso | Método e caminho |
|---|---|
| Listar vinícolas acessíveis | `GET /api/v1/wineries` |
| Lotes | `GET /api/v1/wineries/{wineryId}/lots` |
| Análises de um lote | `GET /api/v1/wineries/{wineryId}/lots/{lotId}/analyses` |
| Ações de adição | `GET /api/v1/wineries/{wineryId}/additionActions` |
| Ações de análise | `GET /api/v1/wineries/{wineryId}/actions/analysisActions` |
| Recebimento de fruta | `GET /api/v1/wineries/{wineryId}/actions/receiveFruitActions` |
| Processar fruta → volume | `GET /api/v1/wineries/{wineryId}/actions/processFruitToVolumeActions` |
| Vasos | `GET /api/v1/wineries/{wineryId}/vessels` |
| Vinhedos / blocos | `GET .../vineyards` · `GET .../blocks` |

Filtros úteis em listagens de ações (quando disponíveis): `effectiveAtAfter`, `effectiveAtBefore`,
`createdAtAfter`, `createdAtBefore`, `actionType`, `sort`, `limit`, `offset`.

## Como o agente deve usar

1. Leia este playbook (e `dados-vivos/queries/exemplos-innovint.md`) antes de montar a chamada.
2. Use para reconstruir linha do tempo de adega/lote/safra e números de análise/adições.
3. Eventos **marcantes** (ex.: recebimento de fruta da colheita, análise decisiva) viram páginas em
   `wiki/eventos/`; o operacional de alta frequência fica na API e é sintetizado por safra/vinho.
4. Abra a documentação oficial só para parâmetros/campos não cobertos aqui.
5. Registrar data da consulta, endpoint e filtros como `fontes`.
6. Em `429`, esperar o `Retry-After`; não martelar a API.
7. Por padrão, **somente leitura** (GET). Não criar/alterar recursos sem pedido explícito do humano.
