from django.contrib import admin
from .models import Categoria, Etiqueta, Producto, DetalleProducto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)


@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


class DetalleProductoInline(admin.StackedInline):
    model = DetalleProducto
    extra = 0


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio")
    list_filter = ("categoria", "etiquetas")
    search_fields = ("nombre", "descripcion")
    filter_horizontal = ("etiquetas",)
    inlines = [DetalleProductoInline]


@admin.register(DetalleProducto)
class DetalleProductoAdmin(admin.ModelAdmin):
    list_display = ("producto", "dimensiones", "peso")
