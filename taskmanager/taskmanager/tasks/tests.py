from django.test import TestCase
from .models import Task
from django.test.client import Client 

class TaskTestCase(TestCase):
    
    def setUp(self):
        self.task = Task.objects.create(description = 'My_teste', status='new')

    def tearDown(self):
        self.task.delete()

    def test_task_form_success(self):
        data = {'description': 'my new description'}
        path = '/newtask/'
        client = Client()
        
        response = client.post(path, data)
        self.assertEqual(response.status_code, 200)
