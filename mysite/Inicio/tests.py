from django.contrib.auth.models import User
from Inicio.models import Anuncio, Imagen
from django.test import TestCase, Client

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

class AddRoleTest(TestCase):

    def testCreateNews(self):
        i= Imagen.objects.create(nombre='Prueba O',path='media/images/agua.jpg')
        im = Imagen.objects.get(nombre='Prueba O')
        c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
        co = Comunidad.objects.get(nombre='Prueba C')
        n = Noticia.objects.create(titulo='Prueba', texto='Lorem Ipsum',
        fechaInicio=django.utils.timezone.now(), fechaFin=django.utils.timezone.now() + django.utils.timezone.timedelta(30)
        ,comunidad=co)
        n.imagenes.add(im)
        return n


    def testAddNews(self):
        w = self.testCreateNews()
        self.assertTrue(isinstance(w, Noticia))


class EditRoleTest(TestCase):

    def testCreateNews(self):
        i= Imagen.objects.create(nombre='Prueba O',path='media/images/agua.jpg')
        im = Imagen.objects.get(nombre='Prueba O')
        c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
        co = Comunidad.objects.get(nombre='Prueba C')
        n = Noticia.objects.create(titulo='Prueba', texto='Lorem Ipsum',
        fechaInicio=django.utils.timezone.now(), fechaFin=django.utils.timezone.now() + django.utils.timezone.timedelta(30)
        ,comunidad=co)
        n.imagenes.add(im)
        return n


    def testEditNews(self):
        w = self.testCreateNews()
        w.titulo = 'Prueba N'
        self.assertTrue(w.titulo,'Prueba N')

class DeleteRoleTest(TestCase):

    def testCreateAnnouncement(self):
        a = Anuncio.objects.create(titulo="Prueba A", texto="Lorem Ipsum")
        an = Anuncio.objects.get(titulo='Prueba A')
        return an


    def testDeleteAnnouncement(self):
        w = self.testCreateAnnouncement()
        w.delete()
        self.assertTrue(w,None)
