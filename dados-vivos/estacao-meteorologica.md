---
tipo: dados-vivos
titulo: Estação meteorológica
banco: postgresql
atualizado_em: 2026-07-08
---

# Estação meteorológica (dados vivos)

Cada local (Macaia e São Geraldo) tem estação própria. Os dados **não** são copiados para o repo:
o agente consulta em tempo real e arquiva apenas **sínteses** na wiki (ex.: resumo climático em
`wiki/safras/`).

> Presumido **PostgreSQL**. Confirmar e ajustar conexão/schema quando o acesso for liberado.

## Conexão

_A preencher: host, porta, base, credenciais (via variável de ambiente/secret, nunca em texto)._

## Schema (a preencher)

Descrever tabelas e colunas relevantes, por exemplo:

- `medicoes(local, timestamp, temp_c, umidade, chuva_mm, vento_ms, ...)`

## Como o agente deve usar

- Consultar para números atuais/históricos (temperatura, chuva, geada, veranico, graus-dia).
- Ao usar numa síntese, registrar a **data da consulta** e o SQL como `fontes` na página.
- SQL reutilizável em `dados-vivos/queries/`.
