"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myprojectapp import views

urlpatterns = [
    path('', views.main),
    path('about/', views.about),
    path('add-to-cart/', views.cart),
    path('men/', views.men),
    path('women/', views.women),
    path('single/', views.single),
    path('404/', views.page404),

    path('admin/', admin.site.urls),
]
