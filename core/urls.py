from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('page.urls')),
    path('order/', include('order.urls')),
    path('product/', include('product.urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
