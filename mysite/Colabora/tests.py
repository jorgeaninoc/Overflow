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
# Import libraries used.
from django.test import TestCase, Client
from Colabora.forms import ColaboradorForm


"""
Function Delete Consult Colabora
Function description: Anyone can view colabora page.
Function parameters: testCase
return none
"""
# Test for the UC: Consult Colabora
class ConsultColaboraTest(TestCase):
    # This function gets the site /colabora and returns if it is possible to access it.
    def testConsultColabora(self):
        self.client = Client()
        response = self.client.get('/colabora')
        self.assertEqual(response.status_code, 301)



"""
Function Offer Colaboration
Function description: Anyone can view signup to collaborate.
Function parameters: testCase
return none
"""
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
        # Check if the object exists in the DB.
        self.assertTrue(form.is_valid())
