import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product, Contact


def load_from_json(file_name):
    with open(os.path.join(settings.BASE_DIR, f'mainapp/json/{file_name}.json'), 'r', encoding='utf-8') as f:
        return json.load(f)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            ProductCategory.objects.create(**category)
            # ProductCategory.objects.create(name='дом', description='Описание')

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            _category = ProductCategory.objects.get(name=product['category'])
            # print(_category)
            product['category'] = _category
            # print(product)
            Product.objects.create(**product)

        # User.objects.create_superuser('django', 'django@local.gb', 'geekbrains')

        contacts = load_from_json('contacts_list')
        Contact.objects.all().delete()
        for contact in contacts:
            Contact.objects.create(**contact)

        ShopUser.objects.create_superuser('django', 'django@local.gb', 'geekbrains', age=30)



