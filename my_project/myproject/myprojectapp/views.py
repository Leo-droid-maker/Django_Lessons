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
        'bottom_banners': bottom_banners
    }

    return render(request, 'myprojectapp/index.html', content)


def about(request):
    content = {
        'title': 'about'
    }
    return render(request, 'myprojectapp/about.html', content)


def men(request, pk=None):
    cart = 0

    if request.user.is_authenticated:
        cart = sum(list(Cart.objects.filter(user=request.user).values_list('quantity', flat=True)))

    categories_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            men_products = Product.objects.all().filter(gender='male')
            category_item = {'name': 'все', 'pk': 0}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            men_products = Product.objects.filter(category=category_item, gender='male')

        content = {
            'title': 'men',
            'categories_menu': categories_menu,
            'men_products': men_products,
            'category_item': category_item,
            'cart': cart
        }
        return render(request, 'myprojectapp/men.html', content)

    same_men_products = Product.objects.all().filter(gender='male')
    content = {
        'title': 'men',
        'categories_menu': categories_menu,
        'men_products': same_men_products,
        'cart': cart
    }
    return render(request, 'myprojectapp/men.html', content)


def women(request):
    women_products = Product.objects.all().filter(gender='female')
    content = {
        'title': 'women',
        'women_products': women_products
    }
    return render(request, 'myprojectapp/women.html', content)


def single(request):
    content = {
        'title': 'single'
    }
    return render(request, 'myprojectapp/single.html', content)


def page404(request):
    content = {
        'title': '404'
    }
    return render(request, 'myprojectapp/404.html', content)
