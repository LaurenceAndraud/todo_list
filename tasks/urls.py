from django.urls import path
from .views import (
    ProjectListView, ProjectCreateView, ProjectDetailView, 
    TaskCreateView, TaskDetailView, SubTaskCreateView
)
from . import views

urlpatterns = [
    path('', views.project_list, name='home'),
    path('project/new/', views.ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/task/new/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/subtask/new/', views.SubTaskCreateView.as_view(), name='subtask_create'),
    path('projects/<int:project_id>/add_task/', views.add_task, name='add_task'),
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),
]
