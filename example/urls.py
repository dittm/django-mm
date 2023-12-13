# example/urls.py
from django.contrib import admin
from django.urls import path


from example.views import index, carousel, project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('carousel-m/', carousel, name='carousel-m'),
    path('project/', project, name='project'),
]