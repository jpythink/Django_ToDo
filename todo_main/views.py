from django.shortcuts import render
from todo.models import Task

def home(request):
    taskes = Task.objects.filter(is_completed = False)
    
    context = {
        'taskes':taskes
    }
    return render(request, "home.html", context)