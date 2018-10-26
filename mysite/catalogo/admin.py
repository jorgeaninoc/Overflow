"""
Created by Framework
This file is where you can set the models that can be edited by the admin.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries used.
from django.contrib import admin
from Catalogo.models import Producto, Imagen

# Register your models here.
admin.site.register(Producto)
admin.site.register(Imagen)
