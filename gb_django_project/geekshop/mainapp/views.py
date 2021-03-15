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
        'products': products
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    basket = 0

    if request.user.is_authenticated:
        basket = sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat=True)))

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
            'basket': basket
        }
        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[3:5]
    content = {
        'title': title,
        'links_menu': links_menu,
        'products': same_products,
        'basket': basket
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    # with open(settings.BASE_DIR / 'contacts_list.json', 'r', encoding='utf-8') as f:
    #     contacts = json.load(f)
    contacts = Contact.objects.all()
    content = {
        'title': 'Контакты',
        'contacts': contacts
    }
    return render(request, 'mainapp/contact.html', content)
