from django.shortcuts import render, get_object_or_404
from .models import Registry

def registry_detail(request, slug):
    registry = get_object_or_404(
        Registry,
        slug=slug,
        is_public=True
    )

    products = registry.products.all()

    context = {
        'registry': registry,
        'products': products,
    }

    return render(request, 'registries/registry_detail.html', context)
