from django.contrib import admin
from django import forms
from .models import Post, Area, Attraction, Category


admin.site.register(Post)
admin.site.register(Area)
admin.site.register(Attraction)
admin.site.register(Category)

#
# Register your models here.
