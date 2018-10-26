"""
Created by Framework
This file is where you can set the models that can be edited by the admin.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries needed
from django.contrib import admin
from Somos.models import Historia, Mision, Valor, Somos

# Register your models here.
admin.site.register(Mision)
admin.site.register(Valor)
admin.site.register(Historia)
admin.site.register(Somos)
