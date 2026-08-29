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
## [2026-08-29] ingest | Granola 2026-08-28: 14 gravações de manejo do agrônomo ingeridas; 19 eventos, 12 históricos mensais de agosto e a safra 2027 criados
## [2026-08-29] pendencia | 959f04be (Etrel application timeline): fonte diz apenas "o talhão", sem identificar o setor. Ethrel 03/08, poda 17/08, Dormex 19/08 (6,5 L/ha) e MAP 21/08 não geraram evento
## [2026-08-29] pendencia | e69b01c1 (E-TREO application results): setor gravado como "1112" e data como "14 de outubro", posterior à própria gravação. Ethrel 2 L/ha não atribuído a nenhum evento
## [2026-08-29] pendencia | cd9d4b96 (Poda preparation for PEWIS): área identificada por "variedades em teste PEWIS", sem setor; grafia provavelmente de PIWI. Preparo de 26/08 com Ethrel 2 L/ha não gerou evento
## [2026-08-29] pendencia | 8fc6973b (setor 4): dose de Ethrel com valor 2,5 e unidade não recuperável ("2,5 Tert"); evento criado com a dose marcada como pendente
## [2026-08-29] pendencia | Nenhuma das 14 gravações declara safra; eventos de agosto de 2026 receberam safra 2027 pelo ciclo de colheita. Confirmar a convenção de numeração antes de novas ingestões
## [2026-08-29] pendencia | Nenhuma gravação declara estágio fenológico; preparo, poda e Dormex ancorados em dormencia pela natureza da operação e as fertirrigações posteriores à poda deixadas nulas
## [2026-08-29] pendencia | 38dd42a6 (setor 1): a fonte chama a fertirrigação de 28/08 de "segunda", mas a primeira não consta em nenhuma gravação ingerida
## [2026-08-29] lint | tools/validar-wiki.py criado (frontmatter, wikilinks, âncoras temporais, fontes citadas): 91 arquivos, 0 erros. Avisos remanescentes são anteriores a esta ingestão — 2026-01-14-macaia-recebimentos-uva-safra-2026 sem setor e sem ingerido_em; 2026-06-15-macaia-geada-q3 (página de exemplo) sem setor, ingerido_em nem fonte
## [2026-08-29] lint | Uma gravação de 2026-08-27 (6dc805bb, "Edge follow-up action plan") não trata do vinhedo e não foi ingerida
## [2026-08-29] update | Skill ingerir-gravacoes-granola criada: procedimento de ingestão em 10 passos, com a exigência de ingerir pelo transcript verbatim (o resumo do Granola já produziu setor "1112", data "14 de outubro" e unidade "2,5 L/t"); AGENTS.md §8 passa a apontar a skill
## [2026-08-29] update | tools/granola-ingeridos.py criado e AGENTS.md §8 explicitado: a idempotência do Granola é conferida no próprio repositório, com os estados NOVO, JA INGERIDO, SO FONTE e NO LOG; entradas do log passam a citar o prefixo de 8 caracteres do granola_id
## [2026-08-29] ingest | Mapa de plantio Alma Gerais Vivert: ruas, variedades, plantas e produção esperada dos 12 setores; 35.921 plantas; 63.479,8 kg esperados
## [2026-08-29] pendencia | 2026-08-29-mapa-de-plantio-alma-gerais-vivert.json: objeto totais duplica plantas (71842 vs 35921) e produção esperada (126959.6 vs 63479.8 kg)
## [2026-08-29] pendencia | 2026-08-29-mapa-de-plantio-alma-gerais-vivert.json: setor-09 ruas 1-9 com rótulo PIWI´S sem cultivar, clone nem porta-enxerto
