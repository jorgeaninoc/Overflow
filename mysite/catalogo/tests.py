"""
Created by Framework
This file is where you can create tests for the App
Modified by: Enrique Posada
Date: 03/11/18
"""
# Import libraries used.
from django.test import TestCase

from django.contrib.auth.models import User
from Catalogo.models import Producto
from datetime import datetime as dt
from datetime import timedelta as td
import django
# from django.contrib.auth.models import User
from django.test import TestCase, Client


# Create your tests here.



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

