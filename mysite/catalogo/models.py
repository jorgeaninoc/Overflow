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

# Create your models here.


# Session id Table for User Handling
class UserSession(models.Model):
    user = models.CharField(max_length=32, null=True)


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


class Cart(models.Model):
    user = models.ForeignKey(UserSession, null=True, blank=True, on_delete='CASCADE')
    count = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User with key: {} has {} items in the cart. Total is ${}".format(self.user, self.count, self.total)


class Entry(models.Model):
    product = models.ForeignKey(Producto, null=True, on_delete='CASCADE')
    cart = models.ForeignKey(Cart, null=True, on_delete='CASCADE')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "The entry contains {} {}(s).".format(self.quantity, self.product.name)


@receiver(post_save, sender=Entry)
def update_cart(sender, instance, **kwargs):
    line_cost = instance.quantity * instance.product.cost
    instance.cart.total += line_cost
    instance.cart.count += instance.quantity
    instance.cart.updated = datetime.now()




