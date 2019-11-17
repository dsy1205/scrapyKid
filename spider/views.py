from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def index(request):
    print(len(request.GET['webRoot']))
    return render(request, 'index.html')

