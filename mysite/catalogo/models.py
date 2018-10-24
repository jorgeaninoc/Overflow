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
    nombre = models.CharField(max_length=255,null=False)
    precio=models.IntegerField(null=False)
    communidad = models.ForeignKey(Comunidad,on_delete=models.CASCADE)
    imagenes = models.ManyToManyField(Imagen,null=False)
    subCat = models.CharField(max_length=255,null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Producto"
        verbose_name_plural = "Productos"
