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
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from Actividades.models import Noticia, Imagen
from django.contrib.auth.models import Permission
from django.contrib.auth.models import ContentType

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
<<<<<<< HEAD
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
=======
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
>>>>>>> 55bbd8c4ba3840586a014f484c5f8c987b91b848
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
        my_group = Group.objects.get(name='Editor')
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

    def testEditAnnouncementEditor(self):
        """
        This test edits an announcement and checks if it saves.
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
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='editor',password='pass')
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
# Test for the CU: Delete Announcement
class DeleteAnnouncementTest(TestCase):


    def testDeleteAnnouncementAdmin(self):
        """
        This function calls the function to create the object Announcement and deletes it, then checks if it was deleted.
        """
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=False)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            c = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
            c.save()
            c.delete()
            c.save()
            co = Anuncio.objects.get(titulo='Prueba A')
        # Check if it was deleted from the BD.
        self.assertEqual(c,co)

    def testDeleteAnnouncementEditor(self):
        """
        This function calls the function to create the object Announcement and deletes it, then checks if it was deleted.
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
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='editor',password='pass')
        if loginresponse:
            c = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
            c.save()
            c.delete()
            c.save()
            co = Anuncio.objects.get(titulo='Prueba A')
        # Check if it was deleted from the BD.
        self.assertEqual(c,co)





"""
Created by Framework
This file is where the tests of Add Role are declared.
Modified by: Abraham
Modification date: 25/10/18
"""

#ayuda: https://django-guardian.readthedocs.io/en/stable/userguide/assign.html

class RemoveRoleFromAccount(TestCase):

    def RemoveRole(self):
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
            my_group = Group.objects.get(pk=1)

            #Create the task object
            an = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
            an.save()
            assign_perm('change_anuncio', my_group, an)
            #User doesn't have privilege
            self.assertTrue(not self.my_editor.has_perm('change_anuncio', an))

            #add user to Group with privilege
            my_group.user_set.add(self.my_editor)
            my_group.save()

            #now he has privilege
            self.assertTrue(self.my_editor.has_perm('change_anuncio', an))




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

    def testAddAnnouncementEditor(self):
        """
        This test adds an announcement and checks if it exist.
        """
        self.client = Client()
        content_type = ContentType.objects.get(app_label='Inicio', model='Anuncio')
        permission = Permission.objects.create(codename='can_add',
                                       name='Can Add Announcements',
                                       content_type=content_type)
        self.my_editor = User(username='editor')
        self.my_editor.set_password('pass') # can't set above because of hashing
        self.my_editor.save() # needed to save to temporary test db
        self.geditor = Group(name='Editor')
        self.geditor.save()
        self.geditor.permissions.add(permission)
        my_group = Group.objects.get(name='Editor')
        my_group.user_set.add(self.my_editor)
        my_group.save()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='editor',password='pass')
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

    def testEditAnnouncementEditor(self):
        """
        This test edits an announcement and checks if it saves.
        """
        self.client = Client()
        content_type = ContentType.objects.get(app_label='Inicio', model='Anuncio')
        permission = Permission.objects.create(codename='can_edit',
                                       name='Can Edit Announcements',
                                       content_type=content_type)
        self.my_editor = User(username='editor')
        self.my_editor.set_password('pass') # can't set above because of hashing
        self.my_editor.save() # needed to save to temporary test db
        self.geditor = Group(name='Editor')
        self.geditor.save()
        self.geditor.permissions.add(permission)
        my_group = Group.objects.get(name='Editor')
        my_group.user_set.add(self.my_editor)
        my_group.save()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='editor',password='pass')
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
# Test for the CU: Delete Announcement
class DeleteAnnouncementTest(TestCase):


    def testDeleteAnnouncementAdmin(self):
        """
        This function calls the function to create the object Announcement and deletes it, then checks if it was deleted.
        """
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=False)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            c = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
            c.save()
            c.delete()
            c.save()
            co = Anuncio.objects.get(titulo='Prueba A')
        # Check if it was deleted from the BD.
        self.assertEqual(c,co)

    def testDeleteAnnouncementEditor(self):
        """
        This function calls the function to create the object Announcement and deletes it, then checks if it was deleted.
        """
        self.client = Client()
        content_type = ContentType.objects.get(app_label='Inicio', model='Anuncio')
        permission = Permission.objects.create(codename='can_delete',
                                       name='Can Delete Announcements',
                                       content_type=content_type)
        self.my_editor = User(username='editor')
        self.my_editor.set_password('pass') # can't set above because of hashing
        self.my_editor.save() # needed to save to temporary test db
        self.geditor = Group(name='Editor')
        self.geditor.save()
        self.geditor.permissions.add(permission)
        my_group = Group.objects.get(name='Editor')
        my_group.user_set.add(self.my_editor)
        my_group.save()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='editor',password='pass')
        if loginresponse:
            c = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
            c.save()
            c.delete()
            c.save()
            co = Anuncio.objects.get(titulo='Prueba A')
        # Check if it was deleted from the BD.
        self.assertEqual(c,co)






#             my_group.user_set.add(self.my_editor)
#             my_group.save()
#             my_group.user_set.remove(self.my_editor) # now user doesn't belong to group
#             my_group.save()
#         self.assertTrue(not self.my_editor.groups.filter(name="Editor").exists())

"""
Created by Framework
This file is where the tests of Add Role are declared.
Modified by: Abraham
Modification date: 25/10/18
"""
class ViewUsersTest(TestCase):

#ayuda: https://django-guardian.readthedocs.io/en/stable/userguide/assign.html

class RemoveRoleFromAccount(TestCase):

    def RemoveRole(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            response = self.client.get('/admin/auth/user/')
            self.assertEqual(response.status_code, 403)



"""
Created by Framework
This file is where the tests of Assign Role to account are declared.
Modified by: Maritza
Modification date: 25/10/18
"""

class AssignRoleTest(TestCase):

    def testCreateRole(self):
        self.client = Client()
        content_type = ContentType.objects.get(app_label='Inicio', model='Anuncio')
        permission = Permission.objects.create(codename='can_add',
                                       name='Can Add Role',
                                       content_type=content_type)
        permission.save()
        self.my_editor = User(username='editor')
        self.my_editor.set_password('pass') # can't set above because of hashing
        self.my_editor.save() # needed to save to temporary test db
        self.geditor = Group(name='Editor')
        self.geditor.save()
        my_group = Group.objects.get(name='Editor')
        my_group.user_set.add(self.my_editor)
        my_group.save()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='editor',password='pass')
        if loginresponse:
            return permission


"""
Created by Framework
This file is where the tests of Add Role are declared.
Modified by: Maritza
Modification date: 25/10/18
"""

class AddRoleTest(TestCase):

    def testAddRole(self):
        self.client = Client()
        content_type = ContentType.objects.get(app_label='Inicio', model='Anuncio')

        self.my_editor = User(username='editor')
        self.my_editor.set_password('pass') # can't set above because of hashing
        self.my_editor.save() # needed to save to temporary test db
        self.geditor = Group(name='Editor')
        self.geditor.save()

        my_group = Group.objects.get(name='Editor')
        my_group.user_set.add(self.my_editor)
        my_group.save()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='editor',password='pass')
        if loginresponse:
            an = Permission.objects.create(codename='can_add',
                                           name='Can Add Announcements',
                                           content_type=content_type)
            an.save()
            c = Permission.objects.get(name='Can Add Announcements')
            #add
        self.assertEqual(an,c)


"""
Created by Framework
This file is where the tests of Edit Role are declared.
Modified by: Maritza
Modification date: 25/10/18
"""
class RemovePrivRoleTest(TestCase):


    def testCreateRole(self):
        self.client = Client()
        content_type = ContentType.objects.get(app_label='Inicio', model='Anuncio')
        permission = Permission.objects.create(codename='can_add',
                                       name='Can Add Role',
                                       content_type=content_type)
        permission.save()
        self.my_editor = User(username='editor')
        self.my_editor.set_password('pass') # can't set above because of hashing
        self.my_editor.save() # needed to save to temporary test db
        self.geditor = Group(name='Editor')
        self.geditor.save()
        my_group = Group.objects.get(name='Editor')
        my_group.user_set.add(self.my_editor)
        my_group.save()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='editor',password='pass')
        if loginresponse:
            return permission

    def testEditRole(self):
        w = self.testCreateRole()
        w.name = 'Can Edit Role'
        self.assertTrue(w.name,'Can Edit Role')
        #false


"""
Created by Framework
This file is where the tests of Delete Role are declared.
Modified by: Maritza
Modification date: 25/10/18
"""
class ViewUsersTest(TestCase):


class DeleteRoleTest(TestCase):
    def testCreateRole(self):
        self.client = Client()
        content_type = ContentType.objects.get(app_label='Inicio', model='Anuncio')
        permission = Permission.objects.create(codename='can_add',
                                       name='Can Add Role',
                                       content_type=content_type)
        permission.save()
        self.my_editor = User(username='editor')
        self.my_editor.set_password('pass') # can't set above because of hashing
        self.my_editor.save() # needed to save to temporary test db
        self.geditor = Group(name='Editor')
        self.geditor.save()
        my_group = Group.objects.get(name='Editor')
        my_group.user_set.add(self.my_editor)
        my_group.save()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='editor',password='pass')
        if loginresponse:
            return permission



    def testViewUsers(self):
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='user', is_staff=True)
        self.my_admin.set_password('passphrase') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='user',password='passphrase')
        if loginresponse:
            response = self.client.get('/admin/auth/user/')
            self.assertEqual(response.status_code, 403)



"""
Created by Framework
This file is where the tests of Assign Role to account are declared.
Modified by: Maritza
Modification date: 25/10/18
"""

class AssignRoleTest(TestCase):

    def testCreateRole(self):
        self.client = Client()
        self.my_editor = User(username='Maritza')
        self.my_editor.set_password('maritza1234') # can't set above because of hashing
        self.my_editor.save() # needed to save to temporary test db
        self.geditor = Group(name='Editor')
        self.geditor.save()
        content_type = ContentType.objects.get(app_label='Inicio', model='Anuncio')
        my_group = Group.objects.get(name='Editor')
        my_group.user_set.add(self.my_editor)
        my_group.save()
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='Maritza',password='maritza1234')
        if loginresponse:
            #Create the task object
            an = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
            an.save()
            assign_perm('change_anuncio', my_group, an)

            #add user to Group with privilege
            my_group.user_set.add(self.my_editor)
            my_group.save()

            #now he has privilege
            self.assertTrue(self.my_editor.has_perm('change_anuncio', an))
            #add Role
            an = Permission.objects.create(codename='can_add',
                                           name='Can Add Announcements',
                                           content_type=content_type)
            an.save()
            c = Permission.objects.get(name='Can Add Announcements')
            #add

            return an
        self.assertEqual(an,c)
        #edit role
    def testEditRole(self):
        w = self.testCreateRole()
        w.name = 'Can Edit Role'
        self.assertTrue(w.name,'Can Edit Role')
        #false

    def testDeleteRole(self):
        w = self.testCreateRole()
        w.delete()
        self.assertTrue(w,None)
        #false


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
<<<<<<< HEAD
# class ConsulReportTest(TestCase):

#     def testReports(self):
#         self.client = Client()
#         response = self.client.get('/admin/', follow=True)
#         self.my_admin = User(username='user', is_staff=True)
#         self.my_admin.set_password('passphrase') # can't set above because of hashing
#         self.my_admin.save() # needed to save to temporary test db
#         loginresponse = self.client.login(username='user',password='passphrase')
#         if loginresponse:
#             self.client = Client()
#             response = self.client.get('/admin')
#             self.assertEqual(response.status_code, 301)




"""
Created by Framework
This file is where the tests of Edit Mission and Vission are declared.
Modified by: Enrique
Modification date: 21/11/18
"""

# class AddAccountTest(TestCase):

#     def testCreateUser(self):
#         self.client = Client()
#         content_type = ContentType.objects.get(app_label='Inicio', model='Anuncio')
#         permission = Permission.objects.create(codename='can_add',
#                                        name='Can Add Role',
#                                        content_type=content_type)
#         permission.save()
#         self.my_editor = User(username='editor')
#         self.my_editor.set_password('pass') # can't set above because of hashing
#         self.my_editor.save() # needed to save to temporary test db
#         self.geditor = Group(name='Editor')
#         self.geditor.save()
#         my_group = Group.objects.get(name='Editor')
#         my_group.user_set.add(self.my_editor)
#         my_group.save()
#         response = self.client.get('/admin/', follow=True)
#         loginresponse = self.client.login(username='editor',password='pass')
#         if loginresponse:
#             return permission





class AddAccountTest(TestCase):


    def testAddAccount(self): # Done
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='admin', is_staff=True)
        self.my_admin.set_password('password') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='admin',password='password')
        if loginresponse:
            response = self.client.get('/admin/auth/user/')
            user_created = User(username = 'user', is_staff = True)
            user_created.set_password('pasuser')
            user_created.save()
            # self.assertTrue(isinstance(user_created, User))
            users = User.objects.get(username = 'user')
            self.assertEqual(user_created,users)


class EditAccountTest(TestCase):


    def testEditAccount(self): # Done
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='admin', is_staff=True)
        self.my_admin.set_password('password') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='admin',password='password')
        if loginresponse:
            response = self.client.get('/admin/auth/user/')
            user_created = User(username = 'user', is_staff = True)
            user_created.set_password('pasuser')
            user_created.save()
            # self.assertTrue(isinstance(user_created, User))
            user_created.username = 'userchanged'
            user_created.save()
            users = User.objects.get(username = 'userchanged')
            self.assertEqual(user_created,users)


class DeleteAccountTest(TestCase):

    def testDeleteAccount(self): # Done
        self.client = Client()
        response = self.client.get('/admin/', follow=True)
        self.my_admin = User(username='admin', is_staff=True)
        self.my_admin.set_password('password') # can't set above because of hashing
        self.my_admin.save() # needed to save to temporary test db
        loginresponse = self.client.login(username='admin',password='password')
        if loginresponse:
            response = self.client.get('/admin/auth/user/')
            user_created = User(username = 'user', is_staff = True)
            user_created.set_password('pasuser')
            user_created.save()
            # self.assertTrue(isinstance(user_created, User))
            # user_created.username = 'userchanged'
            user_created.delete()
            # user_created.save()

            # users = User.objects.get(username = 'user')
            # self.assertEqual(user_created,users)
            self.assertTrue(user_created,None)

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
