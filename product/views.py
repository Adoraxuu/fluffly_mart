from django.shortcuts import render

def index(request):
    return render(request, 'product/index.html')

def search(request):
    return render(request, 'product/search.html')

def inventory(request):
    return render(request, 'product/inventory.html')

def selected(request):
    return render(request, 'product/selected.html')