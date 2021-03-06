"""
Created by Framework
This file is where you can declare the models (tables) of the DB
Modified by: Enrique Posada
Date: 03/11/18
"""
#Import libraries that will be used
from django.db import models
from datetime import timedelta as td
from datetime import datetime as dt
from Comunidades.models import Comunidad
import django

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid

# Create your models here.


# Session id Table for User Handling
# class UserSession(models.Model):
#     user = models.CharField(max_length=32, null=True)


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
    descripcion = models.CharField(max_length=255, default = '')
    subCat = models.CharField(max_length=255,null=False)


    # Function to return the name of the product
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name: "Producto"
        verbose_name_plural = "Productos"


class ProductosCheckout(models.Model):
    nombre_producto = models.CharField(max_length = 255, null = False)
    cantidad = models.IntegerField(null = False)
    total = models.FloatField(null = False)

    # Function to return the name of the product
    def __str__(self):
        return self.nombre_producto

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name: "ProductoCheckout"
        verbose_name_plural = "ProductosCheckout"


class Ordenes(models.Model):
    # Falta Generar el numero al azar de la referencia
    numero_referencia = models.UUIDField(default = uuid.uuid4, editable = True)
    nombre =  models.CharField(max_length=255,null=False)
    correo = models.EmailField(null=False)

    productos = models.ManyToManyField(ProductosCheckout, null = False)

    monto_totalcompra = models.CharField(max_length = 255, null = False, default = '0')

    # productos = models.ManyToManyField(ProductosCheckout, null = False)

    # productos = models....
    Fecha_de_Compra = models.DateTimeField(auto_now_add=True, null = False, editable = True)

    # readonly_fields=('numero_referencia', 'Fecha_de_Compra',)


    # fields = ['numero_referencia', 'nombre', 'correo', 'Fecha_de_Compra']
    # readonly = ['numero_referencia', 'Fecha_de_Compra']

    # Declare function to return the name of the user sending the message
    def __str__(self):
        return self.correo

    class Meta:
        # Change verbose names to spanish language
        verbose_name: "Orden Pendiente"
        verbose_name_plural = "Ordenes Pendientes"
    # Falta declarar un espacio de almacenmamiento para el diccionario
    #     ya sea guardar por separado cantidad o juntarlo todo




# Se va a tener que hacer una tabla que represente las ordenes hechas por usuarios con un numero aleatorio como referencia de compra y un apartado para almacenar todo los productos del carrito



# class Cart(models.Model):
#     user = models.ForeignKey(UserSession, null=True, blank=True, on_delete='CASCADE')
#     count = models.PositiveIntegerField(default=0)
#     total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
#     updated = models.DateTimeField(auto_now=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return "User with key: {} has {} items in the cart. Total is ${}".format(self.user, self.count, self.total)


# class Entry(models.Model):
#     product = models.ForeignKey(Producto, null=True, on_delete='CASCADE')
#     cart = models.ForeignKey(Cart, null=True, on_delete='CASCADE')
#     quantity = models.PositiveIntegerField()

#     def __str__(self):
#         return "The entry contains {} {}(s).".format(self.quantity, self.product.name)


# @receiver(post_save, sender=Entry)
# def update_cart(sender, instance, **kwargs):
#     line_cost = instance.quantity * instance.product.cost
#     instance.cart.total += line_cost
#     instance.cart.count += instance.quantity
#     instance.cart.updated = datetime.now()
