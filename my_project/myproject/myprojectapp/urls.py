from django.urls import path
from myprojectapp import views


app_name = 'myprojectapp'

urlpatterns = [
    path('', views.men, name='men'),
    path('<int:pk>/', views.men, name='men_category'),
]

