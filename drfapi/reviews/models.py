from django.db import models


class Reviews(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почтовый адрес')
    topic = models.CharField(max_length=70, verbose_name='Тема обращения')
    review = models.CharField(max_length=500, verbose_name='Отзыв')

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'

    def __str__(self):
        return self.topic
