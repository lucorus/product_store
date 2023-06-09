from django.db import models


# список фотографий, добавляемых к продукту (на случай если в будущем придётся изменить количество фото продукта)
class ProductPhoto(models.Model):
    product_photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фотографии продуктов'


class Product(models.Model):
    title = models.CharField(max_length=256, unique=True, verbose_name='Название')
    slug = models.SlugField()
    price = models.PositiveIntegerField(verbose_name='Цена')
    photos = models.ManyToManyField(ProductPhoto, related_name='product', verbose_name='Фотографии')
    subcategory = models.ForeignKey('SubCategory', on_delete=models.PROTECT, related_name='product', verbose_name='Подкатегория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='photos', verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='photos', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

