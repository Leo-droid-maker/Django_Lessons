from django.shortcuts import render


# Create your views here.

def main(request):
    return render(request, 'myprojectapp/index.html')


def about(request):
    return render(request, 'myprojectapp/about.html')


def cart(request):
    return render(request, 'myprojectapp/add-to-cart.html')


def men(request):
    return render(request, 'myprojectapp/men.html')


def women(request):
    return render(request, 'myprojectapp/women.html')


def single(request):
    return render(request, 'myprojectapp/single.html')


def page404(request):
    return render(request, 'myprojectapp/404.html')
