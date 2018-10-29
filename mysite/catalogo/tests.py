"""
Created by Framework
This file is where you can create tests for the App
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries used.
from django.test import TestCase

# Create your tests here.

# Test for the UC: Filter Catalogue
# Test by roles
class FilterCatalogueTest(TestCase):

    def testFilterCommunities(self):
        """
        This function checks the objects at the communities and checks if filter works
        """
        self.client = Client()

        # Create objects to filter and save them
        i= Imagen.objects.create(nombre='Prueba O',path='media/images/agua.jpg')
        im = Imagen.objects.get(nombre='Prueba O')
        c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
        co = Comunidad.objects.get(nombre='Prueba C')
        c = Producto.objects.create(nombre="p1", precio=200, communidad = co, imagenes=(im,), subcat="a")
        c.save()
        d = Producto.objects.create(nombre="p2", precio=200, communidad = co, imagenes=(im,), subcat="a")
        d.save()

        response = client.get('/catalogo/')

        #Checar que tiene 2 objetos
        self.assertEquals(response.context_data['filter'].qs.count, 2)


        response = client.get('/catalogo/?nombre=1')
        #Checar que el filtro 1 solo regresa 1 objeto
        self.assertEquals(response.context_data['filter'].qs.count, 1)
