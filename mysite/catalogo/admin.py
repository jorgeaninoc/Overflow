"""
Created by Framework
This file is where you can set the models that can be edited by the admin.
Modified by: Enrique Posada
Date: 03/11/18
"""
# Import libraries used.
from django.contrib import admin
from Catalogo.models import Producto, Imagen, Ordenes

from django.utils.datetime_safe import datetime



# class EntryAdmin(admin.ModelAdmin):
#     # Overide of the save model
#     def save_model(self, request, obj, form, change):
#         obj.cart.total += obj.quantity * obj.product.cost
#         obj.cart.count += obj.quantity
#         obj.cart.updated = datetime.now()
#         obj.cart.save()
#         super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Producto)
admin.site.register(Imagen)

admin.site.register(Ordenes)

# admin.site.register(Cart)
# admin.site.register(Entry, EntryAdmin)