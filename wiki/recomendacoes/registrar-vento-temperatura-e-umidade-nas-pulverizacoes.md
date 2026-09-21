---
tipo: recomendacao
titulo: Registrar vento, temperatura e umidade no momento de cada pulverização
origem: agente
status: sugerida
data: 2026-09-21
local: macaia
setores: []
variedades: []
safra: 2027
tags: [produtos, condicoes-ambientais, vento, conferencia-de-aplicacao, fitossanidade]
fontes:
  - raw/fichas-tecnicas/comercial/abamectin-72-ec-nortox-bula.pdf
  - raw/fichas-tecnicas/comercial/cabrio-top-bula.pdf
  - raw/fichas-tecnicas/comercial/caramba-bula.pdf
  - raw/fichas-tecnicas/comercial/cercobin-875-wg-bula.pdf
  - raw/fichas-tecnicas/comercial/collis-bula.pdf
  - raw/fichas-tecnicas/comercial/comet-bula.pdf
  - raw/fichas-tecnicas/comercial/completto-bula.pdf
  - raw/fichas-tecnicas/comercial/curzate-bula.pdf
  - dados-vivos/estacao-meteorologica.md
atualizado_em: 2026-09-21
---

# Registrar vento, temperatura e umidade no momento de cada pulverização

**Recomendação do agente, status `sugerida`.** Toda bula com registro para videira nesta base exige uma
janela de vento, temperatura e umidade para a aplicação terrestre, e **nenhuma das pulverizações
registradas em Macaia anota nenhum desses três valores**. Sem eles, a conferência de uma aplicação
já realizada fica impossível de fechar: o item existe na bula e não existe no registro de campo.

## O que os documentos exigem

Os três parâmetros aparecem em todas as bulas, com faixas que diferem por titular:

| Produtos | Vento | Temperatura | Umidade relativa |
|---|---|---|---|
| [[cabrio-top]], [[caramba]], [[collis]], [[comet]] (BASF) | 5 a 10 km/h | abaixo de 30 °C | acima de 60% |
| [[cercobin-875-wg]], [[completto]], [[curzate]] | 3 a 10 km/h | abaixo / até 30 °C | acima de 50% |
| [[amistar-top]] | 3 a 10 km/h | abaixo de 30 °C | acima de 55% |
| [[abamectin-72-ec-nortox]] | 2 a 10 km/h | máximo 28 °C | mínimo 70% |

**O vento tem piso, não só teto.** É a parte da janela que passa despercebida: as bulas não dizem
apenas "não aplicar com vento forte", elas fixam um mínimo. As quatro bulas BASF explicam por quê: "A
ausência de vento pode indicar situação de inversão térmica, que deve ser evitada"
(`raw/fichas-tecnicas/comercial/cabrio-top-bula.pdf`). Sem vento, a calda pode ficar suspensa e
derivar depois, em vez de se depositar na planta.

As bulas BASF acrescentam uma quarta condição, também não registrada em campo: "A ocorrência de chuvas
dentro de um período de quatro (4) horas após a aplicação pode afetar o desempenho do produto. Não
aplicar logo após a ocorrência de chuva ou em condições de orvalho."

## O que o campo registra

Nada. Uma varredura por `\bvento\b`, "velocidade do vento" e "umidade relativa" em
`raw/registros-manejo/`, `raw/registros-ciclos-videira/` e `wiki/eventos/` não devolve nenhuma
ocorrência. As 17 pulverizações anotadas em setembro de 2026 registram produto, dose e vazão, e
nenhuma condição ambiental.

## Avaliação do agente

Isto é **interpretação**, não fato de campo.

A estação meteorológica de Macaia (`dados-vivos/estacao-meteorologica.md`, estação 966) responde em
tempo real e cobre exatamente os três parâmetros. O problema não é falta de instrumento: é que a
leitura não é capturada no momento da operação e a API **não devolve histórico** para os meses de 2026
já verificados, o que impede reconstruir as condições depois. A janela de conferência é, na prática, o
próprio momento da aplicação.

Uma leitura tomada em 2026-09-21 às 17:30 (GMT-3) mostra por que isso importa: temperatura 25,8 °C e
umidade 64% atenderiam à janela de todos os produtos BASF, **mas o vento estava em 0 km/h**, com rajada
de 4,8 km/h. Pelo texto das bulas, esse instante não é adequado para pulverizar nenhum dos oito
produtos registrados para videira desta base — e é justamente o parâmetro que o registro de campo não
guarda. Não se trata de uma pulverização real: é uma leitura de demonstração, e nenhuma aplicação está
sendo avaliada aqui.

**Correlação não implica causalidade e nada disso afirma que as aplicações anteriores foram malfeitas.**
A ausência do dado não é evidência de condição inadequada; é a impossibilidade de conferir.

## O que fazer

1. Anotar, na própria gravação da operação, a temperatura, a umidade relativa e a velocidade do vento
   no momento da pulverização — ou pedir a leitura da estação 966 durante a operação.
2. Tratar o vento como faixa, com mínimo e máximo, e não apenas como limite superior.
3. Observar a previsão de chuva para as 4 horas seguintes quando o produto for de bula BASF.
4. Decisão de aplicar ou não aplicar é do responsável técnico. Esta página organiza o que os documentos
   exigem; não autoriza nem veda operação nenhuma.

## Ligações

- Catálogo e janelas por produto: [[catalogo-produtos]]
- Tema: [[fitossanidade]] · [[clima]]
- Recomendação irmã, do mesmo tipo de divergência: [[vazao-de-calda-dos-produtos-registrados-para-videira]]
- Safra em curso: [[safra-2027]]
