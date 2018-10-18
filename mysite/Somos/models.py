from django.db import models
from datetime import timedelta as td
from datetime import datetime as dt
import django
# Create your models here.

class Valor(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    valor = models.TextField(null=False)
    valoresImagen = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Valor"
        verbose_name_plural = "Valores"

class Somos(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    titulo = models.CharField(max_length=255,null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Titulo"
        verbose_name_plural = "Titulos"

class Historia(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    historia=models.TextField(null=False)
    historiaImagen = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Historia"
        verbose_name_plural = "Historias"



class Mision(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    mision = models.TextField(null=False)
    imagen =  models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Misión"
        verbose_name_plural = "Misiones"
