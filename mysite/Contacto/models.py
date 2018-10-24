from django.db import models
from datetime import timedelta as td
from datetime import datetime as dt
import django

# Create your models here.
class Contacto(models.Model):
    telefono = models.CharField(max_length=255,null=False)
    horario = models.CharField(max_length=255,null=False)
    mail = models.EmailField(null=False)

    class Meta:
        verbose_name: "Informacion de Contacto"
        verbose_name_plural = "Informacion de Contacto"

class Mensaje(models.Model):
    nombre =  models.CharField(max_length=255,null=False)
    correo = models.EmailField(null=False)
    mensaje = models.TextField(max_length=255,null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Mensaje"
        verbose_name_plural = "Mensajes"
