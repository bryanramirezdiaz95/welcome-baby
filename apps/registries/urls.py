from django.urls import path
from .views import *

app_name = 'registries'

urlpatterns = [
    path('', registry_list, name='catalog'),
]
