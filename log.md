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
## [2026-08-23] update | Fontes brutas simplificadas; fichas técnicas e registros de manejo/ciclos separados; pesquisa externa orientada a clima tropical
## [2026-08-23] update | Modelo de eventos por setor, históricos mensais e skill de consulta setorial adicionados
## [2026-08-25] ingest | Mapa georreferenciado dos dez setores de Macaia cadastrado; área total de 9,7952 ha
## [2026-08-29] ingest | Coleção Plantio Vivert com 12 polígonos; setores 11 e 12 cadastrados; geometria vigente atualizada; área total 10,7641 ha
## [2026-08-29] pendencia | 2026-08-29-plantio-vivert.geojson: polígonos 11 e 12 sem rótulo de talhão; numerados setor-11 e setor-12 pela ordem na coleção
## [2026-08-29] ingest | Mapa de plantio Alma Gerais Vivert: ruas, variedades, plantas e produção esperada dos 12 setores; 35.921 plantas; 63.479,8 kg esperados
## [2026-08-29] pendencia | 2026-08-29-mapa-de-plantio-alma-gerais-vivert.json: objeto totais duplica plantas (71842 vs 35921) e produção esperada (126959.6 vs 63479.8 kg)
## [2026-08-29] pendencia | 2026-08-29-mapa-de-plantio-alma-gerais-vivert.json: setor-09 ruas 1-9 com rótulo PIWI´S sem cultivar, clone nem porta-enxerto
