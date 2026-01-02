from django.contrib import admin
from .models import Registry

@admin.register(Registry)
class RegistryAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'is_public', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_filter = ('is_public',)
