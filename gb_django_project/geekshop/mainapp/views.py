from django.shortcuts import render
import json
from geekshop.settings import BASE_DIR
from mainapp.models import Product, ProductCategory
from random import shuffle


# Create your views here.

def main(request):

    products = Product.objects.all()[:4]

    menu_list = [
        {'href': 'main_popular', 'name': 'популярные'},
        {'href': 'main_new', 'name': 'новинки'}
    ]
    content = {
        'title': 'Главная',
        'menu_list': menu_list,
        'products': products
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    list_of_products = Product.objects.all()[4:7]
    links_menu = ProductCategory.objects.all()
    content = {
        'title': 'Товары',
        'links_menu': links_menu,
        'list_of_products': list_of_products
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    with open(BASE_DIR / 'contacts_list.json', 'r', encoding='utf-8') as f:
        contacts = json.load(f)

    content = {
        'title': 'Контакты',
        'contacts': contacts
    }
    return render(request, 'mainapp/contact.html', content)
