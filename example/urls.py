# example/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from example.views import index, carousel, project,carouselSmall, data, imprint, guide, functionality, introduction, use, bibliography, poems, poem1, poem2, poem3, poem4, films, monroe, letters, letter1, works, drawings

urlpatterns = [
    path('', index, name='index'),
    path('carousel-m/', carousel, name='carousel-m'),
    path('carousel-s/', carouselSmall, name='carousel-s'),
    path('project/', project, name='project'),
    path('films/', films, name='films'),
    path('monroe/', monroe, name='monroe'),
    path('imprint/', imprint, name='imprint'),
    path('guide/', guide, name='guide'),
    path('functionality/', functionality, name='functionality'),
    path('introduction/', introduction, name='introduction'),
    path('use/', use, name='use'),
    path('bibliography/', bibliography, name='bibliography'),
    path('data/', data, name='data'),
    path('drawings/', drawings, name='drawings'),
    path('works/', works, name='works'),
    path('letters/', letters, name='letters'),
    path('letters/1', letter1, name='letter1'),
    path('poems/', poems, name='poems'),
    path('poems/1', poem1, name='poem1'),
    path('poems/2', poem2, name='poem2'),
    path('poems/3', poem3, name='poem3'),
    path('poems/4', poem4, name='poem4'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)