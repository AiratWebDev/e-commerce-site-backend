from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.views.generic import DetailView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Product, ProductCatalog  # Users
from .serializers import ProductSerializer, CatalogSerializer


class ProductsAPIList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CatalogAPIList(generics.ListAPIView):
    queryset = ProductCatalog.objects.all()
    serializer_class = CatalogSerializer


def get_img(request, img_url):
    return FileResponse(open(f'product_pictures/{img_url}', 'rb'))


# class CabinetUserAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UsersSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )
#
#
# class CabinetAPI(generics.ListCreateAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UsersSerializer
