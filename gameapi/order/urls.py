from django.urls import path

from .views import CartView, OrderSummaryView, CheckoutView, OrderHistoryView

urlpatterns = [
        path('api/v1/addtocart/<int:pk>/', CartView.as_view() , name='add_cart'),
        path('api/v1/ordersummary/', OrderSummaryView.as_view(), name='order_summary'),
        path('api/v1/checkout/', CheckoutView.as_view(), name='order_checkout'),
        path('api/v1/orderhistory/', OrderHistoryView.as_view(), name='order_history'),
]