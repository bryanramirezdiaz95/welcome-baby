from django.shortcuts import render, get_object_or_404
from .models import Registry


def registry_list(request):
    registry = get_object_or_404(Registry, is_public=True)

    products = registry.products.all()

    context = {
        "registry": registry,
        "products": products,
    }

    return render(request, "apps/registries/registry_list_product.html", context)
