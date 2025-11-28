-- =====================================================
-- 02_datos_ejemplo.sql
-- Inserción, actualización y eliminación de datos
-- =====================================================

USE mudanza_db;

-- INSERT: algunos clientes de ejemplo
INSERT INTO Cliente (nombre, email, telefono)
VALUES
('Ana Pérez',  'ana.perez@example.com',  '+56911111111'),
('Luis Gómez', 'luis.gomez@example.com', '+56922222222'),
('María López','maria.lopez@example.com','+56933333333');

-- INSERT: algunas reservas de ejemplo
INSERT INTO Reserva (
    fecha_mudanza,
    hora_mudanza,
    direccion_origen,
    direccion_destino,
    tipo_servicio,
    notas,
    id_cliente
)
VALUES
('2025-09-01', '09:00:00', 'Calle Roble 123, Santiago', 'Av. Las Flores 789, Santiago',
 'local', 'Cliente con mascotas, requiere cuidado especial', 1),

('2025-09-10', '14:30:00', 'Av. Central 456, Santiago', 'Calle Norte 321, Valparaíso',
 'nacional', 'Mudanza de oficina, varios equipos electrónicos', 2),

('2025-09-15', '08:00:00', 'Pasaje Sur 789, Santiago', 'Calle Este 654, Santiago',
 'local', NULL, 1);

-- UPDATE: actualizar el teléfono de un cliente
UPDATE Cliente
SET telefono = '+56999999999'
WHERE email = 'ana.perez@example.com';

-- UPDATE: cambiar la hora de una mudanza
UPDATE Reserva
SET hora_mudanza = '10:00:00'
WHERE id_reserva = 1;

-- DELETE: eliminar una reserva que fue cancelada (ejemplo)
DELETE FROM Reserva
WHERE id_reserva = 2;
