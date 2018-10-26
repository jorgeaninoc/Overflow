"""
Created by Framework
This file is where you can set the models that can be edited by the admin.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries.
from django.contrib import admin
from Actividades.models import Noticia, Imagen

# Register your models here.
admin.site.register(Noticia)
admin.site.register(Imagen)
