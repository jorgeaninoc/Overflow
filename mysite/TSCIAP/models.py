from django.db import models
from datetime import timedelta as td
from datetime import datetime as dt
import django


# Create your models here.

# Table Image
class Imagen(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

# Table Community
class Comunidad(models.Model):
    nombre = models.CharField(max_length=255,unique=True)
    descripcion = models.TextField(null=False)
    imagenes = models.ManyToManyField(Imagen)

    def __str__(self):
        return self.nombre

# Table Product
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio=models.IntegerField()
    communidad = models.ForeignKey(Comunidad,on_delete=models.CASCADE)
    imagenes = models.ManyToManyField(Imagen)

    def __str__(self):

        return self.nombre

# Table Notice
class Noticia(models.Model):
    titulo = models.CharField(max_length=255,null=False)
    texto = models.TextField(null=False)
    fechaInicio = models.DateField(default=django.utils.timezone.now())
    fechaFin = models.DateField(default=django.utils.timezone.now() + django.utils.timezone.timedelta(30))
    comunidad = models.ForeignKey(Comunidad,on_delete=models.CASCADE)
    imagenes = models.ManyToManyField(Imagen)

    def __str__(self):
        return self.titulo


# Table Video
class Video(models.Model):
    url = models.CharField(max_length=255,unique=True,null=False)

    def __str__(self):
        return self.url

# Table IndexImages
class InicioImagen(models.Model):
    path = models.ImageField(upload_to="images")


class GaleriaImagen(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre
