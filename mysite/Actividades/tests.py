from django.contrib.auth.models import User
from django.test import TestCase, Client
from Actividades.models import Noticia
from Comunidades.models import Comunidad,Imagen
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
        i= Imagen.objects.create(nombre='Prueba I',path='media/images/agua.jpg')
        im = Imagen.objects.get(nombre='Prueba I')
        c = Comunidad.objects.create(nombre="Prueba C", descripcion="Lorem Ipsum")
        c.imagenes.add(im)
        co = Comunidad.objects.get(nombre='Prueba C')
        n = Noticia.objects.create(titulo='Prueba', texto='Lorem Ipsum',
        fechaInicio=django.utils.timezone.now(), fechaFin=django.utils.timezone.now() + django.utils.timezone.timedelta(30)
        ,comunidad=co)
        n.imagenes.add(im)
        return n


    def testaddNews(self):
        w = self.testCreateNews()
        self.assertTrue(isinstance(w, Noticia))
