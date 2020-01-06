from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import date
from taskmanager.tasks.models import Task
from taskmanager.tasks.forms import Task_form

# Create your views here.

def home(request):
    tasks = Task.objects.search('')
    template_name = 'home.html'
    context = { 
        'tasks' : tasks
        }
    return render(request, template_name, context)

def new_task(request):
    message = ''

    if request.method == 'POST':
        form = Task_form(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.status = 'new'
            task.save()
            message = 'Tarefa salva.'
        
    template_name = 'newtask.html'
    context = { 
        'form' : Task_form(),
        'message': message
        }
    return render(request, template_name, context)

def remove_task(request, pk):
    task= get_object_or_404(Task, pk=pk)    
    task.delete()
    return redirect('/home/')

def edit_task(request, pk):
    task= get_object_or_404(Task, pk=pk)    
    task.status = 'done'
    task.save()
    return redirect('/home/')