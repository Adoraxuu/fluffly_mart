from django.shortcuts import render

def pay(request):
    return render(request, 'finance/pay.html')

def refund_invoice(request):
    return render(request, 'finance/refund_invoice.html')