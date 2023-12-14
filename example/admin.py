# your_app_name/admin.py
from django.contrib import admin
from .models import Image, Entity

admin.site.register(Image)
admin.site.register(Entity)