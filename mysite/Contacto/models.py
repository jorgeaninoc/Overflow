"""
Created by Framework
This file is where the models(Tables) of Contacto are declared.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries needed
from django.db import models
from datetime import timedelta as td
from datetime import datetime as dt
import django

# Create your models here.

# Table Contacto
class Contacto(models.Model):
    # Declare variables for table Contacto
    telefono = models.CharField(max_length=255,null=False)
    horario = models.CharField(max_length=255,null=False)
    mail = models.EmailField(null=False,unique=True)

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name: "Informacion de Contacto"
        verbose_name_plural = "Informacion de Contacto"

# Table Mensaje
class Mensaje(models.Model):
    # Declare variables for table Mensaje
    nombre =  models.CharField(max_length=255,null=False)
    correo = models.EmailField(null=False,unique=True)
    mensaje = models.TextField(max_length=255,null=False)

    # Declare function to return the name of the user sending the message
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name: "Mensaje"
        verbose_name_plural = "Mensajes"
