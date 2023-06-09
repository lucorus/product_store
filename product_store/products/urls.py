from django.urls import path, include
from .views import *

#app_name = 'products'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('categories', categories, name='categories'),
    path('print_data/<slug:slug>', print_data, name='print_data'),
    #path('add_basket/<slug:slug>', views.add_basket, name='add_basket')
    path('add_basket/<str:title>', include('user_profile.urls'), name='add_basket'),
]


