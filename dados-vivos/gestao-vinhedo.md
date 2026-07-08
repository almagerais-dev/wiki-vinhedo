---
tipo: dados-vivos
titulo: Software de gestão do vinhedo
banco: postgresql
atualizado_em: 2026-07-08
---

# Software de gestão do vinhedo (dados vivos)

Banco de dados da gestão do vinhedo (manejo: irrigação, adubação, pulverização, podas/desfolhas,
etc.). Consultado em tempo real; apenas sínteses vão para a wiki.

> Presumido **PostgreSQL**. Confirmar e ajustar conexão/schema quando o acesso for liberado.

## Conexão

_A preencher: host, porta, base, credenciais (via variável de ambiente/secret, nunca em texto)._

## Schema (a preencher)

Descrever tabelas e colunas relevantes, por exemplo:

- `manejo(local, quadra, data, tipo, produto, dose, ...)`

## Como o agente deve usar

- Consultar para reconstruir a linha do tempo de manejo de uma quadra/safra.
- Eventos de manejo **marcantes** viram páginas em `wiki/eventos/` (categoria `manejo`); o
  operacional de alta frequência fica no banco e é sintetizado por safra.
- Registrar data da consulta e SQL como `fontes`.
