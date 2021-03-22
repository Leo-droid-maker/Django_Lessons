from django.shortcuts import render, get_object_or_404
from myprojectapp.models import PageCategories, ProductCategory, Product, BottomBanners
from cartapp.models import Cart


# Create your views here.

def main(request):
    products = Product.objects.all()[:4]
    bottom_banners = BottomBanners.objects.all()

    content = {
        'title': 'home',
        'products': products,
        'bottom_banners': bottom_banners,
        'cart': get_cart(request.user)
    }

    return render(request, 'myprojectapp/index.html', content)


def about(request):
    content = {
        'title': 'about',
        'cart': get_cart(request.user)
    }
    return render(request, 'myprojectapp/about.html', content)


def get_cart(user):
    if user.is_authenticated:
        return Cart.objects.filter(user=user)
    return []


# def men(request, pk=None):
#
#     categories_menu = ProductCategory.objects.all()
#
#     if pk is not None:
#         if pk == 0:
#             men_products = Product.objects.all().filter(gender='male')
#             category_item = {'name': 'все', 'pk': 0}
#         else:
#             category_item = get_object_or_404(ProductCategory, pk=pk)
#             men_products = Product.objects.filter(category=category_item, gender='male')
#
#         content = {
#             'title': 'men',
#             'categories_menu': categories_menu,
#             'men_products': men_products,
#             'category_item': category_item,
#             'cart': get_cart(request.user)
#         }
#         return render(request, 'myprojectapp/../menapp/templates/menapp/women.html', content)
#
#     same_men_products = Product.objects.all().filter(gender='male')
#     content = {
#         'title': 'men',
#         'categories_menu': categories_menu,
#         'men_products': same_men_products,
#         'cart': get_cart(request.user)
#     }
#     return render(request, 'myprojectapp/../menapp/templates/menapp/women.html', content)

#
# def women(request):
#     women_products = Product.objects.all().filter(gender='female')
#     content = {
#         'title': 'women',
#         'women_products': women_products,
#         'cart': get_cart(request.user)
#     }
#     return render(request, 'myprojectapp/../womenapp/templates/womenapp/women.html', content)


def single(request, pk):
    categories_menu = ProductCategory.objects.all()
    product = get_object_or_404(Product, pk=pk)

    content = {
        'title': 'single',
        'cart': get_cart(request.user),
        'product': product,
        'categories_menu': categories_menu
    }
    return render(request, 'myprojectapp/single.html', content)


def page404(request):
    content = {
        'title': '404',
        'cart': get_cart(request.user)
    }
    return render(request, 'myprojectapp/404.html', content)
