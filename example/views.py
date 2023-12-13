# example/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def project(request):
    return render(request, 'project.html')

def base(request):
    return render(request, 'base.html')

def carousel(request):
    return render(request, 'carousel-m.html')