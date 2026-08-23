# Log da wiki-vinhedo

Registro cronológico e append-only. Cada entrada começa com `## [AAAA-MM-DD] tipo | descrição`.
Filtrar as últimas entradas: `grep "^## \[" log.md | tail -5`.

## [2026-07-08] setup | Estrutura inicial da wiki criada (camadas raw/wiki/dados-vivos, schema, gabaritos e exemplos)
## [2026-07-08] update | Foco reduzido para apenas Macaia; São Geraldo marcado como expansão futura (estrutura multi-local mantida)
## [2026-07-14] update | Dados vivos migrados de PostgreSQL para APIs (WS Clima + InnoVint); playbooks em dados-vivos/
## [2026-07-14] query | WS Clima: estação 966 confirmada para Macaia; leitura atual ativa e histórico sem registros
## [2026-07-14] query | InnoVint: vinícola Alma Gerais mapeada; cadastros, lotes, vasos, recebimentos e análises sintetizados
## [2026-07-14] ingest | Recebimentos de uva da safra 2026 consolidados até 2026-07-14
## [2026-07-21] update | InnoVint: documentadas regras de reconciliação de recebimentos e divergência conhecida do Sauvignon Blanc Vivert
## [2026-08-23] ingest | Rotina de campo 2026-08-23: poda nos setores 5 e 7 e pulverização contra míldio nos setores 3 e 4 (quadras q3/q4/q5/q7 e tema fitossanidade criados; safra e estágio fenológico a confirmar)
