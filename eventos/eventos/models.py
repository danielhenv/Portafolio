from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    TIPO_CHOICES = [
        ('conferencia', 'Conferencia'),
        ('concierto', 'Concierto'),
        ('seminario', 'Seminario'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, blank=True)
    es_privado = models.BooleanField(default=False)

    organizador = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='eventos_organizados'
    )

    asistentes = models.ManyToManyField(
        User,
        related_name='eventos_asistidos',
        blank=True,
    )

    def __str__(self):
        return self.titulo
