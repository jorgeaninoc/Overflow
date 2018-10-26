"""
Created by Framework
This file is where you can create tests for the App
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries needed
from django.contrib.auth.models import User
from Inicio.models import Anuncio, Imagen
from django.test import TestCase, Client
from Comunidades.models import Comunidad
from Somos.models import Mision
from Catalogo.models import Producto
from Comunidades.models import Comunidad
from datetime import datetime as dt
from datetime import timedelta as td
import django
from django.contrib.auth.models import User
from Actividades.models import Noticia, Imagen

class LogInOutTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db


    def testLogIn(self):
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='user',password='passphrase')
        self.assertTrue(loginresponse) # should now return "true"

    def testLogOut(self):
        self.client = Client()
        self.client.login(username='fred', password='secret')
        response = self.client.get('/admin/logout/')
        self.assertEqual(response.status_code, 302)


class AddAnnouncementTest(TestCase):

    def testCreateAnnouncement(self):
        a = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
        an = Anuncio.objects.get(titulo='Prueba A')
        return an


    def testAddAnnouncement(self):
        w = self.testCreateAnnouncement()
        self.assertTrue(isinstance(w,Anuncio))

class EditAnnouncementTest(TestCase):

    def testCreateAnnouncement(self):
        a = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
        an = Anuncio.objects.get(titulo='Prueba A')
        return an


    def testEditAnnouncement(self):
        w = self.testCreateAnnouncement()
        w.titulo='Prueba B'
        self.assertTrue(w.titulo,'Prueba B')

class DeleteAnnouncementTest(TestCase):

    def testCreateAnnouncement(self):
        a = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
        an = Anuncio.objects.get(titulo='Prueba A')
        return an


    def testDeleteAnnouncement(self):
        w = self.testCreateAnnouncement()
        w.delete()
        self.assertTrue(w,None)


"""
Created by Framework
This file is where the tests of Add Role are declared.
Modified by: Maritza
Modification date: 25/10/18
"""

class AddRoleTest(TestCase):

    def testCreateRole(self):
        g = Comunidad.objects.create(nombre="Prueba A")
        gr = Comunidad.objects.get(nombre='Prueba A')
        return gr

    def testAddRole(self):
        w = self.testCreateRole()
        self.assertTrue(isinstance(w, Comunidad))

"""
Created by Framework
This file is where the tests of Edit Role are declared.
Modified by: Maritza
Modification date: 25/10/18
"""

class EditRoleTest(TestCase):

    def testCreateRole(self):
        g = Comunidad.objects.create(nombre="Prueba A")
        gr = Comunidad.objects.get(nombre='Prueba A')
        return gr

    def testEditRole(self):
        w = self.testCreateRole()
        w.nombre = 'Prueba B'
        self.assertTrue(w.nombre,'Prueba B')

"""
Created by Framework
This file is where the tests of Delete Role are declared.
Modified by: Maritza
Modification date: 25/10/18
"""

class DeleteRoleTest(TestCase):
    def testCreateRole(self):
        g = Comunidad.objects.create(nombre="Prueba A")
        gr = Comunidad.objects.get(nombre='Prueba A')
        return gr

    def testDeleteRole(self):
        w = self.testCreateRole()
        w.delete()
        self.assertTrue(w,None)

"""
Created by Framework
This file is where the tests of Assign Role to account are declared.
Modified by: Maritza
Modification date: 25/10/18
"""

class AssignRoleTest(TestCase):

    def testCreateRole(self):
        g = Comunidad.objects.create(nombre="Prueba A")
        gr = Comunidad.objects.get(nombre='Prueba A')

"""
Created by Framework
This file is where the tests of Add Mission and Vission are declared.
Modified by: Maritza
Modification date: 25/10/18
"""
class AddMVHTest(TestCase):

    def testCreateMVH(self):
        n = Mision.objects.create(nombre='Prueba A', mision='Lorem ipsum')
        nv = Mision.objects.get(nombre='Prueba A', mision='Lorem ipsum')

        return nv

    def testAddMVH(self):
        w = self.testCreateMVH()
        self.assertTrue(isinstance(w, Mision))

"""
Created by Framework
This file is where the tests of Edit Mission and Vission are declared.
Modified by: Maritza
Modification date: 25/10/18
"""
class EditMVHTest(TestCase):

    def testCreateMVH(self):
        g = Mision.objects.create(nombre='Prueba A', mision='Lorem ipsum')
        gr = Mision.objects.get(nombre='Prueba A', mision='Lorem ipsum')

        return gr

    def testEditMVH(self):
        w = self.testCreateMVH()
        w.nombre = 'Prueba B'
        self.assertTrue(w.nombre,'Prueba B')

"""
Created by Framework
This file is where the tests of Delete Mission and Vission are declared.
Modified by: Maritza
Modification date: 26/10/18
"""
class DeleteMVHTest(TestCase):

    def testCreateMVH(self):
        g = Mision.objects.create(nombre="Prueba A")
        gr = Mision.objects.get(nombre='Prueba A')
        return gr

    def testDeleteRole(self):
        w = self.testCreateMVH()
        w.delete()
        self.assertTrue(w,None)

"""
Created by Framework
This file is where the tests of Add Products to catalog are declared.
Modified by: Maritza
Modification date: 26/10/18
"""
class AddProductsCatalog(TestCase):

    def testCreateCommunity(self):
        c = Comunidad.objects.create(nombre='Prueba A', descripcion = 'Lorem ipsum')
        co = Comunidad.objects.get(nombre='Prueba A', descripcion = 'Lorem ipsum')

    def testCreateProduct(self):
        n = Producto.objects.create(nombre='Prueba B', precio='15',
                                    communidad = 'Prueba A', subCat = 'dol sit')
        nv = Producto.objects.get(nombre='Prueba B', precio='15',
                                    communidad = 'Prueba A', subCat = 'dol sit')
        return nv

    def testAddProductC(self):
        w = self.testCreateProduct()
        self.assertTrue(isinstance(w, Producto))
