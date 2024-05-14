from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    
    return redirect('home')

def mark_as_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.save()

    return redirect('home')