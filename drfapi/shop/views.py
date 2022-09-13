from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, ProductCatalog
from .serializers import ProductSerializer, CatalogSerializer


class ProductsAPIList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CatalogAPIList(generics.ListAPIView):
    queryset = ProductCatalog.objects.all()
    serializer_class = CatalogSerializer


def get_img_url(request, img_url):
    return HttpResponse('Тестовый текст')

