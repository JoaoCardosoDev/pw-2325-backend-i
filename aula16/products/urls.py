from django.urls import path

from products.views import ProductDetail, ProductsView

urlpatterns = [
    path("", ProductsView.as_view(), name="product_list"),
    path("<slug>", ProductDetail.as_view(), name="product_detail")
]