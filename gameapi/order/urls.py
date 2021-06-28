from django.urls import path

from .views import CartView, OrderSummaryView

urlpatterns = [
        path('api/addtocart/<int:pk>/', CartView.as_view() , name='add_cart'),
        path('api/ordersummary/', OrderSummaryView.as_view(), name='order_summary'),

]