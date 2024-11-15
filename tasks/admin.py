from django.contrib import admin
from .models import Project, Task, SubTask

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
    search_fields = ('name', 'owner_username')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'priority', 'due_date', 'project')  
    list_filter = ('status', 'priority')  
    search_fields = ('name', 'project__name')  

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'task', 'is_complete')  
    list_filter = ('is_complete',)  
    search_fields = ('nale', 'task__title')