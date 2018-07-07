from django.contrib import admin
from django.contrib.auth import login

from .models import Column, Article, User, NewsComment


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'nav_display', 'home_display')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub_date', 'update_time')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password','email')

class NewsCommentAdmmin(admin.ModelAdmin):
    list_display = ('comment','username')


admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(NewsComment, NewsCommentAdmmin)
# Register your models here.
# Register your models here.
from news import models
