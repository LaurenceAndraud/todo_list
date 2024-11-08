from django.urls import path
from .views import (
    ProjectListView, ProjectCreateView, ProjectDetailView, 
    TaskCreateView, TaskDetailView, SubTaskCreateView
)

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('project/new/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'), 
    path('project/<int:pk>/task/new/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'), 
    path('task/<int:pk>/subtask/new/', SubTaskCreateView.as_view(), name='subtask_create'),
]