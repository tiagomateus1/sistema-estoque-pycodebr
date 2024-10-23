from django.db.models.signals import post_save
from django.dispatch import receiver
from outflows.models import Outflow


@receiver(post_save, sender=Outflow)
def update_product_quantily(sender, instance, created, **kwargs):
    if created:
        if instance.quantily > 0:
            product = instance.product
            product.quantily -= instance.quantily
            product.save()
