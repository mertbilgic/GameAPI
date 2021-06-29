from django.urls import path

from .views import CartView, OrderSummaryView, CheckoutView

urlpatterns = [
        path('api/addtocart/<int:pk>/', CartView.as_view() , name='add_cart'),
        path('api/ordersummary/', OrderSummaryView.as_view(), name='order_summary'),
        path('api/checkout/', CheckoutView.as_view(), name='order_checkout'),
]