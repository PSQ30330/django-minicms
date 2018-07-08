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
        return self.title,self.slug


    class Meta:
        verbose_name = '发布新闻'
        verbose_name_plural = '发布新闻'


class Gender(models.Model):
    name = models.CharField(max_length=32)


@python_2_unicode_compatible
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    REQUIRED_FIELDS=['email']
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class NewsComment(models.Model):
    username = models.CharField('用户名',max_length=50)
    comment = models.TextField('评论内容')
    article = models.CharField('文章',max_length=50)

    class Meta:
        verbose_name = '新闻评论'
        verbose_name_plural = verbose_name
    # def __str__(self):
    #     return self.comment[:20],self.username
class Like(models.Model):
    username = models.CharField('用户名',max_length=50)
    like = models.CharField('点赞',max_length=50)
    article = models.CharField('文章', max_length=50)

    class Meta:
        verbose_name_plural='点赞'

class Start(models.Model):
    username = models.CharField('用户名',max_length=100)
    start = models.CharField('收藏',max_length=100)
    class Meta:
        verbose_name_plural='收藏'