from django.contrib import admin
from .models import Categories
from .models import Products
# Register your models here.

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

