from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *


# вывод продуктов + пагинация
def main_page(request):
    return render(request, 'products/main_page.html', {'product': Product.objects.all()})


# просмотр всех категорий с подкатегориями + пагинация
def categories(request):
    category = Paginator(Category.objects.all(), 4)
    page_number = request.GET.get('page')
    page_object = category.get_page(page_number)
    return render(request, 'products/categories.html', {'category': page_object})


def print_data(reqeust, slug):
    data = reqeust.GET.get('count')
    print(data, '\n', slug)
    return redirect('main_page')

