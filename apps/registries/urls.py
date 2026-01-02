from django.urls import path
from .views import registry_detail

app_name = 'registries'

urlpatterns = [
    path('<slug:slug>/', registry_detail, name='detail'),
]
