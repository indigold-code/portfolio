from django.shortcuts import render
from django.views.generic.list import ListView


def home(request):
    return render(request, 'base/home.html')

