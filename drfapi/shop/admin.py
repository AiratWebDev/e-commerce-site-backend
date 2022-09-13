from django.contrib import admin
from .models import Product, ProductCatalog


@admin.register(ProductCatalog)
class CatalogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug_catalog': ('catalog', )}
    list_display = ['id_catalog', 'catalog']
    list_editable = ['catalog']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug_product': ('good', )}
    list_display = ['id_product', 'good', 'parent_catalog', 'price', 'quantity', 'description', 'images']
    list_editable = ['good', 'parent_catalog', 'price', 'quantity', 'description']

