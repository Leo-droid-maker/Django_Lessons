from django.shortcuts import render, get_object_or_404
from myprojectapp.models import PageCategories, ProductCategory, Product, BottomBanners


# Create your views here.

def main(request):
    products = Product.objects.all()[:4]
    bottom_banners = BottomBanners.objects.all()

    content = {
        'title': 'home',
        'products': products,
        'bottom_banners': bottom_banners,
    }

    return render(request, 'myprojectapp/index.html', content)


def about(request):
    content = {
        'title': 'about',
    }
    return render(request, 'myprojectapp/about.html', content)


def single(request, pk):
    categories_menu = ProductCategory.objects.all()
    product = get_object_or_404(Product, pk=pk)

    content = {
        'title': 'single',
        'product': product,
        'categories_menu': categories_menu
    }
    return render(request, 'myprojectapp/single.html', content)


def page404(request):
    content = {
        'title': '404',
    }
    return render(request, 'myprojectapp/404.html', content)
