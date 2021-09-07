from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1> HelloWorld</h1>')


def new(request):
    return HttpResponse('<h1> new applications</h1>')
