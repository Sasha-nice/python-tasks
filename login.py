"""
Декоратор, проверяющий есть ли пользователь в объекте HttpRequest, 
иначе - редирект на страницу логина
"""

from django.shortcuts import redirect


def login_required(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('/login/', next = request.path)
        else:
            return function(request, *args, **kwargs)
    return wrapper