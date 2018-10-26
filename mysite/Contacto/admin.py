"""
Created by Framework
This file is where the models that will be edited by the admin are declared.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries needed
from django.contrib import admin
from Contacto.models import Contacto, Mensaje

# Register your models here.
admin.site.register(Contacto)
admin.site.register(Mensaje)
