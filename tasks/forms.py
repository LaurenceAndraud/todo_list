from django import forms
from .models import Project, Task, SubTask

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date']

class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['title', 'is_complete']
