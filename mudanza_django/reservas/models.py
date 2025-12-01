from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    TIPO_SERVICIO_CHOICES = [
        ('local', 'Mudanza local'),
        ('nacional', 'Mudanza nacional'),
        ('internacional', 'Mudanza internacional'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    fecha_mudanza = models.DateField()
    hora_mudanza = models.TimeField()
    direccion_origen = models.CharField(max_length=255)
    direccion_destino = models.CharField(max_length=255)
    tipo_servicio = models.CharField(max_length=20, choices=TIPO_SERVICIO_CHOICES)
    notas = models.TextField(blank=True)

    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Reserva #{self.id} - {self.cliente.nombre}"
    

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} (${self.precio})"
    
#Relacion OnetoOne
class PerfilCliente(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='perfil')
    biografia = models.TextField(blank=True)
    foto_perfil = models.URLField(blank=True)
    redes_sociales = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Perfil de {self.cliente.nombre}"
    

#Relacion ManytoMany

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    fecha = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"Pedido #{self.id} de {self.cliente.nombre}"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='detalles')
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en pedido #{self.pedido.id}"


