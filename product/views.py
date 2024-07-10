from django.shortcuts import render

def index(request):
    return render(request, 'product/index.html')


def inventory(request):
    return render(request, 'product/inventory.html')

def selected(request):
    return render(request, 'product/selected.html')

def custom_selected(request):
    products = [
        {'title': '產品1', 'image_url': 'https://via.placeholder.com/300x200', 'price': 149.9, 'sales': 10, 'dsr': 4.8},
        {'title': '產品2', 'image_url': 'https://via.placeholder.com/300x200', 'price': 199.0, 'sales': 15, 'dsr': 4.9},
        {'title': '產品3', 'image_url': 'https://via.placeholder.com/300x200', 'price': 175.0, 'sales': 20, 'dsr': 4.7},
        {'title': '產品4', 'image_url': 'https://via.placeholder.com/300x200', 'price': 89.88, 'sales': 30, 'dsr': 4.6},
        {'title': '產品5', 'image_url': 'https://via.placeholder.com/300x200', 'price': 300.9, 'sales': 5, 'dsr': 4.5},
        {'title': '產品6', 'image_url': 'https://via.placeholder.com/300x200', 'price': 209.0, 'sales': 8, 'dsr': 4.4},
        {'title': '產品7', 'image_url': 'https://via.placeholder.com/300x200', 'price': 79.0, 'sales': 12, 'dsr': 4.3},
        {'title': '產品8', 'image_url': 'https://via.placeholder.com/300x200', 'price': 310.0, 'sales': 6, 'dsr': 4.2},
        {'title': '產品9', 'image_url': 'https://via.placeholder.com/300x200', 'price': 139.9, 'sales': 3, 'dsr': 4.1},
        {'title': '產品10', 'image_url': 'https://via.placeholder.com/300x200', 'price': 270.0, 'sales': 9, 'dsr': 4.0},
    ]
    return render(request, 'product/custom_selected.html', {'products': products})