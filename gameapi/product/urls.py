from django.urls import path

from .views import ProductListView

urlpatterns = [
    path('api/v1/productlist/',ProductListView.as_view(), name='product-view'),
]