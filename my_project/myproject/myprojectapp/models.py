from django.db import models


# Create your models here.

class PageCategories(models.Model):
    name = models.CharField(max_length=64, verbose_name='page name', unique=True)
    description = models.TextField(verbose_name='description of page', blank=True)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name='category name', unique=True)
    description = models.TextField(verbose_name='description of page', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name='product name')
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(max_length=64, verbose_name='short description', blank=True)
    description = models.TextField(blank=True, verbose_name='full description')
    price = models.DecimalField(verbose_name='price', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveSmallIntegerField(verbose_name='quantity', default=0)
    size = models.CharField(max_length=4, verbose_name='size', blank=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'


class BottomBanners(models.Model):
    name = models.CharField(max_length=64, verbose_name='bottom banner on index', unique=True)
    image = models.ImageField(upload_to='banner_images', blank=True)
    description = models.TextField(blank=True, verbose_name='banner description')
