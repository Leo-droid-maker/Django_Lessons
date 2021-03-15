from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from cartapp.models import Cart

from myprojectapp.models import Product


def cart(request):
    content = {
        'title': 'cart'
    }
    return render(request, 'myprojectapp/cart.html', content)


def cart_add(request, pk):
    product_item = get_object_or_404(Product, pk=pk)

    cart_item = Cart.objects.filter(product=product_item, user=request.user).first()
    if not cart_item:
        cart_item = Cart(user=request.user, product=product_item)

    cart_item.quantity += 1
    cart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request):
    pass
