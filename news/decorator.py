
from django.shortcuts import redirect
#判断登陆的装饰器

def has_login(func):
    def wrap(request, *args, **kwargs):
        if not request.COOKIES.get('username'):
            print(request.COOKIES.get('username'))
            return redirect('/login/')
        return func(request, *args, **kwargs)
    return wrap



