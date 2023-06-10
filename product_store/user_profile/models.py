from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True, blank=True)
    slug = models.SlugField()

    # def get_absolute_url(self):
    #     return reverse('profile', kwargs={'slug': self.slug})

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


# промежуточный вариант между корзиной и самим продуктом
# создан для хранения в себе название, слага продукта (чтобы продукт можно было извлечь из бд) и колличества в корзине
class ProductInBasket(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    count = models.PositiveIntegerField(default=0, verbose_name='Количество')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'


class Basket(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='basket', verbose_name='Владелец корзины')
    products = models.ManyToManyField(ProductInBasket, related_name='basket', blank=True, verbose_name='Продукты в корзине')

    def __str__(self):
        return self.owner.username

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
