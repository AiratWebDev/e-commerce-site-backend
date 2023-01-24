from django.shortcuts import render
from rest_framework import generics
from .models import Reviews
from .serializers import ReviewsSerializer


class ReviewsAPI(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
