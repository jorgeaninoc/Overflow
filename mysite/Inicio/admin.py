"""
Created by Framework
This file is where you can set the models that can be edited by the admin.
Modified by: Jorge Nino
Date: 19/10/18
"""
from django.contrib import admin
from Inicio.models import Anuncio,InicioImagen,GaleriaImagen, Video
# Register your models here.
admin.site.register(Anuncio)
admin.site.register(InicioImagen)
admin.site.register(GaleriaImagen)
admin.site.register(Video)
