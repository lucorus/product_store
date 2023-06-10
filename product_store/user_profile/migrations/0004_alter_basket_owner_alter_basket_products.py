# Generated by Django 4.2.2 on 2023-06-10 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_alter_basket_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to=settings.AUTH_USER_MODEL, verbose_name='Владелец корзины'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='basket', to='user_profile.productinbasket', verbose_name='Продукты в корзине'),
        ),
    ]
