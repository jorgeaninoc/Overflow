from django.contrib.auth.models import User
from django.test import TestCase, Client
from Actividades.models import Noticia, Imagen
from Comunidades.models import Comunidad
from datetime import datetime as dt
from datetime import timedelta as td
import django

# Create your tests here.

class ConsultNewsTest(TestCase):

    def testConsultNews(self):
        self.client = Client()
        response = self.client.get('/actividades')
        self.assertEqual(response.status_code, 301)

class AddNewsTest(TestCase):

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


class EditNewsTest(TestCase):

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
