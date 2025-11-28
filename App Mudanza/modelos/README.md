# Modelo de Datos – App Mudanza

Este directorio contiene el diagrama entidad-relación utilizado para el sistema de reservas de mudanzas. El objetivo es mostrar cómo se organiza la información y cómo se relacionan las entidades principales.

## Descripción del modelo

El sistema trabaja con dos tablas principales:

### Cliente
Guarda los datos básicos de cada persona que solicita un servicio:
- id_cliente (PK)
- nombre
- email
- teléfono

### Reserva
Registra cada solicitud de mudanza:
- id_reserva (PK)
- fecha_mudanza
- hora_mudanza
- direcciones de origen y destino
- tipo de servicio
- notas
- id_cliente (FK)

Cada cliente puede realizar varias reservas.  
La tabla `Reserva` incluye la clave foránea `id_cliente`, que permite relacionar ambos registros.

El diagrama incluido en esta carpeta representa esta relación 1 a muchos.
