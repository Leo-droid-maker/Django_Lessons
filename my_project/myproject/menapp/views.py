from django.shortcuts import render, get_object_or_404
from myprojectapp.models import ProductCategory, Product


# Create your views here.

def men(request, pk=None):
    categories_menu = ProductCategory.objects.all().filter(is_active=True)

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
        }
        return render(request, 'menapp/men.html', content)

    same_men_products = Product.objects.all().filter(gender='male')
    content = {
        'title': 'men',
        'categories_menu': categories_menu,
        'men_products': same_men_products,
    }
    return render(request, 'menapp/men.html', content)
