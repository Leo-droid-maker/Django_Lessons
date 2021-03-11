from django.shortcuts import render
from myprojectapp.models import PageCategories, ProductCategory, Product, BottomBanners


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


def cart(request):
    content = {
        'title': 'cart'
    }
    return render(request, 'myprojectapp/add-to-cart.html', content)


def men(request, pk=None):
    categories_menu = ProductCategory.objects.all()
    content = {
        'title': 'men',
        'categories_menu': categories_menu
    }
    return render(request, 'myprojectapp/men.html', content)


def women(request):
    content = {
        'title': 'women'
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
