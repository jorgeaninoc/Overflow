"""
Created by Framework
This file is where the tests of Colabora are declared.
Modified by: Maritza
Modification date: 19/10/18
"""
from django.test import TestCase, Client
from Colabora.forms import ColaboradorForm

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
