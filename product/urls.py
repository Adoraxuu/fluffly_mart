from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('inventory', views.inventory, name='inventory'),
    path('selected', views.selected, name='selected'),
]