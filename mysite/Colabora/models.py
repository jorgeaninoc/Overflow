from django.db import models
from datetime import timedelta as td
from datetime import datetime as dt
import django
# Create your models here.
class ColaboraImagen(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Imagen"
        verbose_name_plural = "Imagenes"

class Colaborador(models.Model):
    nombre= models.CharField(max_length=255,null=False)
    telefono=models.CharField(max_length=20)
    correo=models.EmailField()
    empresa=models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Colaborador"
        verbose_name_plural = "Colaboradores"
