from django.contrib import admin
from django.urls import path, include
from mainapp import views as mainapp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('contact/', mainapp.contact, name='contact'),

    path('basket/', include('basketapp.urls', namespace='basket')),

    path("popular/", mainapp.main, name='main_popular'),
    path("new/", mainapp.main, name='main_new'),

    path('auth/', include('authapp.urls', namespace='auth')),

    path('admin/', include('adminapp.urls', namespace='admin')),

    # path('admin/', admin.site.urls),
    # path('control/', admin.site.urls),

    path('', include('social_django.urls', namespace='social')),

    path('order/', include('ordersapp.urls', namespace='order'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
