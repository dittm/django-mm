# example/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Entity

def index(request):
    return render(request, 'index.html')

def project(request):
    return render(request, 'project.html')

def imprint(request):
    return render(request, 'imprint.html')

def guide(request):
    return render(request, 'guide.html')

def functionality(request):
    return render(request, 'functionality.html')

def introduction(request):
    return render(request, 'introduction.html')

def use(request):
    return render(request, 'use.html')

def bibliography(request):
    return render(request, 'bibliography.html')

def data(request):
    return render(request, 'data.html')

def base(request):
    return render(request, 'base.html')

def carousel(request):
    return render(request, 'carousel-m.html')

def carouselSmall(request):
    return render(request, 'carousel-s.html')

def films(request):
    return render(request, 'filmography.html')

def monroe(request):
    return render(request, 'monroe.html')

def drawings(request):
    return render(request, 'works/drawings/all.html')

def letter1(request):
    return render(request, 'works/letters/letter1.html')

def works(request):
    return render(request, 'works/all.html')

def letters(request):
    return render(request, 'works/letters/all.html')

def poems(request):
    return render(request, 'works/poetry/all.html')

def poem1(request):
    return render(request, 'works/poetry/poem1.html')

def poem2(request):
    return render(request, 'works/poetry/poem2.html')

def poem3(request):
    return render(request, 'works/poetry/poem3.html')

def poem4(request):
    return render(request, 'works/poetry/poem4.html')