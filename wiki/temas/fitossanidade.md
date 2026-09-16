---
tipo: tema
titulo: Fitossanidade
tags: [fitossanidade, pulverizacao, gema-algodao, cercobin, civant-prime, absolut-fix, zorvec]
fontes:
  - raw/registros-manejo/2026-09-03-macaia-setor-01-pulverizacao-gema-algodao.md
  - raw/registros-manejo/2026-09-03-macaia-setores-05-08-fertirrigacao-e-pulverizacao.md
  - raw/registros-manejo/2026-09-03-macaia-setores-06-07-fertirrigacao-e-pulverizacao.md
  - raw/registros-manejo/2026-09-11-macaia-setor-03-fertirrigacao-e-pulverizacao.md
  - raw/registros-manejo/2026-09-11-macaia-setores-06-07-pulverizacao.md
  - raw/registros-manejo/2026-09-11-macaia-setor-01-pulverizacao-data-impossivel.md
  - raw/registros-manejo/2026-09-11-macaia-setores-11-12-fertirrigacao-e-pulverizacao.md
  - raw/registros-manejo/2026-09-15-macaia-setor-09-pulverizacao-cercobin.md
  - raw/registros-manejo/2026-09-15-macaia-setor-01-pulverizacao-zorvec.md
  - raw/registros-manejo/2026-09-15-macaia-setores-06-07-pulverizacao-zorvec.md
  - raw/registros-manejo/2026-09-15-macaia-setores-05-08-pulverizacao-produto-nao-transcrito.md
atualizado_em: 2026-09-16
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
| 2026-09-10 | [[setor-09]] | Cercobin 600 g + "silvanto prime" 500 ml + Absoluto Fix 600 ml, em 200 L/ha | [[2026-09-10-macaia-setor-09-pulverizacao]] |
| 2026-09-14 | [[setor-01]] | Zorvec 400 ml + Absoluto Fix 600 ml, em 200 L/ha | [[2026-09-14-macaia-setor-01-pulverizacao-zorvec]] |
| 2026-09-14 | [[setor-06]], [[setor-07]] | Zorvec 400 ml + Absolut Fix 600 ml, em 200 L/ha | [[2026-09-14-macaia-setores-06-07-pulverizacao-zorvec]] |
| 2026-09-14 | [[setor-05]], [[setor-08]] | produto não transcrito 400 ml + Absolut Fix 600 ml, em 200 L/ha | [[2026-09-14-macaia-setores-05-08-pulverizacao]] |

As gravações não dizem contra o que se pulveriza, nem a área tratada, nem se as doses de 600 g,
500 ml e 600 ml são por hectare ou por tanque de 200 L. A wiki registra como a fonte diz.

A segunda rodada, gravada em 2026-09-11, muda a calda: o Civant Prime some das quatro gravações e
sobram Cercobin e Absoluto Fix. O Cercobin se mantém a 600 g em todas; o Absoluto Fix aparece a
600 ml nos setores 06, 07, 11, 12 e 01, e a 200 ml no setor 03. As fontes são inequívocas em cada
caso e cada evento registra a sua dose; confirmar com a equipe se o setor 03 recebeu mesmo um terço
da dose dos demais é uma das pendências de 2026-09-12.

A terceira rodada, gravada em 2026-09-15, muda o fungicida. Em 2026-09-14 os setores 01, 05, 06, 07
e 08 recebem 400 ml de Zorvec e 600 ml de Absolut Fix em 200 L/ha: o Cercobin, presente em todas as
pulverizações de 2026-09-02 a 2026-09-10, desaparece da calda, e o Zorvec aparece pela primeira vez
nos registros de Macaia. As três gravações da rodada declaram o mesmo motivo — chuva —, sem
quantificá-la. Nos setores 05 e 08 o nome do produto não foi recuperado pela transcrição ("sorvete")
e ficou pendente, ainda que a dose e o restante da calda coincidam com os das gravações irmãs.

A pulverização do setor 09 em 2026-09-10, gravada só em 2026-09-15, é a primeira do setor e a única
depois de 2026-09-02 a manter o inseticida na calda.

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
concentração nem formulação. O Zorvec entra na wiki em 2026-09-14, também sem ficha técnica.

O inseticida é grafado "Civant Prime" nas gravações de 2026-09-03 e "silvanto prime" na de
2026-09-15. Nenhuma das duas formas é um nome comercial conhecido, e a wiki mantém as duas como
grafias da fonte, sem decidir qual é a correta. Grafias do Absolut Fix já vistas: Absoluto Fix,
Absoluto Fixo, Absolut Fix.

## Lacunas

- A pulverização dos setores [[setor-06]] e [[setor-07]] está relatada em `001b16e3`, mas com data
  "2 de novembro de 2026", posterior à gravação. Sem data ancorável não há evento, ainda que a
  mesma calda tenha sido aplicada nos setores 01, 05 e 08 em 2026-09-02.
- A pulverização do [[setor-01]] de `2c664c39` está datada em "10 de novembro de 2026" e a dos
  setores [[setor-11]] e [[setor-12]] de `75804673` traz duas datas contraditórias na mesma fonte.
  Nenhuma das duas gerou evento; ver as `pendencia` de 2026-09-12.
- Não há pulverização registrada para os setores 02, 04, 10, 11 e 12.
- O primeiro produto da pulverização dos setores [[setor-05]] e [[setor-08]] de 2026-09-14 está
  transcrito como "sorvete" e não foi identificado. O evento existe porque data, setores e doses
  estão ancorados, mas o produto segue pendente; ver a `pendencia` de 2026-09-16.
- Nenhuma gravação diz contra o que o Zorvec foi aplicado, e a chuva citada como motivo não é
  quantificada em milímetros. Uma consulta à estação WS Clima (ver [[clima]]) poderia dimensionar o
  volume de chuva dos dias anteriores a 2026-09-14.
- A gravação dos setores 06 e 07 de 2026-09-10 chama a operação de "Ovelhização" e, ao contrário
  das de 2026-09-02, não declara o estágio "gema algodão" nem qualquer alvo.
- Nenhuma ocorrência de doença ou praga foi registrada em gravação até 2026-09-11, o que torna as
  pulverizações registros de operação, não de resposta a um problema observado.

## Interpretações relacionadas

_Nenhuma correlação ou hipótese registrada._
