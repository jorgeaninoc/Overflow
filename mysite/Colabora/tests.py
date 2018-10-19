from django.test import TestCase

# Testing colabora displayed
class ConsultColaboraTest(TestCase):

    def testConsultColabora(self):
        self.client = Client()
        response = self.client.get('/colabora')
        self.assertEqual(response.status_code, 301)
