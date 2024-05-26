from django.http import HttpResponse
from django.shortcuts import render, redirect
from food.models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


# def index(request):
#     items_list = Item.objects.all()
#     temmplate = loader.get_template("food/index.html")

#     context = {
#         "items_list": items_list
#     }
#     return render(request, "food/index.html", context)




class indexClassView(ListView):

    model = Item
    template_name = 'food/index.html'
    context_object_name = 'items_list'




class FoodDetail(DetailView):
    model = Item
    template_name = 'food/index.html'





def item(request):
    return HttpResponse("<h1>This is an item page</h1>")


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html',{'form':form})

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("food:index")
    
    return render(request, 'food/item-form.html',{'form':form, 'item':item})

def delete_item(request,id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect("food:index")
    
    return render(request, "food/item-delete.html",{"item":item})
