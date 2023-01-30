from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer, UserSerializer
from .models import User


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class Registration(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # при сохранения применяется метод create
        return Response(serializer.data)

    def patch(self, request):
        data = request.data
        user_email = data.get('email')
        user = User.objects.get(email=user_email)

        user.name = data.get('name', user.name)
        user.username = data.get('username', user.username)
        user.surname = data.get('surname', user.surname)
        user.email = data.get('email', user.email)
        user.phone = data.get('phone', user.phone)
        user.gender = data.get('gender', user.gender)
        user.birthdate = data.get('birthdate', user.birthdate)
        user.city = data.get('city', user.city)
        user.street = data.get('street', user.street)
        user.house = data.get('house', user.house)
        user.apartment = data.get('apartment', user.apartment)

        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # def get(self, request):
    #     users = User.objects.all()
    #     serializer = UserSerializer(users, many=True)  # используем many потому что у нас список пользователей
    #     return Response(serializer.data)


class GetUserInfo(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'name']

