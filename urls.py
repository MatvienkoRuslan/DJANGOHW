"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import numpy as np

def home(request):
    return HttpResponse('<h1> Домашня сторінка </h1>')

def prog(request, start, count, step):
    result = np.arange(0, count) * step + start
    return HttpResponse(str(result))

def greet(request, username):
    return HttpResponse(f'<h1> Привіт, {username}  </h1>')


from django.http import HttpResponse

def number_of_Fibonacci(request, value):
    def fib(num: int) -> int:
        if num <= 0:
            return 0
        if num <= 1:
            return 1

        a = 0
        b = 1
        for _ in range(1, num):
            a, b = b, b + a

        return b

    counter = fib(value)
    return HttpResponse(counter)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prog/<int:start>/<int:count>/<int:step>/', prog),
    path('Fib/<int:value>/', number_of_Fibonacci),
    path('greet/<str:username>/', greet),
    path('', home)
]
