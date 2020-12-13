from django.contrib import admin
from django import forms
from .models import Post, Category, Attraction


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Attraction)

#
# Register your models here.
