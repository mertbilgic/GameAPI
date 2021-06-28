from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name')
    
    class Meta:
        model = OrderItem
        fields = ['item_name','quantity']

class OrderSummarySerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Order
        fields = ('pk','username', 'items', 'ordered','ordered_date')