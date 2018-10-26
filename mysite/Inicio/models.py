"""
Created by Framework
This file is where the models(Tables) of Inicio are declared.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries needed
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
# Create a model to save the images from the index
class InicioImagen(models.Model):
    # Declare variables for table InicioImagen
    nombre = models.CharField(max_length=255,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    # Return the name of the image
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name: "Imagen de Inicio"
        verbose_name_plural = "Imagenes de Inicio"
        #app_label = 'Inicio'

# Create a model to save the images of the galery of the index
class GaleriaImagen(models.Model):
    # Declare variables for table GaleriaImagen
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    # Return the name of the image
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name: "Imagen de Galeria"
        verbose_name_plural = "Imagenes de Galeria"

# Create a model to save the announcements of the index
class Anuncio(models.Model):
    # Declare variables for table Anuncio
    titulo = models.CharField(max_length=255,null=False)
    texto = models.TextField(null=False)
    imagen = models.ImageField(upload_to="images")

    # Return the title of the announcement
    def __str__(self):
        return self.titulo

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name: "Anuncio"
        verbose_name_plural = "Anuncios"

# Table Video
# Create a model to save the video of the index
class Video(models.Model):
    # Declare variables for table Video
    url = models.CharField(max_length=255,unique=True,null=False)

    # Return the title of the announcement
    def __str__(self):
        return self.url

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name: "Video"
        verbose_name_plural = "Videos"
