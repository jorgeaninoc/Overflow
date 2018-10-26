"""
Created by Framework
This file is where the tests of Contacto are declared.
Modified by: Maritza
Modification date: 19/10/18
"""
# Import libraries needed
from django.test import TestCase, Client

# Test for UC: Consult Contact
class ConsultContactTest(TestCase):

    def testConsultContact(self):
        """
        This test goes to the page /contacto and checks if you can access it.
        """
        self.client = Client()
        response = self.client.get('/contacto')
        self.assertEqual(response.status_code, 301)
