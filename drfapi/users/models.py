from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """в джанго уже есть свой юзер, и нам надо расширить его функционал"""

    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]

    name = models.CharField(max_length=50, verbose_name='Имя')
    username = models.CharField(max_length=50, verbose_name='Имя пользователя', default='Some_user')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    password = models.CharField(verbose_name='Пароль', max_length=255, db_index=True)
    email = models.EmailField(verbose_name='Почтовый адрес', unique=True, db_index=True)
    phone = PhoneNumberField(unique=True, verbose_name='Номер телефона')
    gender = models.CharField(default=MALE, max_length=1, choices=GENDERS, verbose_name='Пол')
    birthdate = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house = models.CharField(max_length=20, verbose_name='Дом')
    apartment = models.IntegerField(verbose_name='Квартира', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.surname} {self.name}'
