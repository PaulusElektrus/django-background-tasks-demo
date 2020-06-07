from django.shortcuts import render, redirect, HttpResponse # To display the website data
from background_task import background                      # Import the django-background-tasks module
from background_task.models import Task, CompletedTask      # To access the data stored in the database to display the tasks

# Create your views here.

@background # Initialization: Background Decorator

def hello(task_id): # Background Function, parameter must all be serializable as JSON

    if task_id == 1:
        print("Hello Task 1!")
    
    if task_id == 2:
        print("Hello Task 2!")
        
    if task_id == 3:
        print("Hello Task 3!")


# def background_view(request): # Test Function for repeating tasks, HttpResponse happens immediately so you see "hello" function runs in background
#    hello(1, repeat=10, repeat_until=None)
#    return HttpResponse("Hello World!")


def home(request): # renders home.html, located in templates folder

    return render(request, "home.html")


def start_task(request, task_id): # Function is called via urls.py over the home.html and starts the task

    hello(task_id)

    return redirect(home)


def tasks(request): # Shows the database entrys for running and completed tasks

    running_tasks = Task.objects.values('task_name', 'run_at', 'task_params')

    completed_tasks = CompletedTask.objects.values('task_name', 'run_at', 'task_params')

    return render(request, "tasks.html", {'running_tasks': running_tasks, 'completed_tasks': completed_tasks})