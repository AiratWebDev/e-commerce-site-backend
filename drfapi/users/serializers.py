from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['name'] = user.name
        token['email'] = user.email
        # ...

        return token


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'name', 'phone']

    def create(self, validated_data):
        password = validated_data.pop('password', None)  # достаем пароль из даты
        new_user = User.objects.create_user(**validated_data)  # создаем пользователя по оставшейся дате
        new_user.set_password(password)  # устанавливаем хэшируемый пароль
        new_user.save()
        return new_user
