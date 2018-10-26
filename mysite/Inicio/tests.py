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
from django.contrib.auth.models import User, Group
from Actividades.models import Noticia, Imagen


"""
Function LogIn-logOut.
Function description: The admin/editor can login/logout.
Function parameters: testCase
return none
"""
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


"""
Function Add announcement.
Function description: The admin/editor can Add announcement.
Function parameters: testCase
return announcementCreated
"""
class AddAnnouncementTest(TestCase):

    def testCreateAnnouncement(self):
        a = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
        an = Anuncio.objects.get(titulo='Prueba A')
        return an


    def testAddAnnouncement(self):
        w = self.testCreateAnnouncement()
        self.assertTrue(isinstance(w,Anuncio))

"""
Function Edit announcement.
Function description: The admin/editor can Edit announcement.
Function parameters: testCase
return announcementCreated
"""
class EditAnnouncementTest(TestCase):

    def testCreateAnnouncement(self):
        a = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
        an = Anuncio.objects.get(titulo='Prueba A')
        return an


    def testEditAnnouncement(self):
        w = self.testCreateAnnouncement()
        w.titulo='Prueba B'
        self.assertTrue(w.titulo,'Prueba B')


"""
Function Delete announcement.
Function description: The admin/editor can Delete announcement.
Function parameters: testCase
return announcementCreated
"""

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
Function Add Role.
Function description: The admin/editor can Add Role.
Function parameters: testCase
return roleCreated
"""

class AddRoleTest(TestCase):

    def newAdmin(self):
        self.my_admin = User(username='user', is_staff=True)
        my_group = Group.objects.get(name='user')
        my_group.user_set.add(your_user)

    def testCreateRole(self):
        g = Comunidad.objects.create(nombre="Prueba A")
        gr = Comunidad.objects.get(nombre='Prueba A')
        return gr

    def testAddRole(self):
        w = self.testCreateRole()
        self.assertTrue(isinstance(w, Comunidad))

"""
Function Edit Role.
Function description: The admin/editor can edit role.
Function parameters: testCase
return roleCreated
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
Function Delete Role.
Function description: The admin/editor can Delete role.
Function parameters: testCase
return roleCreated
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
Function Assign Role to account.
Function description: The admin/editor can Assign Role to account.
Function parameters: testCase
return roleCreated
"""

class AssignRoleTest(TestCase):

    def testCreateRole(self):
        g = Comunidad.objects.create(nombre="Prueba A")
        gr = Comunidad.objects.get(nombre='Prueba A')

        return gr


"""
Function Add Mission and Vission.
Function description: The admin/editor can Add Mission and Vission.
Function parameters: testCase
return MisionCreated
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
Function Edit Mission and Vission.
Function description: The admin/editor can Edit Mission and Vission.
Function parameters: testCase
return MisionCreated
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
Function Delete Mission and Vission.
Function description: The admin/editor can Delete Mission and Vission.
Function parameters: testCase
return MisionCreated
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
Function Consult visits graphics.
Function description: The admin/editor can view visits report.
Function parameters: testCase
return MisionCreated
"""
class ConsulReportTest(TestCase):

    self.client = Client()
    self.my_editor = User(username = 'editor')
    self.my_editor.set_password('pass')
    self.my_editor.save()
    self.geditor = Group(name = 'Editor')

    def testReports(self):
        self.client = Client()
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 301)
