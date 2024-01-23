from django.urls import path, URLResolver

from . import views

app_name = 'goods'

urlpatterns: list[URLResolver] = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product'),
]

