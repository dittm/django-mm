# example/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from example.views import index, carousel, project,carouselSmall, poems, poem1, poem2, poem4, films, monroe, letters, letter1, works, drawings, entity_detail, entity_list, letter_detail_view

urlpatterns = [
    path('', index, name='index'),
    path('carousel-m/', carousel, name='carousel-m'),
    path('carousel-s/', carouselSmall, name='carousel-s'),
    path('project/', project, name='project'),
    path('films/', films, name='films'),
    path('monroe/', monroe, name='monroe'),
    path('drawings/', drawings, name='drawings'),
    path('works/', works, name='works'),
    path('letters/', letters, name='letters'),
    path('letters/1', letter1, name='letter1'),
    path('poems/', poems, name='poems'),
    path('poems/1', poem1, name='poem1'),
    path('poems/2', poem2, name='poem2'),
    path('poems/4', poem2, name='poem4'),
    path('entities/', entity_list, name='entity_list'),
    path('entity/<int:pk>/', entity_detail, name='entity_detail'),
    path('works/letters/<int:letter_id>/', letter_detail_view, name='letter_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)