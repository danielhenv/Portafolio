#Filtrado de datos con ORM


from reservas.models import Pedido, Producto, Cliente
from django.db.models import Sum, F

# Todos los productos(servicios) con precio mayor a 50
productos_caros = Producto.objects.filter(precio__gt=50)

# Pedidos de un cliente específico (por ID)
cliente = Cliente.objects.get(pk=1)
pedidos_cliente = Pedido.objects.filter(cliente=cliente)

# Pedidos en un rango de fechas
from datetime import datetime
inicio = datetime(2025, 1, 1)
fin = datetime(2025, 12, 31)
pedidos_en_rango = Pedido.objects.filter(fecha__range=(inicio, fin))

# Total por pedido usando annotate
totales = Pedido.objects.annotate(
    total=Sum(F('detalles__cantidad') * F('detalles__precio_unitario'))
)

#Consultas raw ()

from reservas.models import Producto

# Productos con precio menor a 100 usando SQL
productos_baratos = Producto.objects.raw(
    "SELECT id, nombre, precio, cantidad FROM reservas_producto WHERE precio < %s",
    [100]
)

for p in productos_baratos:
    print(p.nombre, p.precio)

