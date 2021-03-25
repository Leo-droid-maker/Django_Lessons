from random import sample

from django.shortcuts import render, get_object_or_404
from basketapp.models import Basket
from django.conf import settings
from mainapp.models import Product, ProductCategory, Contact


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
        'products': products,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/index.html', content)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
        # basket = sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat=True)))
    return []


def get_hot_product():
    products_list = Product.objects.all()
    return sample(list(products_list), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def products(request, pk=None):
    title = 'товары'
    links_menu = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all().order_by('price')
            category_item = {'name': 'все', 'pk': 0}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category=category_item)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category_item,
            'products': products_list,
            'basket': get_basket(request.user)
        }
        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'products': same_products,
        'hot_product': hot_product,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    links_menu = ProductCategory.objects.all()
    content = {
        'title': 'страница товара',
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/product.html', content)


def contact(request):
    # with open(settings.BASE_DIR / 'contacts_list.json', 'r', encoding='utf-8') as f:
    #     contacts = json.load(f)
    contacts = Contact.objects.all()
    content = {
        'title': 'Контакты',
        'contacts': contacts,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/contact.html', content)
