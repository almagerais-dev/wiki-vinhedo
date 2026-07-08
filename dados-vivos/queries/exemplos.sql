-- SQL reutilizável para os bancos vivos (PostgreSQL presumido).
-- Ajustar nomes de tabelas/colunas quando o schema real for confirmado.

-- [estacao] Chuva acumulada por mês para um local/safra
-- SELECT date_trunc('month', timestamp) AS mes, SUM(chuva_mm) AS chuva
-- FROM medicoes
-- WHERE local = :local AND timestamp BETWEEN :inicio AND :fim
-- GROUP BY 1 ORDER BY 1;

-- [estacao] Graus-dia (base 10) por dia
-- SELECT date_trunc('day', timestamp) AS dia,
--        GREATEST(AVG(temp_c) - 10, 0) AS graus_dia
-- FROM medicoes
-- WHERE local = :local AND timestamp BETWEEN :inicio AND :fim
-- GROUP BY 1 ORDER BY 1;

-- [gestao] Linha do tempo de manejo de uma quadra
-- SELECT data, tipo, produto, dose
-- FROM manejo
-- WHERE local = :local AND quadra = :quadra
-- ORDER BY data;
