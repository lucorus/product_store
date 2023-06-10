from django.urls import path, include
from .views import *


urlpatterns = [
    path('', main_page, name='main_page'),
    path('categories', categories, name='categories'),
    path('add_basket/<str:title>', include('user_profile.urls'), name='add_basket'),
]


