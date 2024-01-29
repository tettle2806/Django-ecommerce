from django.db.models.manager import BaseManager

from goods.models import Categories
from django import template

register = template.Library()


@register.simple_tag()
def tag_categories() -> BaseManager[Categories]:
    return Categories.objects.all()

