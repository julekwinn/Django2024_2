from django.http import HttpResponse
from django.shortcuts import render, redirect
from food.models import Item
from django.template import loader
from .forms import ItemForm


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

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html',{'form':form})