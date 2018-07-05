# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .models import Column, Article, User
from django.shortcuts import redirect
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms


def index(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
    # username = User.objects.filter(username__exact='test', )[0]
    username = request.COOKIES.get('username', '')
    return render(request, 'index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
        'username': username,
    })


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    username = request.COOKIES.get('username', '')
    return render(request, 'news/column.html', {'username':username,'column': column})


def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)
    username = request.COOKIES.get('username', '')
    if article_slug != article.slug:
        return redirect(article, permanent=True)

    return render(request, 'news/article.html', {'username':username,'article': article})


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
                if User.objects.filter(username__exact=username) :
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
                if user :
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
        response =HttpResponseRedirect('/')
        #清理cookie里保存username
        response.delete_cookie('username')
        return response