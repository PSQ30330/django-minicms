from django.contrib import admin
from django.contrib.auth import login

from .models import Column, Article, User


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'nav_display', 'home_display')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub_date', 'update_time')


admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(User)
# Register your models here.
from news import models
