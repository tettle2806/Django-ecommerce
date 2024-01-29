from typing import Any

from django.db.models.manager import BaseManager
from django.shortcuts import render, HttpResponse
from .models import Products, Categories

# Create your views here.


def catalog(request) -> HttpResponse:

    goods: BaseManager[Products] = Products.objects.all()

    context: dict[str, Any] = {
        'title': 'Home - Каталог',
        'goods': goods
    }
    return render(request, 'goods/catalog.html', context)


def product(request) -> HttpResponse:
    return render(request, 'goods/product.html')


