"""
Created by Framework
This file is where you can create tests for the App
Modified by: Enrique Posada
Date: 21/11/18
"""
# Import libraries used.
from django.test import TestCase, Client
from django.test import TestCase
# Import libraries that will be used.
from django.contrib.auth.models import User
from django.test import TestCase, Client
from Actividades.models import Noticia, Imagen
from Comunidades.models import Comunidad
from Catalogo.models import *
from datetime import datetime as dt
from datetime import timedelta as td
import django

from django.contrib.auth.models import User
from Catalogo.models import Producto
from datetime import datetime as dt
from datetime import timedelta as td
import django
# from django.contrib.auth.models import User
from django.test import TestCase, Client


# Create your tests here.

class ConsultCartTest(TestCase):
	def testConsultCart(self):
		self.client = Client()
		response = self.client.get('/carrito')
		self.assertEqual(response.status_code, 301)


# class CartTest(TestCase):
# 	def test_my_cart():
# 	    apple = Producto.objects.get_or_create(nombre='apple', precio=0.25)
# 	    my_cart = Cart.objects.get_or_create(user=None)

# 	    print(my_cart)
# 	    # STDOUT --> User: None has 0 items in their cart. Their total is $0.00
# 	    entry1 = Entry.objects.create(product=apple, cart=my_cart, quantity=3)

# 	    print(entry1)
# 	    # STDOUT --> This entry contains 3 apple(s)
# 	    print(my_cart)
	    # STDOUT --> User: None has 3 items in their cart. Their total is $0.75

# Test for the UC: Filter Catalogue
# Test by roles
class FilterCatalogueTest(TestCase):

    def testFilterCatalogo(self):
        """
        This function checks the objects at the communities and checks if filter works
        """
        self.client = Client()

        # Create objects to filter and save them
        imagen= Imagen.objects.create(nombre='Prueba O',path='media/images/agua.jpg')
        imagenn = Imagen.objects.get(nombre='Prueba O')
        comunidad = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
        comunidad.save()
        producto = Producto.objects.create(nombre="prod 1", precio=200, communidad = comunidad, subCat="a")
        producto.save()
        crear = Producto.objects.create(nombre="prod 2", precio=200, communidad = comunidad, subCat="a")
        crear.save()

        response = self.client.get('/catalogo/')

        #Checar que tiene 2 objetos
        self.assertEquals(response.context_data['filter'].qs.count(), 2)


        response = self.client.get('/catalogo/?nombre=1')
        #Checar que el filtro 1 solo regresa 1 objeto
        self.assertEquals(response.context_data['filter'].qs.count(), 1)
