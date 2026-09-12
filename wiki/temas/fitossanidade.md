---
tipo: tema
titulo: Fitossanidade
tags: [fitossanidade, pulverizacao, gema-algodao, cercobin, civant-prime, absolut-fix]
fontes:
  - raw/registros-manejo/2026-09-03-macaia-setor-01-pulverizacao-gema-algodao.md
  - raw/registros-manejo/2026-09-03-macaia-setores-05-08-fertirrigacao-e-pulverizacao.md
  - raw/registros-manejo/2026-09-03-macaia-setores-06-07-fertirrigacao-e-pulverizacao.md
  - raw/registros-manejo/2026-09-11-macaia-setor-03-fertirrigacao-e-pulverizacao.md
  - raw/registros-manejo/2026-09-11-macaia-setores-06-07-pulverizacao.md
  - raw/registros-manejo/2026-09-11-macaia-setor-01-pulverizacao-data-impossivel.md
  - raw/registros-manejo/2026-09-11-macaia-setores-11-12-fertirrigacao-e-pulverizacao.md
atualizado_em: 2026-09-12
---

# Fitossanidade

## Pulverizações registradas (safra 2027)

As primeiras pulverizações documentadas na wiki são de 2026-09-02, logo depois da poda de agosto e
das fertirrigações com MAP descritas em [[irrigacao]]. A calda é idêntica nos setores registrados:

| Data | Setor(es) | Calda | Evento |
|---|---|---|---|
| 2026-09-02 | [[setor-01]] | Cercobin 600 g + Civant Prime 500 ml + Absolut Fix 600 ml, em 200 L/ha | [[2026-09-02-macaia-setor-01-pulverizacao-gema-algodao]] |
| 2026-09-02 | [[setor-05]], [[setor-08]] | Cercobin 600 g + Civant Prime 500 ml + Absolut Fix 600 ml, em 200 L/ha | [[2026-09-02-macaia-setores-05-08-pulverizacao-gema-algodao]] |
| 2026-09-09 | [[setor-03]] | Cercobin 600 g + Absoluto Fix 200 ml, em 200 L/ha | [[2026-09-09-macaia-setor-03-pulverizacao-gema-algodao]] |
| 2026-09-10 | [[setor-06]], [[setor-07]] | Cercobin 600 g + Absoluto Fix 600 ml, em 200 L/ha | [[2026-09-10-macaia-setores-06-07-pulverizacao]] |

As gravações não dizem contra o que se pulveriza, nem a área tratada, nem se as doses de 600 g,
500 ml e 600 ml são por hectare ou por tanque de 200 L. A wiki registra como a fonte diz.

A segunda rodada, gravada em 2026-09-11, muda a calda: o Civant Prime some das quatro gravações e
sobram Cercobin e Absoluto Fix. O Cercobin se mantém a 600 g em todas; o Absoluto Fix aparece a
600 ml nos setores 06, 07, 11, 12 e 01, e a 200 ml no setor 03. As fontes são inequívocas em cada
caso e cada evento registra a sua dose; confirmar com a equipe se o setor 03 recebeu mesmo um terço
da dose dos demais é uma das pendências de 2026-09-12.

## O estágio "gema algodão"

As três gravações situam a operação no estágio que o agrônomo chama de "gema algodão". Esse nome não
consta do vocabulário controlado de `estagio_fenologico` do `AGENTS.md`, e por isso os eventos
ficaram com o campo nulo em vez de receberem um estágio escolhido pela wiki. Enquanto a
correspondência não for confirmada pela equipe, não há como comparar essas pulverizações com
eventos de outros ciclos pelo estágio.

O resumo automático do Granola leu "gema algodão" como "Cultura: algodão" em `786405af`, e o título
da gravação carrega o mesmo erro. Não há algodão em Macaia; ver a nota na fonte bruta.

## Nomenclatura dos produtos

Cercobin (tiofanato-metílico), Civant Prime e Absolut Fix aparecem pela primeira vez na wiki nestas
gravações. Nenhum deles tem ficha técnica em `raw/fichas-tecnicas/`, e as transcrições não trazem
concentração nem formulação.

## Lacunas

- A pulverização dos setores [[setor-06]] e [[setor-07]] está relatada em `001b16e3`, mas com data
  "2 de novembro de 2026", posterior à gravação. Sem data ancorável não há evento, ainda que a
  mesma calda tenha sido aplicada nos setores 01, 05 e 08 em 2026-09-02.
- A pulverização do [[setor-01]] de `2c664c39` está datada em "10 de novembro de 2026" e a dos
  setores [[setor-11]] e [[setor-12]] de `75804673` traz duas datas contraditórias na mesma fonte.
  Nenhuma das duas gerou evento; ver as `pendencia` de 2026-09-12.
- Não há pulverização registrada para os setores 02, 04, 09, 10, 11 e 12.
- A gravação dos setores 06 e 07 de 2026-09-10 chama a operação de "Ovelhização" e, ao contrário
  das de 2026-09-02, não declara o estágio "gema algodão" nem qualquer alvo.
- Nenhuma ocorrência de doença ou praga foi registrada em gravação até 2026-09-11, o que torna as
  pulverizações registros de operação, não de resposta a um problema observado.

## Interpretações relacionadas

_Nenhuma correlação ou hipótese registrada._
