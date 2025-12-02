from django.contrib import admin
from .models import Cliente, Reserva, Producto


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')
    list_per_page = 20


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha_mudanza', 'hora_mudanza', 'tipo_servicio')
    list_filter = ('tipo_servicio', 'fecha_mudanza')
    search_fields = ('cliente__nombre', 'direccion_origen', 'direccion_destino')
    date_hierarchy = 'fecha_mudanza'
    list_per_page = 20

