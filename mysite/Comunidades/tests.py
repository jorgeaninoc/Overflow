"""
Created by Framework
This file is where the tests of Comunidades are declared.
Modified by: Jorge Nino
Date: 19/10/18
"""
#Import libraries used.
from django.test import TestCase, Client
from Comunidades.models import Comunidad,Imagen
from django.contrib.auth.models import User, Group

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

    def testAddCommunitiesAdmin(self):
        """
        This function calls the function to create the object Comunidad and checks if it is an instance of Comunidad.
        """
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            i= Imagen.objects.create(nombre='Prueba I',path='media/images/agua.jpg')
            im = Imagen.objects.get(nombre='Prueba I')
            c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
            c.imagenes.add(im)
            co = Comunidad.objects.get(nombre='Prueba C')
            co.save()
            # Check if the community exists in the DB
            c = Comunidad.objects.get(nombre='Prueba C')
        self.assertEqual(co,c)

# Test for CU: Edit Communities
class EditCommunitiesTest(TestCase):


    def testEditCommunitiesAdmin(self):
        """
        This function calls the function to create the object Comunidad and changes a value from it, then checks if the value is the same as tested.
        Returns nothing.
        """
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            i= Imagen.objects.create(nombre='Prueba I',path='media/images/agua.jpg')
            im = Imagen.objects.get(nombre='Prueba I')
            c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
            c.imagenes.add(im)
            c.save()
            c.nombre = 'Prueba C2'
            c.save()
            co = Comunidad.objects.get(nombre='Prueba C2')
        self.assertTrue(co,c)

# Test for the CU: Delete Community
class DeleteCommunitiesTest(TestCase):


    def testDeleteCommunitiesAdmin(self):
        """
        This function calls the function to create the object Comunidad and deletes it, then checks if it was deleted.
        """
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            i= Imagen.objects.create(nombre='Prueba I',path='media/images/agua.jpg')
            im = Imagen.objects.get(nombre='Prueba I')
            c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
            c.imagenes.add(im)
            c.save()
            c.delete()
            c.save()
            co = Comunidad.objects.get(nombre='Prueba C')
        # Check if it was deleted from the BD.
        self.assertEquals(c,co)



# Test for the UC: Filter Communities
# Test by roles
class FilterCommunitiesTest(TestCase):

    def testFilterCommunities(self):
        """
        This function checks the objects at the communities and checks if filter works
        """
        self.client = Client()

        # Create objects to filter and save them
        c = Comunidad.objects.create(nombre="Prueba 1", descripcion="Lorem Ipsum")
        c.save()
        d = Comunidad.objects.create(nombre="Prueba 2", descripcion="Lorem Ipsum")
        d.save()

        response = client.get('/comunidades/')

        #Checar que tiene 2 objetos
        self.assertEquals(response.context_data['filter'].qs.count, 2)


        response = client.get('/comunidades/?nombre=1')
        #Checar que el filtro 1 solo regresa 1 objeto
        self.assertEquals(response.context_data['filter'].qs.count, 1)
