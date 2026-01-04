from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, slug):
    # Busca el producto por slug, o lanza 404 si no existe
    product = get_object_or_404(Product, slug=slug)
    
    # Pasamos el producto al template
    context = {
        'product': product
    }
    return render(request, 'apps/products/product_detail.html', context)
