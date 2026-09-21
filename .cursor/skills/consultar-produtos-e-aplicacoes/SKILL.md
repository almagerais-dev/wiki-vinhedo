---
name: consultar-produtos-e-aplicacoes
description: Consulta a base documental dos produtos do vinhedo da Alma Gerais (bulas, rótulos, FDS/FISPQ e fichas de emergência) e confere aplicações. Use quando a pergunta envolver um produto, defensivo, agrotóxico, fungicida, inseticida, acaricida, herbicida, adjuvante, fertilizante, calda, dose, alvo, praga, doença, carência, intervalo de segurança, número de aplicações, mistura, compatibilidade, EPI, primeiros socorros, derramamento, intoxicação, emergência, ficha de segurança, bula ou rótulo; e também quando o usuário disser que vai fazer, planeja fazer ou já fez uma aplicação.
---

# Consultar produtos e conferir aplicações

Esta skill governa tudo o que envolve os produtos do vinhedo. A base documental fica em
`raw/fichas-tecnicas/` (PDFs imutáveis) e é sintetizada em `wiki/produtos/`, com o
[[catalogo-produtos]] como ponto de entrada.

## Princípio que vale para toda a skill

**O documento manda.** Não invente, não presuma e não complete informação técnica que não esteja nos
documentos consultados. Quando os documentos disponíveis não bastam, diga isso — essa é uma resposta
correta e útil, e é melhor do que uma resposta plausível.

Distinga sempre três coisas diferentes, e nomeie qual delas você está dando:

1. **O que está escrito no documento** (com o produto, o arquivo e, quando útil, a frase literal).
2. **Interpretação ou informação complementar** sua, de conhecimento externo ou de cálculo.
3. **O que os documentos não permitem concluir.**

Para segurança, conformidade legal e autorização de uso, nada substitui rótulo, bula, registro
vigente, responsável técnico e autoridades competentes. Diga isso quando a pergunta chegar nesse
terreno.

## 1. Consulta simples sobre um produto

1. Abra o [[catalogo-produtos]] e localize o produto. Confira as grafias: as gravações de campo trazem
   nomes deformados pela transcrição automática, e nomes parecidos podem ser produtos distintos
   (por exemplo [[assist]] e [[assist-ec]], que são produtos diferentes da mesma fabricante).
2. Abra a página do produto em `wiki/produtos/`. Ela já traz identificação, uso na videira, restrições,
   compatibilidade, condições de aplicação e segurança, com o caminho de cada documento.
3. Se a pergunta exigir detalhe que a página não cobre, **abra o PDF** em
   `raw/fichas-tecnicas/comercial/` e cite o documento.
4. Se o produto não estiver no catálogo, diga que não há documento dele na base. Não responda por
   analogia com um produto de ingrediente ativo parecido, e não preencha a lacuna com conhecimento
   geral sem marcar que é isso o que está fazendo.
5. Responda com citações: nome do produto, tipo de documento e caminho do arquivo.

## 2. Pedido de documento

Quando o pedido for "ficha de segurança do produto X", "bula do X", "ficha de emergência do X":

1. Localize o arquivo pela página do produto ou por `ls raw/fichas-tecnicas/comercial/`.
2. Informe o caminho exato e a versão/data impressa no documento.
3. Apresente o conteúdo pedido. Se aquele tipo de documento não existir para o produto, diga
   explicitamente qual existe no lugar — FDS e bula não são intercambiáveis.

## 3. Pergunta de segurança ou emergência

Prioridade absoluta: **reproduzir fielmente** a orientação oficial da ficha de segurança, da ficha de
emergência ou da bula aplicável.

1. Identifique o produto. Se a pergunta for genérica ("o que fazer em caso de contato com os olhos?")
   e houver mais de um produto envolvido ou nenhum indicado, pergunte qual é o produto **ou** responda
   por produto, separadamente — as orientações diferem entre eles.
2. Reproduza o texto do documento, não uma paráfrase. Preserve números (minutos de lavagem, raios de
   isolamento, temperaturas) e proibições ("NÃO provoque vômito").
3. Indique de qual documento a informação saiu.
4. Deixe claro quando o próprio documento manda procurar atendimento ou contato especializado, e
   reproduza os telefones: emergência do titular, Disque-Intoxicação 0800-722-6001 e o que mais o
   documento listar.
5. Se o produto não tiver o documento de segurança na base (é o caso do
   [[basfoliar-black-evolution-sl]], sem FDS), diga isso de imediato, no começo da resposta, e oriente a
   obter o documento com o fabricante ou fornecedor. Não improvise conduta de emergência.

## 4. Conferência de uma aplicação planejada

Quando o usuário informar que uma aplicação **será** realizada, faça a conferência técnica cruzando o
que estiver disponível. Confira, item por item, e diga o resultado de cada um:

1. **Produto** — existe documento na base? Qual?
2. **Cultura** — a bula lista uva/videira entre as culturas registradas? Se não lista (caso do
   [[abamectin-72-ec-nortox]]), esse é o primeiro ponto da resposta.
3. **Alvo** — a praga ou doença pretendida está entre os alvos registrados para uva? Um produto
   registrado para a cultura pode ter um único alvo registrado nela.
4. **Dose** — compare com a dose da bula, atento à unidade: por 100 L de calda, por hectare, por planta
   ou em % v/v não são a mesma coisa. Se a conversão for necessária, apresente-a como **cálculo seu**,
   separando-a do número do documento.
5. **Volume de calda e equipamento** — a bula costuma fixar o volume por hectare para a cultura.
6. **Época ou estágio da cultura** — compare com o que a bula exige (fase fenológica, dias após a
   emergência, início das chuvas, idade da planta, estado do tronco, umidade do solo). Se a bula usa um
   vocabulário que a wiki não tem (por exemplo "30 DAE", ou "gema algodão" no sentido inverso), diga
   que a correspondência não está estabelecida em vez de traduzir por conta própria.
7. **Aplicações anteriores** — use a skill `consultar-historico-setorial` para levantar o que já foi
   aplicado no setor e quando. Conte quantas aplicações do produto foram registradas no ciclo e calcule
   os dias desde a última.
8. **Intervalo entre aplicações** — confronte o intervalo mínimo da bula com a data da última aplicação
   registrada.
9. **Número máximo de aplicações** — confronte com o registrado. Note se a bula diz "por ciclo da
   cultura", "por ano" ou não especifica; quando não especifica, diga isso.
10. **Carência (intervalo de segurança)** — compare com a previsão de colheita quando ela for conhecida.
11. **Restrições e limitações de uso** — percorra a seção da página do produto por inteiro: distância de
    corpos d'água, idade mínima da planta, tipo e umidade do solo, matéria orgânica, estresse da cultura,
    horário por causa das abelhas, intervalo de reentrada, limpeza do pulverizador.
12. **Condições ambientais** — temperatura, umidade relativa e vento exigidos. Quando os números atuais
    importarem, consulte a estação em `dados-vivos/estacao-meteorologica.md` e registre a data da
    consulta.
13. **Manejo de resistência** — se a bula exigir alternância de grupo (FRAC/IRAC/HRAC), verifique o
    grupo dos produtos das aplicações anteriores registradas.

Feche a conferência com três listas explícitas: o que **está conforme** os documentos, o que **está em
desacordo ou excede um limite documentado** e o que **não foi possível verificar** (por falta de
documento, de registro de campo, de análise de solo ou de dado ambiental).

## 5. Conferência de mistura (dois ou mais produtos na mesma operação)

Compare as informações de compatibilidade e restrição de mistura de **todos** os documentos envolvidos
e classifique o resultado em uma destas três situações, nomeando qual é:

- **Compatibilidade ou uso expressamente previsto/documentado** — algum documento autoriza aquela
  combinação, ou prevê explicitamente o tipo de produto na calda.
- **Incompatibilidade ou restrição expressamente documentada** — algum documento proíbe ou restringe.
  Inclui restrições de sequência, não só de tanque: o [[abamectin-72-ec-nortox]] veda captana, folpete e
  enxofre em uma janela de 10 dias antes e 10 dias depois, ainda que aplicados separadamente.
- **Informação insuficiente** — os documentos não tratam da combinação.

**A ausência de incompatibilidade documentada nunca é prova de compatibilidade.** Silêncio é o terceiro
caso, não o primeiro. Também não basta uma alegação genérica do fabricante: "compatível com a maioria dos
produtos fitossanitários" (frase do [[basfoliar-black-evolution-sl]]) e "para uso em mistura com
defensivos agrícolas" (frase do [[assist-ec]]) não nomeiam produto nenhum e continuam sendo o terceiro
caso quando aplicadas a uma combinação concreta.

Quando cair em informação insuficiente, diga o que resolveria: qual documento falta, ou que a decisão
cabe ao responsável técnico.

## 6. Registrar uma aplicação realizada

Uma aplicação só é registrada como **realizada** quando o usuário confirmar explicitamente que ela
ocorreu. Aplicação planejada, cogitada ou discutida **não** vira fato, não gera evento e não entra no
histórico.

Confirmada a aplicação, siga as regras de ingestão do `AGENTS.md`:

1. Crie o evento em `wiki/eventos/`, com `categoria: manejo`, as âncoras temporais obrigatórias
   (`data`, `safra`, `estagio_fenologico`, `local`, `setores`) e `fontes` apontando para a fonte da
   informação. Cite o produto pela página em `wiki/produtos/` quando ele existir na base.
2. Atualize o histórico mensal do setor em `wiki/historicos/setores/<setor>/AAAA-MM-<setor>.md`.
3. Atualize as páginas de setor, variedade, safra e [[fitossanidade]] afetadas.
4. Registre a entrada `ingest` (ou `query`, se a origem foi uma conversa) no `log.md`.
5. Não adivinhe setor, rua, data, dose ou estágio. Campo ambíguo vira `pendencia` no `log.md`.
6. Rode `python3 tools/validar-wiki.py` antes do commit.

O evento registra o fato. A conferência técnica — se a dose estava dentro da bula, se o intervalo foi
respeitado — é interpretação e vive em `wiki/correlacoes/`, `wiki/hipoteses/` ou
`wiki/recomendacoes/`, nunca embutida no evento.

## 7. Quando os documentos não bastam

Diga com precisão o que falta e qual documento resolveria. Se buscar conhecimento externo, siga a regra
do `AGENTS.md`: registre título, autoria ou instituição, URL/DOI e data da consulta, e marque com
clareza que é fonte externa. Conhecimento externo embasa interpretação; **não** cria autorização de uso
nem substitui o rótulo ou a bula.

## 8. Arquivar documentos de um produto novo

As remessas de documentos chegam em lotes e a base cresce por produto, não por arquivo.

1. Salve cada PDF em `raw/fichas-tecnicas/comercial/` (ou `biologicos/`) com nome
   `<produto-em-kebab-case>-<tipo>.pdf`, onde `<tipo>` é `bula`, `rotulo`, `fds`, `fispq` ou
   `ficha-emergencia`. Uma vez salvo, o arquivo é imutável.
2. Crie a página copiando `wiki/produtos/_modelo-produto.md`. Nomes comerciais parecidos podem ser
   produtos diferentes: compare registro MAPA, ingrediente ativo e função antes de tratar dois
   documentos como do mesmo produto.
3. Escreva as asserções da página em `tools/fidelidade/<pagina>.txt` — uma linha por dose, carência,
   limite, restrição e telefone que a página afirma, e também por cada negação ("a bula não registra
   videira"). Feche com `python3 tools/conferir-fidelidade.py`; divergência significa que a página diz
   algo que o PDF não sustenta, e quem corrige é a página, nunca a asserção.
4. Atualize o [[catalogo-produtos]] (tabelas, restrições que atravessam produtos, telefones e o estado
   da remessa), o `index.md` e o `log.md`.
5. Documento que completa um produto já catalogado resolve a lacuna registrada na página — não crie
   uma página nova para ele.
6. Rode `python3 tools/validar-wiki.py` antes do commit.
