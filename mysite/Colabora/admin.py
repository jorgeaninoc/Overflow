"""
Created by Framework
This file is where you can set the models that can be edited by the admin.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import the libraries used.
from django.contrib import admin
from Colabora.models import ColaboraImagen, Colaborador

# Register your models here.
admin.site.register(ColaboraImagen)
admin.site.register(Colaborador)
