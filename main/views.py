from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render, redirect, get_object_or_404

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Simple HTML CRUD view

def home(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        title = request.POST.get('title')
        if task_id:
            task = get_object_or_404(Task, pk=task_id)
            task.title = title
            task.save()
        elif title:
            Task.objects.create(title=title)
        return redirect('/')
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('/')

def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('/')