from django.contrib import admin

from products.models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=("id","name","price","enabled")
    list_editable=("enabled", "price")