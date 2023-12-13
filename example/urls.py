# example/urls.py
from django.contrib import admin
from django.urls import path

from example.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]