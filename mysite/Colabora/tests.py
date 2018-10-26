from django.contrib.auth.models import User
from django.test import TestCase, Client
from Actividades.models import Noticia, Imagen
from Comunidades.models import Comunidad
from datetime import datetime as dt
from datetime import timedelta as td
import django
from Colabora.forms import ColaboradorForm

"""
Created by Framework
This file is where the tests of Colabora are declared.
Modified by: Maritza
Modification date: 19/10/18
"""
class ConsultColaboraTest(TestCase):

    def testConsultColabora(self):
        self.client = Client()
        response = self.client.get('/colabora')
        self.assertEqual(response.status_code, 301)


class OfferCollaborationTest(TestCase):
    def testForm(self):
        form_data = {'nombre': 'prueba','telefono':'1234567',
        'correo':'prueba@gmail.com','empresa':'ITESM'
        }
        form = ColaboradorForm(data=form_data)
        self.assertTrue(form.is_valid())
