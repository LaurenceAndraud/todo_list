from django.test import TestCase
from django.urls import reverse
from .models import Project, Task
from django.contrib.auth.models import User

class ProjectTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.project = Project.objects.create(name="Test Project", description="A test project")

    def test_project_creation(self):
        response = self.client.post(reverse('project_create'), {
            'name': 'New Project',
            'description': 'Description of new project',
        })
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Project.objects.count(), 2)  

    def test_project_detail_view(self):
        """Test pour vérifier la vue de détail du projet"""
        response = self.client.get(reverse('project_detail', kwargs={'pk': self.project.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Project')  
        self.assertContains(response, 'A test project')  

    def test_task_creation(self):
        """Test pour vérifier la création d'une tâche pour un projet"""
        response = self.client.post(reverse('task_create', kwargs={'pk': self.project.pk}), {
            'title': 'Test Task',
            'description': 'A task for the project',
            'due_date': '2024-12-31 23:59:59',
        })
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Task.objects.count(), 1) 
        task = Task.objects.first()
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.project, self.project)  

class TaskTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.project = Project.objects.create(
            name="Test Project",
            description="A test project",
            owner=self.user  
        )

    def test_task_edit(self):
        self.assertEqual(self.project.owner.username, "testuser")
