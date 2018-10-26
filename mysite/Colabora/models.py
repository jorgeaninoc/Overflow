"""
Created by Framework
This file is where the models of Comunidades are declared.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries used
from django.db import models
from datetime import timedelta as td
from datetime import datetime as dt
import django
# Create your models here.
# Create a model to save the image of Colabora site
class ColaboraImagen(models.Model):
    # Declare the variables (Columns) for the table Colabora.
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    # Function to return the name of the image
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change the verbose names to spanish language
        verbose_name: "Imagen"
        verbose_name_plural = "Imagenes"

# Create a model to save the Colaborador model
class Colaborador(models.Model):
    # Declare the variables (Columns) for the table Colaborador.
    nombre= models.CharField(max_length=255,null=False)
    telefono=models.CharField(max_length=20)
    correo=models.EmailField()
    empresa=models.CharField(max_length=255)

    # Function to return the name of the image
    def __str__(self):
        return self.nombre
    # Class to change super Class attributes
    class Meta:
        # Change the verbose names to spanish language
        verbose_name: "Colaborador"
        verbose_name_plural = "Colaboradores"
