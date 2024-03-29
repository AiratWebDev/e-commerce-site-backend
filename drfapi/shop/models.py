import uuid
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from pytils.translit import slugify


class ProductCatalog(models.Model):
    id_catalog = models.AutoField(primary_key=True, verbose_name='ID каталога')
    catalog = models.CharField(max_length=20, verbose_name='Категория товаров', db_index=True, blank=True)
    slug_catalog = models.SlugField(unique=True, default='', null=False, db_index=True, verbose_name='ЧПУ каталога')

    class Meta:
        verbose_name_plural = 'Каталоги'
        verbose_name = 'Каталог'

    def __str__(self):
        return self.catalog


class Product(models.Model):
    id_product = models.AutoField(primary_key=True, editable=False, verbose_name='ID товара')
    good = models.CharField(max_length=50, verbose_name='Название товара', db_index=True)
    slug_product = models.SlugField(unique=True, default='', null=False, db_index=True, verbose_name='ЧПУ товара')
    parent_catalog = models.ForeignKey(ProductCatalog, on_delete=models.PROTECT, null=True,
                                       verbose_name='Родительский каталог')
    price = models.DecimalField(max_digits=7, decimal_places=2, db_index=True, verbose_name='Цена')
    discount = models.DecimalField(max_digits=7, decimal_places=2, db_index=True, blank=True, null=True,
                                   verbose_name='Скидочная цена')
    quantity = models.PositiveIntegerField(verbose_name='Количество товара')
    reviews = models.CharField(max_length=500, verbose_name='Отзывы', blank=True)
    description = models.CharField(max_length=150, verbose_name='Описание товара', blank=True)
    images = models.FileField(upload_to='product_pictures', verbose_name='Фото товара')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.good
