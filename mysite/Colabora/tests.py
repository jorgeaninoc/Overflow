from django.test import TestCase

# Description: Testing colabora displayed
# In charge: Maritza
# Modify by Maritza
# Modify date: 19 oct 18
class ConsultColaboraTest(TestCase):

    def testConsultColabora(self):
        self.client = Client()
        response = self.client.get('/colabora')
        self.assertEqual(response.status_code, 301)
