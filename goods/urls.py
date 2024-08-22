from django.urls import path, URLResolver

from . import views

app_name = 'goods'

urlpatterns: list[URLResolver] = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]

