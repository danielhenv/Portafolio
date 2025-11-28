-- =====================================================
-- 03_consultas_reportes.sql
-- Consultas SELECT / WHERE / JOIN / GROUP BY
-- =====================================================

USE mudanza_db;

-- 1) Todas las reservas de un cliente específico (por email)
SELECT
    r.id_reserva,
    c.nombre AS nombre_cliente,
    r.fecha_mudanza,
    r.hora_mudanza,
    r.direccion_origen,
    r.direccion_destino,
    r.tipo_servicio,
    r.notas
FROM Reserva r
JOIN Cliente c ON r.id_cliente = c.id_cliente
WHERE c.email = 'ana.perez@example.com';

-- 2) Reservas programadas para una fecha específica
SELECT
    r.id_reserva,
    c.nombre AS nombre_cliente,
    r.hora_mudanza,
    r.direccion_origen,
    r.direccion_destino,
    r.tipo_servicio
FROM Reserva r
JOIN Cliente c ON r.id_cliente = c.id_cliente
WHERE r.fecha_mudanza = '2025-09-01';

-- 3) Total de reservas por cliente (GROUP BY)
SELECT
    c.id_cliente,
    c.nombre,
    c.email,
    COUNT(r.id_reserva) AS total_reservas
FROM Cliente c
LEFT JOIN Reserva r ON c.id_cliente = r.id_cliente
GROUP BY c.id_cliente, c.nombre, c.email
ORDER BY total_reservas DESC;

-- 4) Total de reservas por tipo de servicio
SELECT
    tipo_servicio,
    COUNT(*) AS total_reservas
FROM Reserva
GROUP BY tipo_servicio
ORDER BY total_reservas DESC;

-- 5) Próximas mudanzas (a partir de hoy) ordenadas por fecha y hora
SELECT
    r.id_reserva,
    c.nombre AS nombre_cliente,
    r.fecha_mudanza,
    r.hora_mudanza,
    r.direccion_origen,
    r.direccion_destino,
    r.tipo_servicio
FROM Reserva r
JOIN Cliente c ON r.id_cliente = c.id_cliente
WHERE r.fecha_mudanza >= CURDATE()
ORDER BY r.fecha_mudanza, r.hora_mudanza;
