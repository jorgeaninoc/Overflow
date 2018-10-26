"""
Created by Framework
This file is where you can create tests for the App
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries that will be used.
from django.contrib.auth.models import User
from django.test import TestCase, Client
from Actividades.models import Noticia, Imagen
from Comunidades.models import Comunidad
from datetime import datetime as dt
from datetime import timedelta as td
import django

# Create your tests here.

# Test for UC: Consult News
class ConsultNewsTest(TestCase):
    # Function that will be tested.
    def testConsultNews(self):
        # Get a client copy.
        self.client = Client()
        # Get the site from /actividades
        response = self.client.get('/actividades')
        # Check if the code return is 301 for success.
        self.assertEqual(response.status_code, 301)

    def testConsultNewsFalse(self):
        # Get a client copy.
        self.client = Client()
        # Get the site from /actividades
        response = self.client.get('/actividades2')
        # Check if the code return is 404 for failure
        self.assertEqual(response.status_code, 404)


# Test for UC: Add News
class AddNewsTest(TestCase):

    # This function creates a Notice object in DB and returns it
    def testCreateNews(self):
        i= Imagen.objects.create(nombre='Prueba O',path='media/images/agua.jpg')
        im = Imagen.objects.get(nombre='Prueba O')
        c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
        co = Comunidad.objects.get(nombre='Prueba C')
        n = Noticia.objects.create(titulo='Prueba', texto='Lorem Ipsum',
        fechaInicio=django.utils.timezone.now(), fechaFin=django.utils.timezone.now()
        + django.utils.timezone.timedelta(30),comunidad=co)
        n.imagenes.add(im)
        return n

    # This function calls the function testCreateNews to create a Notice object
    # And checks if the object is an instance from Notice
    def testAddNews(self):
        w = self.testCreateNews()
        self.assertTrue(isinstance(w, Noticia))

# Test for UC: Edit News
class EditNewsTest(TestCase):
    # This function creates a Notice object in the DB and returns it.
    def testCreateNews(self):
        i= Imagen.objects.create(nombre='Prueba O',path='media/images/agua.jpg')
        im = Imagen.objects.get(nombre='Prueba O')
        c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
        co = Comunidad.objects.get(nombre='Prueba C')
        n = Noticia.objects.create(titulo='Prueba', texto='Lorem Ipsum',
        fechaInicio=django.utils.timezone.now(), fechaFin=django.utils.timezone.now() + django.utils.timezone.timedelta(30)
        ,comunidad=co)
        n.imagenes.add(im)
        return n

    # This function changes a parameter of the Notice object and checks if the
    # changes are saved.
    def testEditNews(self):
        w = self.testCreateNews()
        w.titulo = 'Prueba N'
        self.assertTrue(w.titulo,'Prueba N')
