from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=5)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
