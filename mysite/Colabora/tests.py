"""
Created by Framework
This file is where the tests of Colabora are declared.
Modified by: Maritza
Modification date: 19/10/18
"""
# Import libraries used.
from django.test import TestCase, Client
from Colabora.forms import ColaboradorForm

# Test for the UC: Consult Colabora
class ConsultColaboraTest(TestCase):
    # This function gets the site /colabora and returns if it is possible to access it.
    def testConsultColabora(self):
        self.client = Client()
        response = self.client.get('/colabora')
        self.assertEqual(response.status_code, 301)


# Test for UC: Offer Collaboration.
class OfferCollaborationTest(TestCase):
    # This function creates a dict for the ColaboradorForm, passes it to it
    # and checks if it is valid
    # returns nothing.
    def testForm(self):
        form_data = {'nombre': 'prueba','telefono':'1234567',
        'correo':'prueba@gmail.com','empresa':'ITESM'
        }
        form = ColaboradorForm(data=form_data)
        self.assertTrue(form.is_valid())
