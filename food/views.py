from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. Food page is here!")


def item(request):
    return HttpResponse("<h1>This is an item page</h1>")