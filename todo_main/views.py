from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    complated_tasks = Task.objects.filter(is_completed = True)
    
    context = {
        'tasks':tasks,
        'complated_tasks': complated_tasks
    }
    return render(request, "home.html", context)