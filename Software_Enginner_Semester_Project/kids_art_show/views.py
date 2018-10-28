from django.shortcuts import render
from django.http import HttpResponse
from . import views

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return HttpResponse('<h1>About Page</h1>')