#1.1. Buscar productos por nombre (filter)

from productos.models import Producto, Categoria, Etiqueta
from django.db.models import Count, Avg
# Productos cuyo nombre contiene "lapiz"
Producto.objects.filter(nombre__icontains="lapiz")

#1.2. Buscar productos por categoría

cat = Categoria.objects.get(nombre="Electrónica")
productos_electronica = Producto.objects.filter(categoria=cat)

o

Producto.objects.filter(categoria_id=1)

#1.3. Productos con precio mayor a un valor (gt, greater than)

productos_caros = Producto.objects.filter(precio__gt=100)


#1.4. Usar exclude() (ej. excluir los baratos)

productos_no_baratos = Producto.objects.exclude(precio__lt=50)

#1.5. Anotaciones (contar productos por categoría)

categorias_con_conteo = Categoria.objects.annotate(
    num_productos=Count('productos')
)

for c in categorias_con_conteo:
    print(c.nombre, c.num_productos)

#1.6. Precio promedio de los productos

Producto.objects.all().aggregate(precio_promedio=Avg('precio'))
