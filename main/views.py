from typing import Any

from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    context: dict[str, Any] = {
        'title': 'Home',
        'content': 'Главная страница магазина - HOME',
        'list': ['first', 'second'],
        'dict': ['first', 1],
        'bool': False
    }

    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    return HttpResponse("About page")
