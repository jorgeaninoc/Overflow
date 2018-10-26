"""
Created by Framework
This file is where the tests of Comunidades are declared.
Modified by: Jorge Nino
Date: 19/10/18
"""
#Import libraries used.
from django.test import TestCase, Client
from Comunidades.models import Comunidad,Imagen

# Create your tests here.

# Test for UC: Consult News
class ConsultCommunitiesTest(TestCase):
    # Function that will be tested.
    def testConsultNews(self):
        # Get a client copy.
        self.client = Client()
        # Get the site from /actividades
        response = self.client.get('/comunidades')
        # Check if the code return is 301 for success.
        self.assertEqual(response.status_code, 301)

    def testConsultCommunitiesFalse(self):
        # Get a client copy.
        self.client = Client()
        # Get the site from /actividades
        response = self.client.get('/comunidades2')
        # Check if the code return is 404 for failure
        self.assertEqual(response.status_code, 404)




# Test for the UC: Add Communities
# Test by roles
class AddCommunitiesTest(TestCase):

    def testCreateCommunity(self):
        """
        This function creates an object Imagen and passes it to Comunidad, it returns the object Comunidad
        """
        i= Imagen.objects.create(nombre='Prueba I',path='media/images/agua.jpg')
        im = Imagen.objects.get(nombre='Prueba I')
        c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
        c.imagenes.add(im)
        co = Comunidad.objects.get(nombre='Prueba C')
        return co

    def testAddCommunities(self):
        """
        This function calls the function to create the object Comunidad and checks if it is an instance of Comunidad.
        """
        w = self.testCreateCommunity()
        # Check if the community exists in the DB
        self.assertEqual(w,Comunidad.objects.get(nombre='Prueba C', descripcion='Lorem Ipsum'))

# Test for CU: Edit Communities
class EditCommunitiesTest(TestCase):

    def testCreateCommunity(self):
        """
        This function creates an object Imagen and passes it to Comunidad, it returns the object Comunidad
        Returns nothing.
        """
        i= Imagen.objects.create(nombre='Prueba I',path='media/images/agua.jpg')
        im = Imagen.objects.get(nombre='Prueba I')
        c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
        c.imagenes.add(im)
        co = Comunidad.objects.get(nombre='Prueba C')
        return co

    def testEditCommunities(self):
        """
        This function calls the function to create the object Comunidad and changes a value from it, then checks if the value is the same as tested.
        Returns nothing.
        """
        c = self.testCreateCommunity()
        c.nombre='Prueba E'
        self.assertTrue(c.nombre,'Prueba E')

# Test for the CU: Delete Community
class DeleteCommunitiesTest(TestCase):
    def testCreateCommunity(self):
        """
        This function creates an object Imagen and passes it to Comunidad, it returns the object Comunidad
        Returns nothing.
        """
        i= Imagen.objects.create(nombre='Prueba I',path='media/images/agua.jpg')
        im = Imagen.objects.get(nombre='Prueba I')
        c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
        c.imagenes.add(im)
        co = Comunidad.objects.get(nombre='Prueba C')
        return co

    def testDeleteCommunities(self):
        """
        This function calls the function to create the object Comunidad and deletes it, then checks if it was deleted.
        """
        c = self.testCreateCommunity()
        c.delete()
        # Check if it was deleted from the BD.
        self.assertTrue(c,None)
