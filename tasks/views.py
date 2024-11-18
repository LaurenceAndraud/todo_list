from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Project, Task, SubTask
from .forms import ProjectForm, TaskForm, SubTaskForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

def project_list(request):
    return HttpResponse("Bienvenue sur la to-do list !")

class ProjectListView(ListView):
    model = Project
    template_name = 'tasks/project_list.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for project in context['projects']:
            tasks_for_project = Task.objects.filter(project=project)
            project.tasks_list = tasks_for_project
        return context

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description']
    template_name = 'tasks/project_form.html'
    success_url = reverse_lazy('project_list')

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/project_form.html'

    def form_valid(self, form):
        form.instance.project_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.project.id})

class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'tasks/subtask_form.html'

    def form_valid(self, form):
        form.instance.task_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.object.task.id})

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'tasks/project_detail.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

def add_task(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', project_id=project.id) 
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form, 'project': project})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    subtasks = task.subtasks.all()
    return render(request, 'tasks/task_detail.html', {'task': task, 'subtasks': subtasks})

