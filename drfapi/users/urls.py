from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import MyTokenObtainPairView, Registration, GetUserInfo

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/register/', Registration.as_view(), name='user_registration'),
    path('api/user/get_info/', GetUserInfo.as_view(), name='get_info'),
]
