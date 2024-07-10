from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('inventory', views.inventory, name='inventory'),
    path('selected', views.selected, name='selected'),
    path('selected/custom', views.custom_selected, name='custom_selected'),
]