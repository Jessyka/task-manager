from django.test import TestCase
from django.test.client import Client

class HomeViewTest(TestCase):
    def test_home_status_code(self):
        cliente = Client()
        response = cliente.get('/home/')
        self.assertEqual(response.status_code, 200)


    def test_home_template_used(self):
        cliente = Client()
        response = cliente.get('/home/')
        self.assertTemplateUsed(response, 'home.html')
