"""
Created by Framework
This file is where you can create tests for the App
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries needed
from guardian.shortcuts import assign_perm, remove_perm
from guardian.models import UserObjectPermission
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
from django.contrib.auth.models import Permission

"""
Function LogIn-logOut.
Function description: The admin/editor can login/logout.
Function parameters: testCase
return none

class LogInOutTest(TestCase):
    def testLogInAdmin(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        self.assertTrue(loginresponse) # should now return "true"

    def testLogOutAdmin(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        response = self.client.get('/admin/logout/')
        self.assertEqual(response.status_code, 200)

    def testLogInEditor(self):
        self.client = Client()
        self.my_editor = User(username='editor')
        self.my_editor.set_password('pass') # can't set above because of hashing
        self.my_editor.save() # needed to save to temporary test db
        self.geditor = Group(name='Editor')
        self.geditor.save()
        my_group = Group.objects.get(pk=1)
        my_group.user_set.add(self.my_editor)
        my_group.save()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='editor',password='pass')
        self.assertTrue(loginresponse) # should now return "true"

    def testLogOutEditor(self):
        self.client = Client()
        self.my_editor = User(username='editor')
        self.my_editor.set_password('pass') # can't set above because of hashing
        self.my_editor.save() # needed to save to temporary test db
        self.geditor = Group(name='Editor')
        self.geditor.save()
        my_group = Group.objects.get(name='Editor')
        my_group.user_set.add(self.my_editor)
        my_group.save()
        loginresponse = self.client.login(username='editor',password='pass')
        response = self.client.get('/admin/logout/')
        self.assertEqual(response.status_code, 302)


class AddAnnouncementTest(TestCase):


    def testAddAnnouncementAdmin(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            an = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
            an.save()
            c = Anuncio.objects.get(titulo='Prueba A')
        self.assertTrue(an,c)

class EditAnnouncementTest(TestCase):

    def testEditAnnouncementAdmin(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            an = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
            an.save()
            an.titulo='Prueba B'
            an.save()
            c = Anuncio.objects.get(titulo='Prueba B')
        self.assertTrue(an,c)

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
"""
Created by Framework
This file is where the tests of Add Role are declared.
Modified by: Abraham
Modification date: 25/10/18
"""
class RemoveRoleFromAccount(TestCase):
    def RemoveRole(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            self.client = Client()
            self.my_editor = User(username='editor')
            self.my_editor.set_password('pass') # can't set above because of hashing
            self.my_editor.save() # needed to save to temporary test db
            self.geditor = Group(name='Editor')
            self.geditor.save()
            my_group = Group.objects.get(pk=0)
            my_group.user_set.add(self.my_editor)
            my_group.save()
            my_group.user_set.remove(self.my_editor) # now user doesn't belong to group
            my_group.save()
            self.assertIs(self.my_editor.groups.filter(name="Editor").exists(), False)

    def RemoveRoleEditor(self):
        self.client = Client()
        self.my_editor = User(username='editor', is_staff=True)
        self.my_editor.set_password('pass') # can't set above because of hashing
        self.my_editor.save() # needed to save to temporary test db
        self.geditor = Group(name='Editor')
        self.geditor.save()
        my_group = Group.objects.get(name="Editor")
        my_group.user_set.add(self.my_editor)
        my_group.save()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='editor',password='pass')
        if loginresponse:
            self.client = Client()
            self.my_editor2 = User(username='user2')
            self.my_editor2.set_password('pass') # can't set above because of hashing
            self.my_editor2.save() # needed to save to temporary test db
            self.geditor2 = Group(name='Editor2')
            self.geditor2.save()
            my_group2 = Group.objects.get(name="Editor2")
            my_group2.user_set.add(self.my_editor2)
            my_group2.save()
            self.assertIs(self.my_editor2.groups.filter(name="Editor2").exists(), True)
            my_group2.user_set.remove(self.my_editor2) # now user doesn't belong to group
            my_group2.save()
            self.assertIs(self.my_editor2.groups.filter(name="Editor2").exists(), False)


"""
Created by Framework
This file is where the tests of Add Role are declared.
Modified by: Abraham
Modification date: 25/10/18
"""
 #ayuda: https://django-guardian.readthedocs.io/en/stable/userguide/assign.html
class AssignPrivRoleTest(TestCase):
    def testAssignPrivRole(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            #Create the Editor, user and assign
            self.client = Client()
            self.my_editor = User(username='editor')
            self.my_editor.set_password('pass') # can't set above because of hashing
            self.my_editor.save() # needed to save to temporary test db
            self.geditor = Group(name='Editor')
            self.geditor.save()
            my_group = Group.objects.get(name="Editor")
            #Create the task object
            an = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
            an.save()
            assign_perm('change_anuncio', my_group, an)
            #User doesn't have privilege
            self.assertIs(self.my_editor.has_perm('change_anuncio', an), False)
            #add user to Group with privilege
            my_group.user_set.add(self.my_editor)
            my_group.save()
            #now he has privilege
            self.assertTrue(self.my_editor.has_perm('change_anuncio', an))

    def testAssignPrivRoleEditor(self):
        self.client = Client()
        self.my_editor = User(username='editor', is_staff=True)
        self.my_editor.set_password('pass') # can't set above because of hashing
        self.my_editor.save() # needed to save to temporary test db
        self.geditor = Group(name='Editor')
        self.geditor.save()
        my_group = Group.objects.get(name="Editor")
        my_group.user_set.add(self.my_editor)
        my_group.save()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='editor',password='pass')
        if loginresponse:
            #Create the Editor, user and assign
            self.client = Client()
            self.my_editor2 = User(username='editor2')
            self.my_editor2.set_password('pass') # can't set above because of hashing
            self.my_editor2.save() # needed to save to temporary test db
            self.geditor = Group(name='Editor2')
            self.geditor.save()
            my_group2 = Group.objects.get(name="Editor2")
            #Create the task object
            an2 = Anuncio.objects.create(titulo="Prueba B", texto="Lorem Ipsum")
            an2.save()
            assign_perm('change_anuncio', my_group2, an2)
            #User doesn't have privilege
            self.assertIs(self.my_editor2.has_perm('change_anuncio', an2), False)
            #add user to Group with privilege
            my_group2.user_set.add(self.my_editor2)
            my_group2.save()
            #now he has privilege
            self.assertTrue(self.my_editor2.has_perm('change_anuncio', an2))





"""
Created by Framework
This file is where the tests of Add Role are declared.
Modified by: Abraham
Modification date: 25/10/18
"""
class RemovePrivRoleTest(TestCase):
    def testRemovePrivRole(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            self.client = Client()
            self.my_editor = User(username='editor')
            self.my_editor.set_password('pass') # can't set above because of hashing
            self.my_editor.save() # needed to save to temporary test db
            self.geditor = Group(name='Editor')
            self.geditor.save()
            editor = User.objects.get(username="editor")
            my_group = Group.objects.get(name="Editor")
            #Create the task object
            an = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
            an.save()
            assign_perm('change_anuncio', my_group, an)
            #User doesn't have privilege
            self.assertIs(editor.has_perm('change_anuncio', an), False)
            #add user to Group with privilege
            my_group.user_set.add(editor)
            my_group.save()
            #now he has privilege
            self.assertTrue(editor.has_perm('change_anuncio', an))
            remove_perm('change_anuncio', my_group, an)
            #now he hasn't
            self.assertIs(editor.has_perm('change_anuncio', an), False)

    def testRemovePrivRoleEditor(self):
        self.client = Client()
        self.my_editor = User(username='editor', is_staff=True)
        self.my_editor.set_password('pass') # can't set above because of hashing
        self.my_editor.save() # needed to save to temporary test db
        self.geditor = Group(name='Editor')
        self.geditor.save()
        my_group = Group.objects.get(name="Editor")
        my_group.user_set.add(self.my_editor)
        my_group.save()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='editor',password='pass')
        if loginresponse:
            self.client = Client()
            self.my_editor2 = User(username='editor2')
            self.my_editor2.set_password('pass') # can't set above because of hashing
            self.my_editor2.save() # needed to save to temporary test db
            self.geditor2 = Group(name='Editor2')
            self.geditor2.save()
            editor2 = User.objects.get(username="editor2")
            my_group2 = Group.objects.get(name="Editor2")
            #Create the task object
            an2 = Anuncio.objects.create(titulo="Prueba B", texto="Lorem Ipsum")
            an2.save()
            assign_perm('change_anuncio', my_group2, an2)
            #User doesn't have privilege
            self.assertIs(editor2.has_perm('change_anuncio', an2), False)
            #add user to Group with privilege
            my_group2.user_set.add(editor2)
            my_group2.save()
            #now he has privilege
            self.assertTrue(editor2.has_perm('change_anuncio', an2))
            remove_perm('change_anuncio', my_group2, an2)
            #now he hasn't
            self.assertIs(editor2.has_perm('change_anuncio', an2), False)


"""
Created by Framework
This file is where the tests of Add Role are declared.
Modified by: Abraham
Modification date: 25/10/18
"""

class ViewUsersTest(TestCase):
    def testViewUsers(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            permission = Permission.objects.get(content_type__model='User', codename='view_user')
            self.my_admin.user_permissions.add(permission)
            #admin has permission to view users
            response = self.client.get('/admin/auth/user/')
            self.assertEqual(response.status_code, 200)

    def testViewUsersEditor(self):
        self.client = Client()
        self.my_editor = User(username='editor', is_staff=True)
        self.my_editor.set_password('pass') # can't set above because of hashing
        self.my_editor.save() # needed to save to temporary test db
        self.geditor = Group(name='Editor')
        self.geditor.save()
        my_group = Group.objects.get(name="Editor")
        my_group.user_set.add(self.my_editor)
        my_group.save()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='editor',password='pass')
        if loginresponse:
            permission = Permission.objects.get(content_type__model='User', codename='view_user')
            self.my_editor.user_permissions.add(permission)
            #admin has permission to view users
            response = self.client.get('/admin/auth/user/')
            self.assertEqual(response.status_code, 200)


"""
class AddRoleTest(TestCase):
    def testCreateRole(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            g = Comunidad.objects.create(nombre="Prueba A")
            gr = Comunidad.objects.get(nombre='Prueba A')
            return gr


    def testAddRole(self):
        w = self.testCreateRole()
        self.assertTrue(isinstance(w, Comunidad))
"""
"""
Created by Framework
This file is where the tests of Edit Role are declared.
Modified by: Maritza
Modification date: 25/10/18
"""

"""
class EditRoleTest(TestCase):

    def testCreateRole(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            g = Comunidad.objects.create(nombre="Prueba A")
            gr = Comunidad.objects.get(nombre='Prueba A')
            return gr

    def testEditRole(self):
        w = self.testCreateRole()
        w.nombre = 'Prueba B'
        self.assertTrue(w.nombre,'Prueba B')
"""

"""
Created by Framework
This file is where the tests of Delete Role are declared.
Modified by: Maritza
Modification date: 25/10/18
"""

"""
class DeleteRoleTest(TestCase):
    def testCreateRole(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            g = Comunidad.objects.create(nombre="Prueba A")
            gr = Comunidad.objects.get(nombre='Prueba A')
            return gr

    def testDeleteRole(self):
        w = self.testCreateRole()
        w.delete()
        self.assertTrue(w,None)
"""


"""
Created by Framework
This file is where the tests of Assign Role to account are declared.
Modified by: Maritza
Modification date: 25/10/18
"""
"""
class AssignRoleTest(TestCase):

    def testCreateRole(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            g = Comunidad.objects.create(nombre="Prueba A")
            gr = Comunidad.objects.get(nombre='Prueba A')
"""


"""
Created by Framework
This file is where the tests of Add Mission and Vission are declared.
Modified by: Maritza
Modification date: 25/10/18
"""



"""
class AddMVHTest(TestCase):

    def testCreateMVH(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            n = Mision.objects.create(nombre='Prueba A', mision='Lorem ipsum')
            nv = Mision.objects.get(nombre='Prueba A', mision='Lorem ipsum')

        return nv

    def testAddMVH(self):
        w = self.testCreateMVH()
        self.assertTrue(isinstance(w, Mision))
"""


"""
Created by Framework
This file is where the tests of Edit Mission and Vission are declared.
Modified by: Maritza
Modification date: 25/10/18
"""


""""
class EditMVHTest(TestCase):

    def testCreateMVH(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            g = Mision.objects.create(nombre='Prueba A', mision='Lorem ipsum')
            gr = Mision.objects.get(nombre='Prueba A', mision='Lorem ipsum')

        return gr

    def testEditMVH(self):
        w = self.testCreateMVH()
        w.nombre = 'Prueba B'
        self.assertTrue(w.nombre,'Prueba B')

"""

"""
Created by Framework
This file is where the tests of Delete Mission and Vission are declared.
Modified by: Maritza
<<<<<<< HEAD
Modification date: 26/10/18
"""
"""
class DeleteMVHTest(TestCase):

    def testCreateMVH(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            g = Mision.objects.create(nombre="Prueba A")
            gr = Mision.objects.get(nombre='Prueba A')
            return gr

    def testDeleteRole(self):
        w = self.testCreateMVH()
        w.delete()
        self.assertTrue(w,None)
"""


"""
Function Consult visits graphics.
Function description: The admin/editor can view visits report.
Function parameters: testCase
return MisionCreated
"""

"""
class ConsulReportTest(TestCase):

    def testReports(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            self.client = Client()
            response = self.client.get('/admin')
            self.assertEqual(response.status_code, 301)
"""
