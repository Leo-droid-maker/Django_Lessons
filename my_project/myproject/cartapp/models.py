from django.db import models
from django.conf import settings
from myprojectapp.models import Product


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='quantity', default=0)
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name='time')
    total_sum = models.DecimalField(verbose_name='sum of the cart', default=0, decimal_places=2, max_digits=18)
