from django.db import models
from django.conf import settings

from product.models import Product

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    order_id = models.CharField(max_length=36)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.order_id}-{self.quantity}-{self.item.item_name}"
        
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    order_item = models.ForeignKey(OrderItem,on_delete=models.CASCADE,related_name='%(class)s_oder_id')
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username



