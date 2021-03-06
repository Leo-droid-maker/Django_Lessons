from django.shortcuts import render
import json
from geekshop.settings import BASE_DIR


# Create your views here.

def main(request):
    menu_list = [
        {'href': 'main_popular', 'name': 'популярные'},
        {'href': 'main_new', 'name': 'новинки'}
    ]
    content = {
        'title': 'Главная',
        'menu_list': menu_list
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'}

    ]
    content = {
        'title': 'Товары',
        'links_menu': links_menu
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
