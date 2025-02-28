from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'notes\index.html')

def home(request):
    return render(request, 'notes\home.html')

def base(request):
    notes = ["Перша нотатка", "Друга нотатка", "Третя нотатка"]
    return render(request, 'notes/base.html', {'notes': notes})