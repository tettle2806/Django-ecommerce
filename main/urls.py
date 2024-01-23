from django.urls import path, URLResolver

from . import views


app_name = 'main'
urlpatterns: list[URLResolver] = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('about_d/', views.delivery_payment, name='about_d')
]

