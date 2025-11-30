from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,        # no se borran categorías si tienen productos
        related_name="productos",
    )
    etiquetas = models.ManyToManyField(
        Etiqueta,
        blank=True,
        related_name="productos",
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} ({self.categoria.nombre})"


class DetalleProducto(models.Model):
    # Relación Uno a Uno: cada producto tiene un solo detalle
    producto = models.OneToOneField(
        Producto,
        on_delete=models.CASCADE,
        related_name="detalle",
    )
    dimensiones = models.CharField(
        max_length=100,
        blank=True,
        help_text="Ej: 10x20x5 cm",
    )
    peso = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Peso en kg",
    )

    class Meta:
        verbose_name = "Detalle de producto"
        verbose_name_plural = "Detalles de producto"

    def __str__(self):
        return f"Detalles de {self.producto.nombre}"
