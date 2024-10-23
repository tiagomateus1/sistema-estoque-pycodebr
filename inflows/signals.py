from django.db.models.signals import post_save
from django.dispatch import receiver
from inflows . models import Inflow


@receiver(post_save, sender=Inflow)
def update_product_quantily(sender, instance, created, **kwargs):
    if created:
        if instance.quantily > 0:
            product = instance.product
            product.quantily += instance.quantily
            product.save()
