-- =====================================================
-- 01_creacion_tablas.sql
-- Definición de la base de datos y tablas para App Mudanza
-- Motor: MySQL / MariaDB
-- =====================================================

-- Crear base de datos (si no existe)
CREATE DATABASE IF NOT EXISTS mudanza_db;
USE mudanza_db;

-- Tabla Cliente
CREATE TABLE IF NOT EXISTS Cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nombre     VARCHAR(100) NOT NULL,
    email      VARCHAR(100) NOT NULL UNIQUE,
    telefono   VARCHAR(20)  NOT NULL
);

-- Tabla Reserva
CREATE TABLE IF NOT EXISTS Reserva (
    id_reserva        INT PRIMARY KEY AUTO_INCREMENT,
    fecha_reserva     DATETIME NOT NULL DEFAULT NOW(),
    fecha_mudanza     DATE NOT NULL,
    hora_mudanza      TIME NOT NULL,
    direccion_origen  VARCHAR(255) NOT NULL,
    direccion_destino VARCHAR(255) NOT NULL,
    tipo_servicio     VARCHAR(50) NOT NULL,  -- local/nacional/internacional
    notas             TEXT,
    id_cliente        INT NOT NULL,
    CONSTRAINT fk_reserva_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES Cliente(id_cliente)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
