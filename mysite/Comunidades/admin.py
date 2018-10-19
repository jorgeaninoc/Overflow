"""
Created by Framework
This file is where the models that will be edited by the admin are declared.
Modified by: Jorge Nino
Date: 19/10/18
"""
from django.contrib import admin
from Comunidades.models import Comunidad,Imagen


# Register your models here.

admin.site.register(Comunidad)
admin.site.register(Imagen)
