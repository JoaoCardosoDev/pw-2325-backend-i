from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from products.models import Product

# Create your views here.

class ProductsView(ListView):
    model = Product
    queryset=Product.objects.filter(enabled=True).all()

class ProductDetail(DetailView):
    model = Product
    slug_field="name"
    
    # def get_context(self, **kwargs):
    #     context = super().get_context(**kwargs)
    #     return context
