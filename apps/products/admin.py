from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'registry', 'is_reserved', 'price')
    list_filter = ('is_reserved', 'registry')
    search_fields = ('name',)
