"""
Created by Framework
This file is where you can declare the models (tables) of the DB
Modified by: Jorge Nino
Date: 19/10/18
"""

#Import libraries that will be used
from django.db import models
from datetime import timedelta as td
from datetime import datetime as dt
from Comunidades.models import Comunidad
import django

# Declaring Table Image
class Imagen(models.Model):
    #Declaring variables for Table image
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    #Checking the vulnerability:
    #path = models.ImageField(upload_to="images")
    path = models.ImageField(upload_to="images")

    # Function to return the name of the Image
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name: "Imagen"
        verbose_name_plural = "Imagenes"



# Table Notice
class Noticia(models.Model):
    # Declare columns of the table notice
    titulo = models.CharField(max_length=255,null=False)
    texto = models.TextField(null=False)
    fechaInicio = models.DateField(default=django.utils.timezone.now())
    fechaFin = models.DateField(default=django.utils.timezone.now() + django.utils.timezone.timedelta(30))
    comunidad = models.ForeignKey(Comunidad,on_delete=models.CASCADE)
    imagenes = models.ManyToManyField(Imagen)

    # Declare function to show the name of the Table notice
    def __str__(self):
        return self.titulo

    # Class to change super class attributes
    class Meta:
        # Change verbose name of the admin site to spanish
        verbose_name: "Actividad"
        verbose_name_plural = "Actividades"
