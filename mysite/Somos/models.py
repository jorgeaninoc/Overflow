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

# Table Somos
# Create a model to save the information in the page Somos.
class Somos(models.Model):
    # Declare the variables/columns of the table.
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    titulo = models.CharField(max_length=255,null=False)

    # Return the name of the model.
    def __str__(self):
        return self.nombre

    # Class to change the super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name: "Titulo"
        verbose_name_plural = "Titulos"

# Table Historia.
# Creates a model to save the history of the IAP.
class Historia(models.Model):
    # Declare the variables/columns of the table.
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    historia=models.TextField(null=False)
    historiaImagen = models.ImageField(upload_to="images")

    # Return the name of the model.
    def __str__(self):
        return self.nombre

    # Class to change the super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name: "Historia"
        verbose_name_plural = "Historias"


# Table Mision
# Creates a model to save the mission of the IAP
class Mision(models.Model):
    # Declare the variables/columns of the table
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    mision = models.TextField(null=False)
    imagen =  models.ImageField(upload_to="images")

    # Return the name of the model.
    def __str__(self):
        return self.nombre

    # Class to change the super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name: "Misión"
        verbose_name_plural = "Misiones"
