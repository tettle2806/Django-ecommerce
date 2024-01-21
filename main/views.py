from typing import Any

from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    context: dict[str, Any] = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }

    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context: dict[str, Any] = {
        'title':'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том какой классный этот интернет магазин.'
    }
    return render(request, 'main/about.html', context)
