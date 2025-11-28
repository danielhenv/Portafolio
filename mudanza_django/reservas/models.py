from django.db import models
from django.contrib.auth.models import User

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

