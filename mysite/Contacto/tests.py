"""
Created by Framework
This file is where the tests of Contacto are declared.
Modified by: Maritza
Modification date: 19/10/18
"""
from django.test import TestCase, Client

class ConsultContactTest(TestCase):

    def testConsultContact(self):
        self.client = Client()
        response = self.client.get('/contacto')
        self.assertEqual(response.status_code, 301)
