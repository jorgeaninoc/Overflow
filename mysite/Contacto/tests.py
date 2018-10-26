"""
Created by Framework
This file is where the tests of Contacto are declared.
Modified by: Maritza
Modification date: 19/10/18
"""
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
# Import libraries needed
>>>>>>> 192f6eaba88b3d1070998b0cdcf4a5f3dc523fb8
from django.test import TestCase, Client
from Actividades.models import Noticia, Imagen
from Comunidades.models import Comunidad
from datetime import datetime as dt
from datetime import timedelta as td

# Test for UC: Consult Contact
class ConsultContactTest(TestCase):

    def testConsultContact(self):
        """
        This test goes to the page /contacto and checks if you can access it.
        """
        self.client = Client()
        response = self.client.get('/contacto')
        self.assertEqual(response.status_code, 301)
