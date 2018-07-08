# -*- coding: utf-8 -*-
from .models import Column, Article, User, NewsComment, Like
from django import forms
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from news.decorator import has_login
from django.contrib import messages

def index(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
    username = request.COOKIES.get('username', '')
    return render(request, 'index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
        'username': username,
    })


# 文章总展示
def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    print(column.article_set.all, column_slug)
    username = request.COOKIES.get('username', '')

    return render(request, 'news/column.html', {'username': username, 'column': column, })


class CommentForm(forms.ModelForm):
    class Meta:
        model = NewsComment
        fields = ['username', 'comment', 'article']


class CommentsForm(forms.Form):
    comment = forms.CharField(label='pinglun', max_length=50)

    @csrf_exempt
    def post(request):
        if request.method == 'POST':
            comment_form = CommentsForm(request.POST)
            username = request.COOKIES.get('username', '')
            id = request.path
            if comment_form.is_valid():
                comment = comment_form.cleaned_data['comment']
                print(comment_form.cleaned_data['comment'], username, id)
                NewsComment.objects.create(comment=comment, username=username, article='34')
                c = NewsComment.objects.filter(username='test')
                print(c)
                return redirect(request.META['HTTP_REFERER'])
        else:
            return render_to_response('comment.html')


# 文章详情
@has_login
def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)
    # comment =NewsComment.objects.filter(article=pk)
    username = request.COOKIES.get('username', '')

    if request.method == 'POST':

        comment_form = CommentsForm(request.POST)
        username = request.COOKIES.get('username', '')

        if comment_form.is_valid():
            comment = comment_form.cleaned_data['comment']
            print(comment_form.cleaned_data['comment'], username, pk)
            NewsComment.objects.create(comment=comment, username=username, article=pk)

        return redirect(reverse(article_detail, args=[pk, article_slug]))
    else:
        if article_slug != article.slug:
            return redirect(article, permanent=True)
        c = NewsComment.objects.filter(article=pk).all()
        # like = Like.objects.filter(article=pk).all()
        like =['as','sad']
        return render(request, 'news/article.html',
                      {'article': article, 'comment': c, 'username': username, 'pk': pk, 'like': like,'article_slug':article_slug})


# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')

    @csrf_exempt
    def regist(request):
        if request.method == 'POST':
            userform = UserForm(request.POST)
            if userform.is_valid():
                username = userform.cleaned_data['username']
                password = userform.cleaned_data['password']
                email = userform.cleaned_data['email']
                if User.objects.filter(username__exact=username):
                    return HttpResponse('已经存在此用户')
                else:
                    User.objects.create(username=username, password=password, email=email)
                    # userform.save()
                    return redirect('/')
        else:
            userform = UserForm()
        return render_to_response('regist.html', {'userform': userform})

    @csrf_exempt
    def login(request):
        if request.method == 'POST':
            userform = UserForm(request.POST)
            if userform.is_valid():
                username = userform.cleaned_data['username']
                password = userform.cleaned_data['password']

                user = User.objects.filter(username__exact=username, password__exact=password)
                if user:
                    # return redirect('/')
                    response = HttpResponseRedirect('/')
                    # 将username写入浏览器cookie,失效时间为3600
                    response.set_cookie('username', username, 3600)
                    return response
                else:
                    return HttpResponse('用户名或密码错误,请重新登录')

        else:
            userform = UserForm()
        return render_to_response('login.html', {'userform': userform})

    @csrf_exempt
    def logout(request):
        response = HttpResponseRedirect('/')
        # 清理cookie里保存username
        response.delete_cookie('username')
        return response

@has_login
@csrf_exempt
def like(request):
    if request.method == 'POST':
        article = request.POST.get('article')
        article_slug = request.POST.get('article_slug')
        username = request.COOKIES.get('username', '')
        print(username,article)
        if Like.objects.filter(username=username,article=article).all():
            messages.error(request,'你之前已经进行过点赞，请换片文章吧！')
        else:
            Like.objects.create( username=username, article=article,like='1')
    return redirect(reverse(article_detail, args=[article, article_slug]))

