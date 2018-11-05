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
        response = self.client.get('/actividades/')
        # Check if the code return is 301 for success.
        self.assertEqual(response.status_code, 200)

    def testConsultNewsFalse(self):
        # Get a client copy.
        self.client = Client()
        # Get the site from /actividades
        response = self.client.get('/actividades10')
        # Check if the code return is 404 for failure
        self.assertEqual(response.status_code, 404)


# Test for UC: Add News
class AddNewsTest(TestCase):

    # This function calls the function testCreateNews to create a Notice object
    # And checks if the object is an instance from Notice
    def testAddNewsAdmin(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            i= Imagen.objects.create(nombre='Prueba O',path='media/images/agua.jpg')
            im = Imagen.objects.get(nombre='Prueba O')
            c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
            co = Comunidad.objects.get(nombre='Prueba C')
            n = Noticia.objects.create(titulo='Prueba', texto='Lorem Ipsum',
            fechaInicio=django.utils.timezone.now(), fechaFin=django.utils.timezone.now()
            + django.utils.timezone.timedelta(30),comunidad=co)
            n.imagenes.add(im)
            n.save()
            c = Noticia.objects.get(titulo='Prueba')
        self.assertEqual(n,c)

    def testAddNewsAdminFalse2(self):
        """
        This tests create an object and compares it with a second one to check if they are not the same
        """
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            i= Imagen.objects.create(nombre='Prueba O',path='media/images/agua.jpg')
            im = Imagen.objects.get(nombre='Prueba O')
            c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
            co = Comunidad.objects.get(nombre='Prueba C')
            n = Noticia.objects.create(titulo='Prueba', texto='Lorem Ipsum',
            fechaInicio=django.utils.timezone.now(), fechaFin=django.utils.timezone.now()
            + django.utils.timezone.timedelta(30),comunidad=co)
            n2 = Noticia.objects.create(titulo='Prueba B', texto='Lorem Ipsum',
            fechaInicio=django.utils.timezone.now(), fechaFin=django.utils.timezone.now()
            + django.utils.timezone.timedelta(30),comunidad=co)
            n.imagenes.add(im)
            n.save()
            c = Noticia.objects.get(titulo='Prueba')
        self.assertNotEqual(n,n2)

    def testAddNewsAdminFalse(self):
        """
        This test tries to add an activity as an anonymous user, if it fails it returns correct
        """
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            i= Imagen.objects.create(nombre='Prueba O',path='media/images/agua.jpg')
            im = Imagen.objects.get(nombre='Prueba O')
            c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
            co = Comunidad.objects.get(nombre='Prueba C')
            n = Noticia.objects.create(titulo='Prueba', texto='Lorem Ipsum',
            fechaInicio=django.utils.timezone.now(), fechaFin=django.utils.timezone.now()
            + django.utils.timezone.timedelta(30),comunidad=co)
            n.imagenes.add(im)
            n.save()
            c = Noticia.objects.get(titulo='Prueba')
            self.assertTrue(False)
        else:
            self.assertTrue(True)

# Test for UC: Edit News
class EditNewsTest(TestCase):

    # This function changes a parameter of the Notice object and checks if the
    # changes are saved.
    def testEditNewsAdmin(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            i= Imagen.objects.create(nombre='Prueba O',path='media/images/agua.jpg')
            im = Imagen.objects.get(nombre='Prueba O')
            c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
            co = Comunidad.objects.get(nombre='Prueba C')
            n = Noticia.objects.create(titulo='Prueba', texto='Lorem Ipsum',
            fechaInicio=django.utils.timezone.now(), fechaFin=django.utils.timezone.now() + django.utils.timezone.timedelta(30)
            ,comunidad=co)
            n.imagenes.add(im)
            n.save()
            n.titulo = 'Prueba N'
            n.save()
            c = Noticia.objects.get(titulo='Prueba N')
        self.assertEqual(n,c)

    def testEditNewsFalse(self):
        """
        This test tries to edit an activity without being an admin. If it doesnt edits it it returns true.
        """
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.assertTrue(n,c)




# Test for the UC: Filter Actividades
# Test by roles
class FilterActivitiesTest(TestCase):

    def testFilterActivities(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            i= Imagen.objects.create(nombre='Prueba O',path='media/images/agua.jpg')
            im = Imagen.objects.get(nombre='Prueba O')
            c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
            co = Comunidad.objects.get(nombre='Prueba C')
            n = Noticia.objects.create(titulo='Prueba', texto='Lorem Ipsum',
            fechaInicio=django.utils.timezone.now(), fechaFin=django.utils.timezone.now() + django.utils.timezone.timedelta(30)
            ,comunidad=co)
            n.imagenes.add(im)
            n.save()
            n.titulo = 'Prueba N'
            n.save()
            c = Noticia.objects.get(titulo='Prueba N')
            self.assertTrue(False)
        else:
            self.assertTrue(True)
            n = Noticia.objects.create(titulo='Prueba 1', texto='Lorem Ipsum',
            fechaInicio=django.utils.timezone.now(), fechaFin=django.utils.timezone.now()
            + django.utils.timezone.timedelta(30),comunidad=co)

            n2 = Noticia.objects.create(titulo='Prueba 2', texto='Lorem Ipsum',
            fechaInicio=django.utils.timezone.now(), fechaFin=django.utils.timezone.now()
            + django.utils.timezone.timedelta(30),comunidad=co)

            n2.imagenes.add(im)
            n.imagenes.add(im)
            n.save()
            n2.save


            response = self.client.get('/actividades/')

            #Checar que tiene 2 objetos
            self.assertEquals(response.context_data['filter'].qs.count(), 2)


            response = self.client.get('/actividades/?titulo=1')
            #Checar que el filtro 1 solo regresa 1 objeto
            self.assertEquals(response.context_data['filter'].qs.count(), 1)
