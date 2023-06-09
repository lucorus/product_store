from django.contrib.auth import login, logout
from django.db.models import QuerySet, Q
from django.shortcuts import render, redirect
from products.models import Product
from .models import *
from .forms import *


# выводим корзину юзера + сумму товаров
def profile(request):
    try:
        basket = Basket.objects.get(owner__slug=request.user.slug)
        products_in_basket = ProductInBasket.objects.filter(basket=basket)
        rate = 0
        quantity = 0
        for item in products_in_basket:
            rate += item.price * item.count
            quantity += item.count
    except:
        basket = None
        quantity = 0
        rate = 0

    return render(request, 'user_profile/profile.html', {'basket': basket, 'price': rate, 'quantity': quantity})


#очищает корзину юзера. если есть доп параметр (название продукта), то убирает только его, иначе всё
def clear_basket(request, title=None):
    if title == None:
        basket = Basket.objects.get(owner__slug=request.user.slug)
        # проходимся по корзине юзера и удаляем содержимое
        for item in basket.products.all():
            item.delete()
    else:
        basket = Basket.objects.get(owner__slug=request.user.slug)
        basket_objects = basket.products.filter(title=title)
        basket_objects.delete()
    return redirect('profile')


# уменьшаем/увеличиваем колличество предетов в корзине в зависимости от mark (+/-)
def change_count(request, title, mark):
    basket = Basket.objects.get(owner__slug=request.user.slug)
    product = ProductInBasket.objects.get(basket=basket, title=title)
    if mark == '-':
        product.count = product.count - 1
    else:
        product.count = product.count + 1
    product.save()

    if product.count < 1:
        clear_basket(request, title)

    return redirect('profile')


# добавляет промежуточный объект между настоящим и корзиной
# добавляет в корзину промежуточный предмет с названием title, количеством count и ценой price
def add_basket(request, title):
    # если ввели в input количества не число, то количество = 1
    try:
        count = int(request.GET.get('count'))
    except:
        count = 1

    user_basket = Basket.objects.get(owner__slug=request.user.slug)
    product = Product.objects.get(title=title)

     # если предмет с таким названием существует, то ничего не делаем
    try:
        t = user_basket.products.get(title=title)
    # иначе создаём промежуточный продукт и добавляем в корзину
    except:
        new_product = ProductInBasket(title=title, count=count, price=int(product.price))
        new_product.save()
        user_basket.products.add(new_product)
        user_basket.save()
    return redirect('profile')


# регистрация юзера
def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.slug = str(user.username)
            user.save()
            basket = Basket.objects.create(owner=request.user)
            basket.save()
            login(request, user)
            return redirect('main_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authorization/authorization.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('main_page')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page')
    else:
        form = UserLoginForm()
    return render(request, 'authorization/authorization.html', {'form': form})
