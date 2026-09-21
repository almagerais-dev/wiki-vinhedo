#!/usr/bin/env python3
"""Confere se cada número escrito em `wiki/produtos/` consta do PDF arquivado em `raw/`.

O `validar-wiki.py` verifica a *estrutura* das páginas. Este script verifica a *fidelidade*: para
cada afirmação de uma página de produto (dose, carência, número de aplicações, telefone, restrição),
uma linha de asserção aponta o PDF e o trecho que precisa estar escrito nele. Se o trecho não
aparece, a página afirma algo que a fonte não sustenta.

As asserções ficam em `tools/fidelidade/<pagina>.txt`, um arquivo por página de produto, no formato:

    arquivo.pdf | presente | o que a wiki afirma | trecho que precisa constar do PDF
    arquivo.pdf | ausente  | o que a wiki nega   | trecho que NÃO pode constar do PDF

`ausente` existe porque negar também é afirmar: dizer "a bula não registra videira" só se sustenta se
a palavra realmente não estiver no documento. Um trecho entre barras (`/\buvas?\b/`) é lido como
expressão regular sem diferenciar maiúsculas, o que serve para negar uma palavra inteira sem cair em
"chuva" ou "luvas". Linhas em branco e as que começam com `#` são ignoradas.

Cuidado ao escrever o trecho: a busca literal é por substring, então `500 g/100 L` casa dentro de
`2500 g/100 L` e diria que a dose está no documento quando não está. Inclua contexto suficiente
(a cultura, o alvo, a unidade) ou use expressão regular com `\b` quando o número puder ser sufixo de
outro.

O texto do PDF é extraído nos dois modos do `pdftotext` (ordem de leitura e `-layout`) e os espaços
são colapsados, porque tabelas em colunas embaralham a ordem das células de um modo ou de outro. Uma
asserção `presente` passa se o trecho aparece em qualquer um dos modos; uma `ausente` só passa se o
trecho não aparece em nenhum deles.

Uso:
    python3 tools/conferir-fidelidade.py              # confere todas as páginas
    python3 tools/conferir-fidelidade.py aliette      # confere apenas as páginas citadas

Sai com código 1 se houver divergência, página de produto sem arquivo de asserções ou asserção
apontando para PDF inexistente. Requer o `pdftotext` (pacote `poppler-utils`).
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PDFS = RAIZ / "raw/fichas-tecnicas"
ASSERCOES = Path(__file__).resolve().parent / "fidelidade"
PAGINAS = RAIZ / "wiki/produtos"
# páginas de wiki/produtos/ que não descrevem um produto e por isso não têm asserções
NAO_SAO_PRODUTOS = {"_modelo-produto", "catalogo-produtos"}
MODOS = {"presente", "ausente"}

erros: list[str] = []
cache: dict[Path, tuple[str, str]] = {}


def texto(pdf: Path) -> tuple[str, str]:
    """Devolve o texto do PDF na ordem de leitura e no modo -layout, com espaços colapsados."""
    if pdf not in cache:
        extraidos = []
        for argumentos in ([], ["-layout"]):
            saida = subprocess.run(
                ["pdftotext", *argumentos, str(pdf), "-"],
                capture_output=True, text=True, check=True,
            )
            extraidos.append(re.sub(r"\s+", " ", saida.stdout))
        cache[pdf] = (extraidos[0], extraidos[1])
    return cache[pdf]


def localizar_pdf(nome: str) -> Path | None:
    achados = sorted(PDFS.rglob(nome))
    return achados[0] if achados else None


def assercoes_de(arquivo: Path) -> list[tuple[str, str, str, str]]:
    linhas = []
    for numero, linha in enumerate(arquivo.read_text(encoding="utf-8").splitlines(), start=1):
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue
        partes = [parte.strip() for parte in linha.split("|", 3)]
        if len(partes) != 4:
            erros.append(f"{arquivo.relative_to(RAIZ)}:{numero}: esperado 4 campos separados por '|'")
            continue
        pdf, modo, afirmacao, agulha = partes
        if modo not in MODOS:
            erros.append(
                f"{arquivo.relative_to(RAIZ)}:{numero}: modo '{modo}' desconhecido "
                f"(use {' ou '.join(sorted(MODOS))})"
            )
            continue
        linhas.append((pdf, modo, afirmacao, agulha))
    return linhas


def conferir(arquivo: Path) -> tuple[int, int]:
    conferidas = divergencias = 0
    print(f"\n{arquivo.stem}")
    for nome_pdf, modo, afirmacao, agulha in assercoes_de(arquivo):
        pdf = localizar_pdf(nome_pdf)
        if pdf is None:
            erros.append(f"{arquivo.relative_to(RAIZ)}: PDF '{nome_pdf}' não existe em raw/")
            continue
        extraidos = texto(pdf)
        alvo = re.sub(r"\s+", " ", agulha)
        if alvo.startswith("/") and alvo.endswith("/") and len(alvo) > 2:
            padrao = re.compile(alvo[1:-1], re.IGNORECASE)
            achou = any(padrao.search(extraido) for extraido in extraidos)
        elif modo == "presente":
            achou = any(alvo in extraido for extraido in extraidos)
        else:
            # negar um conceito não depende da caixa em que o documento o escreveu
            achou = any(alvo.lower() in extraido.lower() for extraido in extraidos)
        ok = achou if modo == "presente" else not achou
        conferidas += 1
        if not ok:
            divergencias += 1
            erros.append(
                f"{arquivo.relative_to(RAIZ)}: {nome_pdf} não sustenta '{afirmacao}' "
                f"({modo}: {agulha!r})"
            )
        print(f"  {'ok     ' if ok else 'DIVERGE'} {nome_pdf:45} {afirmacao}")
    return conferidas, divergencias


def main() -> int:
    if shutil.which("pdftotext") is None:
        print("pdftotext não encontrado. Instale o poppler-utils para conferir os PDFs.")
        return 1

    pedidos = {argumento.removesuffix(".md") for argumento in sys.argv[1:]}
    paginas = {
        caminho.stem for caminho in PAGINAS.glob("*.md") if caminho.stem not in NAO_SAO_PRODUTOS
    }
    if pedidos:
        desconhecidas = pedidos - paginas
        if desconhecidas:
            print(f"páginas inexistentes em wiki/produtos/: {', '.join(sorted(desconhecidas))}")
            return 1
        paginas = pedidos

    conferidas = divergencias = 0
    for pagina in sorted(paginas):
        arquivo = ASSERCOES / f"{pagina}.txt"
        if not arquivo.exists():
            erros.append(
                f"wiki/produtos/{pagina}.md não tem asserções em "
                f"tools/fidelidade/{pagina}.txt — os números da página não estão conferidos"
            )
            continue
        parciais = conferir(arquivo)
        conferidas += parciais[0]
        divergencias += parciais[1]

    print(f"\n{conferidas} afirmações conferidas contra os PDFs; {divergencias} divergências.")
    if erros:
        print(f"\n{len(erros)} problema(s):")
        for erro in erros:
            print(f"  - {erro}")
        return 1
    print("Nenhuma divergência.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
