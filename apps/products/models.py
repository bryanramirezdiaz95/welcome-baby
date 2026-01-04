from django.db import models
from django.utils.text import slugify
from apps.registries.models import Registry


class Product(models.Model):
    registry = models.ForeignKey(
        Registry, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(blank=True)
    url = models.URLField()
    image_url = models.URLField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_reserved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Si no hay slug, lo generamos automáticamente del nombre
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            # Aseguramos que sea único
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
