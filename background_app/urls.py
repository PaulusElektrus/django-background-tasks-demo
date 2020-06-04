from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('starttask/<int:task_id>', views.start_task, name="StartTask"),
    path('tasks', views.tasks, name="TaskStatus"),
]