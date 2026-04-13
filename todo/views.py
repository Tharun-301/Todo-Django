from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task


def addTask(request):
    task = request.POST.get('task')
    Task.objects.create(task=task)
    return redirect('home')