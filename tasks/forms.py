from django import forms
from .models import Project, Task, SubTask

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'priority', 'due_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].widget.attrs['readonly'] = True

class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['name', 'is_complete']
