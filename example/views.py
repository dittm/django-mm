# example/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Entity

def index(request):
    return render(request, 'index.html')

def project(request):
    return render(request, 'project.html')

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

def entity_list(request):
    entities = Entity.objects.all()
    return render(request, 'entity_list.html', {'entities': entities})

def entity_detail(request, pk):
    entity = get_object_or_404(Entity, pk=pk)
    images = entity.images.all()
    return render(request, 'entity_detail.html', {'entity': entity, 'images': images})

def letter_detail_view(request, letter_id):
    letter = get_object_or_404(Entity, pk=letter_id, category='letter')
    images = letter.images.all()

    context = {
        'letter': letter,
        'images': images,
    }

    return render(request, 'works/letters/letter_detail.html', context)