
from django.urls import path
from . import views


app_name = 'food'

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:item_id>/',views.detail, name="detail"),
    path("item", views.item, name="item"),

    # Add Item form
    path("add", views.create_item, name="create_item"),

    # Edit Item
    path("update/<int:id>", views.update_item, name="update_item")

]