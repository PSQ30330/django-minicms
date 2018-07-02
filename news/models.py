# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='')
    nav_display = models.BooleanField('导航显示', default=False)
    home_display = models.BooleanField('首页显示', default=False)

    def get_absolute_url(self):
        return reverse('column', args=(self.slug, ))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '添加栏目'
        verbose_name_plural = '添加栏目'
        ordering = ['name']  # 排序


@python_2_unicode_compatible
class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')

    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256, db_index=True)

    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
    content = models.TextField('内容', default='', blank=True)
    content = UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    def get_absolute_url(self):
        return reverse('article', args=(self.pk, self.slug))

    def __str__(self):
        return self.title

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '添加新闻'
        verbose_name_plural = '添加新闻'


class Gender(models.Model):
    name = models.CharField(max_length=32)


class userinfo(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='用户名', editable=False)
    email = models.EmailField(db_index=True)
    memo = models.TextField()
    img = models.ImageField(upload_to='upload')
    user_type = models.ForeignKey("UserType", null=True, blank=True)
    gender_choices = (
        (0, "男"),
        (1, "女"),
    )
    gender = models.IntegerField(choices=gender_choices, default=1)


class UserType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name