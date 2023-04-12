from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo, TodoItem
from .forms import TodoForm, UserCreation

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .filters import TodoFilter

# Create your views here.

@login_required(login_url = 'login')
def home(request):
    user = request.user
    filter = TodoFilter()
    todos = Todo.objects.filter(user = user)
    if request.method == 'GET':
        output = TodoFilter(request.GET, queryset = todos)
        todos = output.qs
    todo_item = []
    for todo in todos:
        items = todo.todoitem_set.all()
        pair = (todo, items)
        todo_item.append(pair)
    context = {
        'todo_item': todo_item,
        'user': user,
        'filter': filter,
    }
    # return HttpResponse(message)
    return render(request, 'home.html', context)


def detailed(request, id):
    todo = Todo.objects.get(id=id)
    items = todo.todoitem_set.all()
    context = {'todo': todo,
               'items': items}
    return render(request, 'detail.html', context)


def create(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'update.html', context)


def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')

#django signals (search)
def createUser(request):
    form = UserCreation()
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form,
    }
    return render(request, 'signup.html', context)

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    user = request.user
    logout(request) 
    return redirect('/login')