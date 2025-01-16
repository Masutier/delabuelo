from django.db import models
from django.contrib.auth.models import User
from products.models import *


class BasketDb(models.Model):
    id = models.IntegerField(primary_key=True)
    transac_code = models.CharField(max_length=20, blank=True, null=True)
    vendedor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    customer = models.CharField(max_length=20, blank=True, null=True)
    product = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    sale_quantity = models.IntegerField(blank=True, null=True)
    sale_price = models.IntegerField(blank=True, null=True)
    pay = models.CharField(max_length=50, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.id
