import django_filters

from product.models import Product

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['name', 'year', 'category']