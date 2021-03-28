from django.conf import settings
from django import template

register = template.Library()


@register.filter(name='media_for_users')
def media_for_users(path_to_avatar: str) -> str:
    if not path_to_avatar:
        path_to_avatar = "users_avatars/m8.jpg"

    return f'{settings.MEDIA_URL}{path_to_avatar}'


def media_for_products(path_to_media: str) -> str:
    if not path_to_media:
        path_to_media = 'products_images/default.png'

    return f'{settings.MEDIA_URL}{path_to_media}'


register.filter('media_for_products', media_for_products)
