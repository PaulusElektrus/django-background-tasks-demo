from django.shortcuts import render, redirect, HttpResponse
from background_task import background
from background_task.models import Task, CompletedTask

# Create your views here.

@background

def hello(task_id):

    if task_id == 1:
        print("Hello Task 1!")
    
    if task_id == 2:
        print("Hello Task 2!")
        
    if task_id == 3:
        print("Hello Task 3!")


# def background_view(request):
#    hello(repeat=10, repeat_until=None)
#    return HttpResponse("Hello World!")


def home(request):

    return render(request, "home.html")


def start_task(request, task_id):

    hello(task_id)

    return redirect(home)


def tasks(request):

    running_tasks = Task.objects.values('task_name', 'run_at', 'task_params')

    completed_tasks = CompletedTask.objects.values('task_name', 'run_at', 'task_params')

    return render(request, "tasks.html", {'running_tasks': running_tasks, 'completed_tasks': completed_tasks})