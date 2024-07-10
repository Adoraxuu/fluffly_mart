from django.urls import path, include
from . import views

app_name = 'finance'

urlpatterns = [
    path('pay', views.pay, name='pay'),
    path('refund_invoice', views.refund_invoice, name='refund_invoice'),
]