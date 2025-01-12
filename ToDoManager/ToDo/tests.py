from django.test import TestCase
from django.urls import reverse

from .models import Task, User
from .forms import CreateTaskForm


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='test username',
            password='test password'
        )
    
    def test_default_values(self):
        '''Test default value for completed row'''
        task = Task.objects.create(
            title='test title',
            description='test description',
            user_id=self.user,
            priority='Низкий'
        )
        self.assertFalse(task.is_completed)

    def test_correct_values(self):
        task = Task.objects.create(
            title='test title',
            description='test description',
            user_id=self.user,
            priority='Низкий'
        )
        self.assertEqual(task.title, 'test title')
        self.assertEqual(task.description, 'test description')
        self.assertEqual(task.priority, 'Низкий')
        self.assertEqual(task.user_id, self.user)


class ViewTest(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
    
    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    

class TaskFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "title": "test title",
            "description": "test description",
            "priority": "Низкий"
        }
        form = CreateTaskForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_invalid_form(self):
        form_data = {"title": ""}  
        form = CreateTaskForm(data=form_data)
        self.assertFalse(form.is_valid())