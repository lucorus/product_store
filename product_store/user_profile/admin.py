from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'slug']
    prepopulated_fields = {'slug': ('username',)}


class BasketAdmin(admin.ModelAdmin):
    list_display = ['pk', 'owner']


class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'count', 'price']


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(ProductInBasket, ProductInBasketAdmin)
