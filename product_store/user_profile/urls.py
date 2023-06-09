from django.urls import path, include
from .views import *


urlpatterns = [
    path('', profile, name='profile'),
    path('/add_basket/<str:title>', add_basket, name='add_basket'),
    path('clear_basket', clear_basket, name='clear_basket'),
    path('clear_basket/<str:title>', clear_basket, name='clear_basket_1'),
    path('change_count/<str:title>/<str:mark>', change_count, name='change_count'),
    path('/register', user_register, name='register'),
    path('/logout', user_logout, name='logout'),
    path('/login', user_login, name='login'),
]
