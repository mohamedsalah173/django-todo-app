from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TODO,todoItems
from .forms import TodoForm

def home(request):
    todos  = TODO.objects.all()
    context = {
        "todos":todos
    }
  
    return render(request, 'home.html', context)

def detailed(request, id ):
    todo = TODO.objects.get(id = id)
    items = todo.todoitems_set.all()
    context = {
        "todo":todo,
        "items":items
    }
    return render(request, 'detailed.html', context)

def delete(request, id):
    todo = TODO.objects.get(id = id)
    todo.delete()
    return redirect('/')

def createTodo (request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form":form,
    }
    
    return render(request, 'createTodo.html', context)


def updateTodo(request , id):
    todo = TODO.objects.get(id= id)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST , instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request , 'update.html' , context)