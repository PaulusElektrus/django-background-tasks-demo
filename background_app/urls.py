from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), # Homepage
    path('starttask/<int:task_id>', views.start_task, name="StartTask"), # Link to start the tasks
    path('tasks', views.tasks, name="TaskStatus"), # Task Status Page
]