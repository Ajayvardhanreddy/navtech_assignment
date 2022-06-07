from django.db import models


class Products(models.Model):

    object = None
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    ordered_quantity = models.IntegerField()
    total_amount = models.IntegerField()

