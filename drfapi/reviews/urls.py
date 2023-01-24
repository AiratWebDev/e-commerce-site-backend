from django.urls import path
from .views import ReviewsAPI

urlpatterns = [
    path('api/v1/reviews', ReviewsAPI.as_view()),
]
