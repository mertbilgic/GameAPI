from django.urls import path

from .views import ProductListView

urlpatterns = [
    path('api/productlist/',ProductListView.as_view(), name='product-view'),
]