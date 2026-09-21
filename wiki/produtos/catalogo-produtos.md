---
tipo: catalogo
titulo: Catálogo de produtos e documentos
tags: [produtos, defensivos, fertilizantes, adjuvantes, documentacao]
fontes:
  - raw/fichas-tecnicas/comercial/
atualizado_em: 2026-09-21
---

# Catálogo de produtos e documentos

Ponto de entrada da base documental dos produtos usados ou potencialmente usados no vinhedo. Cada
produto tem uma página própria em `wiki/produtos/`, que sintetiza **somente** o que está escrito nos
documentos arquivados em `raw/fichas-tecnicas/comercial/`.

Para o procedimento de consulta, conferência de aplicação e resposta a pergunta de segurança, ver a
skill `.cursor/skills/consultar-produtos-e-aplicacoes/SKILL.md`.

## Como ler este catálogo

- **Registro para videira** reflete o que o documento diz, não o que é possível ou desejável:
  `sim` = a bula ou o rótulo lista uva/videira entre as culturas registradas; `não` = a lista de
  culturas do documento não inclui uva nem videira; `n/a` = produto sem registro de agrotóxico
  (fertilizante, adjuvante isento); `indeterminado` = falta a bula ou o rótulo para saber.
- **Documentos** indica o que está arquivado, e portanto o alcance de qualquer resposta. Um produto sem
  bula não tem dose, alvo nem carência consultáveis nesta base.
- Nenhuma linha desta tabela substitui o rótulo, a bula, o registro vigente ou a decisão do responsável
  técnico.

## Produtos com registro para videira

| Produto | Função | Ingrediente ativo | Alvo registrado em uva | Dose (uva) | Máx. aplicações | Carência | Documentos |
|---|---|---|---|---|---|---|---|
| [[aliette]] | Fungicida | Fosetil-Al 800 g/kg | Míldio (*Plasmopora viticola*) | 250 g/100 L de água | 2 | 15 dias | bula, rótulo, FDS |
| [[amistar-top]] | Fungicida | Azoxistrobina 200 g/L + difenoconazol 125 g/L | Míldio (*Plasmopara vitícola*) | 40–60 mL/100 L ou 400–600 mL/ha | 4 | 7 dias | bula, FISPQ, ficha de emergência |
| [[avatar]] | Inseticida | Indoxacarbe 150 g/L | Traça-dos-cachos (*Cryptobables gnidiella*) | 320 mL/ha | 4 por ciclo | 21 dias | bula, FDS, ficha de emergência |
| [[alion]] | Herbicida | Indaziflam 500 g/L | Plantas daninhas em pré-emergência | 0,15 ou 0,2 L/ha conforme o solo | 1 por ano (intervalo mínimo de 12 meses) | 1 dia | bula, rótulo, FDS, ficha de emergência |

## Produtos sem registro para videira nos documentos disponíveis

| Produto | Função | Ingrediente ativo | Situação | Documentos |
|---|---|---|---|---|
| [[abamectin-72-ec-nortox]] | Acaricida e inseticida | Abamectina 72 g/L | A lista de culturas da bula **não** inclui uva nem videira | bula, FDS, ficha de emergência |

## Adjuvantes e fertilizantes

| Produto | Função | Base | Dose documentada | Documentos |
|---|---|---|---|---|
| [[assist-ec]] | Adjuvante (isento de registro no MAPA) | Óleo mineral 782 g/L | 0,25 a 1,0% v/v na calda | rótulo, FDS |
| [[basfoliar-black-evolution-sl]] | Fertilizante organomineral | 18% COT, 27,5% ácidos fúlvicos, N-P-K-Ca-Mg | Nenhuma dose no documento recebido | bula |

## Produtos com documentação incompleta

| Produto | Função declarada | O que falta | Consequência |
|---|---|---|---|
| [[assist]] | Inseticida (óleo mineral) | Bula e rótulo | Sem cultura, dose, alvo, carência ou número de aplicações consultáveis. A FDS cobre apenas segurança |
| [[basfoliar-black-evolution-sl]] | Fertilizante | FDS | Sem nenhuma orientação de segurança ou emergência nesta base |
| [[abamectin-72-ec-nortox]], [[amistar-top]], [[avatar]] | — | Rótulo | As bulas recebidas trazem o bloco de rótulo com as classificações toxicológica e ambiental; falta a lista de culturas registradas na forma do rótulo, usada como conferência independente da bula |
| [[aliette]], [[assist]], [[assist-ec]] | — | Ficha de emergência | Sem número ONU, número de risco e grupo de embalagem para transporte |

## Restrições documentadas que atravessam produtos

Itens que uma conferência de calendário precisa cruzar, todos escritos nos documentos:

- **[[abamectin-72-ec-nortox]]** — "durante 10 dias antes e 10 dias após a aplicação (...) não devem
  ser usados produtos que contenham Captan, Folpet ou Enxofre". É a única restrição desta base que
  proíbe uma **sequência** de aplicações, e não apenas a mistura.
- **[[aliette]]** — "incompatível com óxido cuproso e alguns fertilizantes foliares como MAP e DAP".
  Macaia usa MAP nas fertirrigações (ver [[irrigacao]]).
- **[[alion]]** — uma única aplicação a cada 12 meses e limite de 100 g de indaziflam por 12 meses;
  plantas a partir de 3,0 anos do transplantio; teor mínimo de matéria orgânica (≥2% em solo arenoso);
  rega somente 48 h após a aplicação.
- **[[amistar-top]]** — azoxistrobina é "extremamente fitotóxica para certas variedades de maçãs";
  não usar em macieira equipamento que já pulverizou o produto. Nunca aplicar a menos de 30 m de
  corpos d'água em aplicação terrestre.
- **[[avatar]]** — "Produto perigoso para abelhas"; aplicar no fim da tarde ou à noite. Não aplicar em
  cultura sob estresse, inclusive por temperaturas muito baixas (geada).
- **Vazão de calda** — as bulas fixam, para uva, 1000 L/ha ([[aliette]]), 800 L/ha ([[amistar-top]]) e
  750 a 900 L/ha ([[avatar]]), enquanto as pulverizações registradas em Macaia usam 200 L/ha. Como a
  dose do Aliette e do Amistar Top é expressa por 100 L de água, a vazão adotada muda a quantidade de
  produto por hectare. Ver [[vazao-de-calda-dos-produtos-registrados-para-videira]].
- **Janela meteorológica** — todos os produtos com bula nesta base trazem condições para aplicação
  terrestre. A mais estreita é a do [[abamectin-72-ec-nortox]] (máximo 28 °C, UR mínima de 70%, vento
  de 2 a 10 km/h); [[aliette]], [[amistar-top]], [[avatar]] e [[alion]] pedem temperatura abaixo de
  30 °C e umidade acima de 55%. Números atuais saem da estação em `dados-vivos/`.

## Telefones de emergência por titular

Retirados dos rótulos, bulas e fichas de emergência. Em emergência, conferir no documento do produto
envolvido, que é a fonte.

| Titular | Produtos | Emergência |
|---|---|---|
| Bayer S.A. | [[aliette]], [[alion]] | 0800-024-3334 (acidente) · 0800-701-0450 (intoxicação) |
| Syngenta | [[amistar-top]] | 0800 704 4304 |
| FMC | [[avatar]] | 0800 34 35 450 · (34) 3319-3019 |
| Nortox S.A. | [[abamectin-72-ec-nortox]] | (43) 3274-8585 |
| BASF S.A. | [[assist]], [[assist-ec]] | 0800 011 2273 |
| Compo Expert | [[basfoliar-black-evolution-sl]] | Não consta do documento recebido |

**Disque-Intoxicação (RENACIAT–ANVISA/MS): 0800-722-6001** — citado por praticamente todos os
documentos. Bombeiros 193, Defesa Civil 199, SAMU 192. Órgão de meio ambiente de Minas Gerais: as
fichas de emergência divergem entre (31) 3915-1905 (Nortox, Syngenta) e (31) 3069-6601 (Bayer); usar o
número da ficha do produto envolvido.

## Estado da remessa de documentos

| Remessa | Documentos | Produtos | Data |
|---|---|---|---|
| 1 de 5 | 20 | 7 (8 páginas, contando [[assist]] e [[assist-ec]] separadamente) | 2026-09-21 |

O time informou um total previsto de 96 documentos. Conforme as remessas seguintes chegarem, novos
produtos entram como páginas próprias e este catálogo é atualizado. Documentos que completem um produto
já catalogado (por exemplo, o rótulo que falta ao [[avatar]]) resolvem a lacuna registrada na página
correspondente.

## Aplicações realizadas

Nenhuma aplicação destes produtos está registrada como realizada em Macaia. O histórico factual de
pulverizações vive em [[fitossanidade]], nos eventos e nos históricos mensais por setor, e cita
produtos que **não** têm documento nesta base (Cercobin, Zorvec, Civant Prime, Absolut Fix, entre
outros). Uma aplicação só é registrada como realizada depois de confirmada pela equipe — intenção,
planejamento ou discussão não viram fato.
