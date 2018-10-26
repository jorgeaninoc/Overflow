"""
Created by Framework
This file is where the models(Tables) of Somos are declared.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries needed
from django.db import models
from datetime import timedelta as td
from datetime import datetime as dt
import django
# Create your models here.

# Table Valor
# Create a model to save the values of the company
class Valor(models.Model):
    # Declare variables for table Valor
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    valor = models.TextField(null=False)
    valoresImagen = models.ImageField(upload_to="images")

    # Return the name of the value
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
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
