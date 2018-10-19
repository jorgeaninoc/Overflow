from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.

class ConsultNewsTest(TestCase):

    def testConsultNews(self):
        self.client = Client()
        response = self.client.get('/Actividades')
        self.assertEqual(response.status_code, 302)
