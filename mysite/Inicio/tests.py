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
"""

# Test for UC: log in and Log out
class LogInOutTest(TestCase):

    def testLogInFalse(self):
        """
        This test tries to log in without having an account.
        """
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='user',password='passphrase')
        self.assertFalse(loginresponse) # should now return "false"

    def testLogOutFalse(self):
        """
        This test tries to log out without having an account.
        """
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='user',password='passphrase')
        response = self.client.logout()
        self.assertFalse(response) # should now return "false"

    def testLogInAdmin(self):
        """
        This test tries to log in as an admin by creating one.
        """
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        self.assertTrue(loginresponse) # should now return "true"

    def testLogOutAdmin(self):
        """
        This test tries to log out as an admin.
        """
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        response = self.client.get('/admin/logout/')
        self.assertEqual(response.status_code, 200)


    def testLogInEditor(self):
        """
        This test tries to log in as an editor.
        """
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
        """
        This test tries to log out as an editor.
        """
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

# Test for UC: Add Announcement
class AddAnnouncementTest(TestCase):


    def testAddAnnouncementAdmin(self):
        """
        This test adds an announcement and checks if it exist.
        """
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
        self.assertEqual(an,c)

    def testAddAnnouncementFalse(self):
        """
        This test tries to add an a Announcement without having an account.
        """
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            an = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
            an.save()
            c = Anuncio.objects.get(titulo='Prueba A')
            self.assertTrue(False)
        else:
            self.assertTrue(True)


# Test for UC: Edit Announcement
class EditAnnouncementTest(TestCase):

    def testEditAnnouncementAdmin(self):
        """
        This test edits an announcement and checks if it saves.
        """
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

    def testEditAnnouncementFalse(self):
        """
        This test tries to edit an anonuncement without having an account
        """
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            an = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
            an.save()
            c = Anuncio.objects.get(titulo='Prueba A')
            self.assertTrue(False)
        else:
            self.assertTrue(True)

class DeleteAnnouncementTest(TestCase):

    def testCreateAnnouncement(self):
        a = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
        an = Anuncio.objects.get(titulo='Prueba A')
        return an


    def testDeleteAnnouncement(self):
        w = self.testCreateAnnouncement()
        w.delete()
        self.assertTrue(w,None)





<<<<<<< HEAD

=======
>>>>>>> abraham_removeRole
"""
Created by Framework
This file is where the tests of Add Role are declared.
Modified by: Abraham
Modification date: 25/10/18
"""

<<<<<<< HEAD

#ayuda: https://django-guardian.readthedocs.io/en/stable/userguide/assign.html

class AssignPrivRoleTest(TestCase):

    def testAssignPrivRole(self):
=======
class RemoveRoleFromAccount(TestCase):

    def RemoveRole(self):
>>>>>>> abraham_removeRole
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
<<<<<<< HEAD
            #Create the Editor, user and assign
=======
>>>>>>> abraham_removeRole
            self.client = Client()
            self.my_editor = User(username='editor')
            self.my_editor.set_password('pass') # can't set above because of hashing
            self.my_editor.save() # needed to save to temporary test db
            self.geditor = Group(name='Editor')
            self.geditor.save()
            my_group = Group.objects.get(pk=1)
<<<<<<< HEAD

            #Create the task object
            an = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
            an.save()
            assign_perm('change_anuncio', my_group, an)
            #User doesn't have privilege
            self.assertTrue(!self.my_editor.has_perm('change_anuncio', an))

            #add user to Group with privilege
            my_group.user_set.add(self.my_editor)
            my_group.save()

            #now he has privilege
            self.assertTrue(self.my_editor.has_perm('change_anuncio', an))






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
            my_group = Group.objects.get(pk=1)

            #Create the task object
            an = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
            an.save()

            assign_perm('change_anuncio', my_group, an)
            #User doesn't have privilege
            self.assertTrue(!editor.has_perm('change_anuncio', an))

            #add user to Group with privilege
            my_group.user_set.add(editor)
            my_group.save()

            #now he has privilege
            self.assertTrue(editor.has_perm('change_anuncio', an))


            remove_perm('change_anuncio', my_group, an)
            #now he hasn't
            self.assertTrue(!editor.has_perm('change_anuncio', an))



<<<<<<< HEAD
=======
            my_group.user_set.add(self.my_editor)
            my_group.save()
            my_group.user_set.remove(self.my_editor) # now user doesn't belong to group
            my_group.save()
        self.assertTrue(!self.my_editor.groups.filter(name="Editor").exists())
>>>>>>> abraham_removeRole
=======
"""
Created by Framework
This file is where the tests of Add Role are declared.
Modified by: Abraham
Modification date: 25/10/18
"""
class ViewUsersTest(TestCase):
>>>>>>> abraham_viewUsers


    def testViewUsers(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            response = self.client.get('/admin/auth/user/')
            self.assertEqual(response.status_code, 200)



"""
Created by Framework
This file is where the tests of Add Role are declared.
Modified by: Maritza
Modification date: 25/10/18
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
Created by Framework
This file is where the tests of Edit Role are declared.
Modified by: Maritza
Modification date: 25/10/18
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
Created by Framework
This file is where the tests of Delete Role are declared.
Modified by: Maritza
Modification date: 25/10/18
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
Created by Framework
This file is where the tests of Assign Role to account are declared.
Modified by: Maritza
Modification date: 25/10/18
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
Created by Framework
This file is where the tests of Add Mission and Vission are declared.
Modified by: Maritza
Modification date: 25/10/18
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
Created by Framework
This file is where the tests of Edit Mission and Vission are declared.
Modified by: Maritza
Modification date: 25/10/18
"""
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
Created by Framework
This file is where the tests of Delete Mission and Vission are declared.
Modified by: Maritza
<<<<<<< HEAD
Modification date: 26/10/18
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
Function Consult visits graphics.
Function description: The admin/editor can view visits report.
Function parameters: testCase
return MisionCreated
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
