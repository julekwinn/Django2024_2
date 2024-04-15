from django.http import HttpResponse
from django.shortcuts import render
from food.models import Item

# Create your views here.


def index(request):

    items_list = Item.objects.all()
    return HttpResponse(items_list)


def item(request):
    return HttpResponse("<h1>This is an item page</h1>")