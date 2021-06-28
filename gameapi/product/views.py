from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductSerializer
from .models import Product

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]