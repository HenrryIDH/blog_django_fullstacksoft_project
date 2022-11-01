from django.contrib import admin

from .models import Post, Category, Like, PostView, Comment

# Register your models here.

admin.site.register((Post, Category, Like, PostView, Comment))
