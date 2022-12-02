import time

from django.shortcuts import render, redirect
from TodoList import models
from TodoList.forms import CreateTask
import datetime

def index(request):
    search = request.GET.get('search')
    if search is None or search == '':
        tasks = models.Task.objects.all()
    else:
        tasks = models.Task.objects.filter(task_name__contains=search)

    return render(request, 'TodoList/index.html', {'tasks': tasks})


def add(request):
    form = CreateTask(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'TodoList/add.html', {'form': form})


def update(request, task_id):
    task = models.Task.objects.get(id=task_id)
    form = CreateTask(request.POST or None, instance=task)
    if form.is_valid():
        edited_task = models.Task(task_name=form.cleaned_data['task_name'], created_at=models.Task.objects.get(id=task_id).created_at, modified_at=datetime.datetime.now(), id=task_id)
        edited_task.save()
        return redirect('index')
    return render(request, 'TodoList/update.html', {'form': form, 'task_id': task_id})


def delete(request, task_id):
    task = models.Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')