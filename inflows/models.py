from django.db import models
from products.models import Product
from suppliers.models import Suppliers


class Inflow(models.Model):
    supplier = models.ForeignKey(Suppliers, on_delete=models.PROTECT, related_name='inflows')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='inflows')
    quantily = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product)
