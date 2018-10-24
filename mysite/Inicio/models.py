from django.db import models
from datetime import timedelta as td
from datetime import datetime as dt
import django
# Create your models here.

# Declaring Table Image
class Imagen(models.Model):
    #Declaring variables for Table image
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    # Function to return the name of the Image
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name: "Imagen"
        verbose_name_plural = "Imagenes"


# Table IndexImages
class InicioImagen(models.Model):
    nombre = models.CharField(max_length=255,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Imagen de Inicio"
        verbose_name_plural = "Imagenes de Inicio"
        #app_label = 'Inicio'


class GaleriaImagen(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Imagen de Galeria"
        verbose_name_plural = "Imagenes de Galeria"

class Anuncio(models.Model):
    titulo = models.CharField(max_length=255,null=False)
    texto = models.TextField(null=False)
    imagen = models.ImageField(upload_to="images")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name: "Anuncio"
        verbose_name_plural = "Anuncios"

# Table Video
class Video(models.Model):
    url = models.CharField(max_length=255,unique=True,null=False)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name: "Video"
        verbose_name_plural = "Videos"
