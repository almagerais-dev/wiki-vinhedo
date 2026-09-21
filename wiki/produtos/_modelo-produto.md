---
tipo: produto
titulo: <nome comercial como aparece no rótulo>
nome_comercial: <nome comercial>
funcao: <fungicida | inseticida | acaricida | herbicida | adjuvante | fertilizante | outro>
ingredientes_ativos: []
grupo_quimico: <grupo químico declarado no documento, ou null>
codigo_resistencia: <código FRAC/IRAC/HRAC impresso no documento, ou null>
formulacao: <sigla e nome da formulação, ou null>
registro_mapa: <número, "isento" ou null>
titular_registro: <empresa, ou null>
classe_toxicologica: <categoria declarada, ou null>
classe_ambiental: <classe declarada, ou null>
registrado_para_videira: <sim | nao | nao-aplicavel | indeterminado>
culturas_registradas: []
documentos_disponiveis: [] # bula | rotulo | fds | fispq | ficha-emergencia | outro
tags: []
fontes: []
atualizado_em: <AAAA-MM-DD>
---

# <Nome comercial>

Página de produto. Sintetiza **apenas** o que está escrito nos documentos arquivados em
`raw/fichas-tecnicas/`. Cada afirmação aponta para o documento de onde saiu. Onde o documento
disponível não informa, a página registra a lacuna em vez de completar.

## Identificação

- **Registro MAPA:** …
- **Composição:** …
- **Classe / grupo químico:** …
- **Formulação:** …
- **Titular do registro:** …
- **Classificação toxicológica:** …
- **Classificação ambiental:** …

## Uso na videira

Preencher com a linha da cultura `uva`/`videira` da bula, **verbatim nos números**. Se o produto
não estiver registrado para a cultura, dizer isso explicitamente e citar a lista de culturas do
documento.

| Alvo | Dose | Nº máximo de aplicações | Intervalo entre aplicações | Volume de calda | Equipamento | Intervalo de segurança |
|---|---|---|---|---|---|---|
| … | … | … | … | … | … | … |

**Época e estágio:** …

## Outras culturas registradas

_Lista do documento, sem interpretação._

## Restrições e limitações de uso

_Extratos das limitações declaradas. Não resumir de forma a perder uma restrição._

## Compatibilidade e mistura

Classificar explicitamente em uma das três situações:

- **Documentado como compatível/previsto:** …
- **Documentado como incompatível/restrito:** …
- **Sem informação suficiente nos documentos disponíveis:** …

## Condições de aplicação e reentrada

_Temperatura, umidade, vento, intervalo de reentrada._

## Segurança e emergência

- **EPI:** …
- **Primeiros socorros:** …
- **Derramamento:** …
- **Incêndio:** …
- **Telefones:** …

Para o texto completo, abrir o documento citado. Em emergência, seguir o documento, não esta
síntese.

## Documentos disponíveis

| Documento | Arquivo | Versão/data no documento |
|---|---|---|
| … | … | … |

## Lacunas

_O que os documentos disponíveis não dizem e que documento resolveria._
