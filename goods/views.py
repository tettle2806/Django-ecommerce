from typing import Any

from django.core.paginator import Paginator
from django.db.models.manager import BaseManager
from django.shortcuts import render, HttpResponse, get_list_or_404
from .models import Products, Categories

# Create your views here.


def catalog(request, category_slug) -> HttpResponse:
    if category_slug == 'all':
        goods: BaseManager[Products] = Products.objects.all()
    else:
        goods: BaseManager[Products] = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, per_page=3)
    current_page = paginator.page(1)

    context: dict[str, Any] = {
        'title': 'Home - Каталог',
        'goods': current_page
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug) -> HttpResponse:
    product: Products = Products.objects.get(slug=product_slug)

    context: dict[str, Products] = {
        'product': product
    }

    return render(request, 'goods/product.html', context=context)
