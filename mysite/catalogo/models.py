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

# Table Product
class Producto(models.Model):
    #Declaring variables for Table product
    nombre = models.CharField(max_length=255,null=False)
    precio=models.IntegerField(null=False)
    communidad = models.ForeignKey(Comunidad,on_delete=models.CASCADE)
    imagenes = models.ManyToManyField(Imagen,null=False)
    subCat = models.CharField(max_length=255,null=False)


    # Function to return the name of the product
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name: "Producto"
        verbose_name_plural = "Productos"
