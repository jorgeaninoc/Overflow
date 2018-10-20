"""
Created by Framework
This file is where the tests of Colabora are declared.
Modified by: Maritza
Date: 19/10/18
"""
from django.test import TestCase

class ConsultColaboraTest(TestCase):

    def testConsultColabora(self):
        self.client = Client()
        response = self.client.get('/colabora')
        self.assertEqual(response.status_code, 301)
