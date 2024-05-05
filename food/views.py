from django.http import HttpResponse
from django.shortcuts import render
from food.models import Item
from django.template import loader


# Create your views here.


def index(request):
    items_list = Item.objects.all()
    temmplate = loader.get_template("food/index.html")

    context = {
        "items_list": items_list
    }
    return render(request, "food/index.html", context)


def item(request):
    return HttpResponse("<h1>This is an item page</h1>")


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item
    }
    return render(request,'food/detail.html',context)