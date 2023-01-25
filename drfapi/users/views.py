from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer, UserSerializer
from .models import User


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class Registration(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)  # используем many потому что у нас список пользователей
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # при сохранения применяется метод create
        return Response(serializer.data)
