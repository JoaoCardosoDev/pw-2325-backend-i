from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

# Create your views here.

class ProductsView(ListView):
    model = Product
    queryset=Product.objects.filter(enabled=True).all()