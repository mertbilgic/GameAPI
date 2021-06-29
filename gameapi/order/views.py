import uuid

from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

from .models import Order, OrderItem
from .serializers import OrderSummarySerializer, CheckoutSerializer
from product.models import Product


class OrderSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Order.objects.get(user=request.user, ordered=False)
        serializer = OrderSummarySerializer(queryset)
        return Response(serializer.data)

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        item = get_object_or_404(Product, pk=pk)
        order = Order.objects.filter(user=request.user, ordered=False).first()

        order_id = order.order_item.order_id if order != None else str(uuid.uuid4())

        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            user=request.user,
            order_id=order_id
        )
        if order != None:
            if order.items.filter(item__pk=item.pk, order_id=order_id).exists():
                order_item.quantity += 1
                order_item.save()
            else:
                order.items.add(order_item)
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(
                user=request.user, ordered_date=ordered_date, order_item=order_item)
            order.items.add(order_item)

        return redirect("order_summary")


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order = Order.objects.get(user=request.user, ordered=False)
        order.ordered = True
        order.save()
        serializer = CheckoutSerializer(order)
        response = {'message': 'Success checkout order'}
        response.update(serializer.data)
        return Response(response,status=status.HTTP_200_OK)
