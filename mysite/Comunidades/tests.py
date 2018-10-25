"""
Created by Framework
This file is where the tests of Comunidades are declared.
Modified by: Jorge Nino
Date: 19/10/18
"""
from django.test import TestCase, Client
from Comunidades.models import Comunidad,Imagen

# Create your tests here.

class AddCommunitiesTest(TestCase):

    def testCreateCommunity(self):
        i= Imagen.objects.create(nombre='Prueba I',path='media/images/agua.jpg')
        im = Imagen.objects.get(nombre='Prueba I')
        c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
        c.imagenes.add(im)
        co = Comunidad.objects.get(nombre='Prueba C')
        return co

    def testAddCommunities(self):
        w = self.testCreateCommunity()
        self.assertTrue(isinstance(w, Comunidad))

class EditCommunitiesTest(TestCase):
    def testCreateCommunity(self):
        i= Imagen.objects.create(nombre='Prueba I',path='media/images/agua.jpg')
        im = Imagen.objects.get(nombre='Prueba I')
        c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
        c.imagenes.add(im)
        co = Comunidad.objects.get(nombre='Prueba C')
        return co

    def testEditCommunities(self):
        c = self.testCreateCommunity()
        c.nombre='Prueba E'
        self.assertTrue(c.nombre,'Prueba E')

class DeleteCommunitiesTest(TestCase):
    def testCreateCommunity(self):
        i= Imagen.objects.create(nombre='Prueba I',path='media/images/agua.jpg')
        im = Imagen.objects.get(nombre='Prueba I')
        c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
        c.imagenes.add(im)
        co = Comunidad.objects.get(nombre='Prueba C')
        return co

    def testDeleteCommunities(self):
        c = self.testCreateCommunity()
        c.delete()
        self.assertTrue(c,None)
