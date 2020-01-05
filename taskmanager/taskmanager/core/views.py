from django.shortcuts import render
from django.http import HttpResponse
from taskmanager.tasks.models import Task

# Create your views here.


def home(request):
    tasks = Task.objects.search('')
    return render(request, 'home.html', {'usuario' : 'Jessyka', 'tasks' : tasks})