from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.views.generic import DetailView

from .models import Product, ProductCatalog
from .serializers import ProductSerializer, CatalogSerializer


class ProductsAPIList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CatalogAPIList(generics.ListAPIView):
    queryset = ProductCatalog.objects.all()
    serializer_class = CatalogSerializer


def get_img(request, img_url):
    return FileResponse(open(f'product_pictures/{img_url}', 'rb'))
    #return render(request, 'shop/image.html', context=data)

