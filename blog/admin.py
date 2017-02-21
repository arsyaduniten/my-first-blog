from django.contrib import admin
from .models import Post #import the Post models from models.py
# Register your models here.

admin.site.register(Post) #register the model