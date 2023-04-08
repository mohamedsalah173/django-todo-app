from django.shortcuts import render
from django.http import HttpResponse
from .models import TODO
# Create your views here.
def home(request):
    todos  = TODO.objects.all()
    context = {
        "todos":todos
    }
  
    return render(request, 'home.html', context)