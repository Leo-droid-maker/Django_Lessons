from django.urls import path
from menapp import views


app_name = 'menapp'

urlpatterns = [
    path('', views.men, name='men'),
    path('category/<int:pk>/', views.men, name='men_category'),
]