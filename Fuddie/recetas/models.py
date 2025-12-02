from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=200)
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True)

    def __str__(self):
        return self.nombre
