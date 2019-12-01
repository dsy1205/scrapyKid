#coding=utf-8
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def index(request):
    context = {'title': 'django首页'}
    return render(request, 'spider/index.html', context)
