from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('product/<slug:slug>/', product_detail, name='product_detail'),
]