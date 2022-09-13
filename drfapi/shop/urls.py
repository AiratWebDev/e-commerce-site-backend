from django.contrib import admin
from django.urls import path, include

from .views import ProductsAPIList, CatalogAPIList, get_img

urlpatterns = [
    path('api/v1/products', ProductsAPIList.as_view()),
    path('api/v1/catalogs', CatalogAPIList.as_view()),
    path('product_pictures/<img_url>', get_img),
]
