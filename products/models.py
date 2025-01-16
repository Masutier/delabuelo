from django.db import models


class Producto(models.Model):
    CATEGORY = (
        ('Bebidas_Frias', 'Bebidas_Frias'),
        ('Bebidas_Calientes', 'Bebidas_Calientes'),
        ('Comida_Rapida', 'Comida_Rapida'),
        ('Jugos', 'Jugos'),
        ('Cigarrillos', 'Cigarrillos'),
        ('Otros', 'Otros'),
    )

    code = models.CharField(max_length=7, blank=True, null=True)
    categoria = models.CharField(max_length=30, blank=True, null=True, choices=CATEGORY)
    name = models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mesure = models.CharField(max_length=10, blank=True, null=True)
    quantity_un = models.IntegerField(blank=True, null=True)
    cost_un = models.IntegerField(blank=True, null=True)
    sale_price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(default='products/defaultProduct.png', upload_to='products')
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modify = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

