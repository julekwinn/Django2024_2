from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path("", views.indexClassView.as_view(), name="index"),  # poprawione
    path('<int:item_id>/', views.detail, name="detail"),
    path("item", views.item, name="item"),
    path("add", views.create_item, name="create_item"),
    path("update/<int:id>", views.update_item, name="update_item"),
    path("delete/<int:id>", views.delete_item, name="delete_item")
]
