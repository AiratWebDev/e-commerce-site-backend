# Backend-часть проекта интернет-магазина

### Описание проекта 

Проект в разработке. Реализуется на Django Rest Framework.  
  
• В разделе **shop** представлены каталоги товаров и соответствующие им товары с основной информацией по ним и изображениями.  
• Раздел **users** хранит информацию о пользователях, перезаписанную логику стандартного класса пользователя Django для авторизации и request-методы для изменения данных. Авторизация производится с помощью JWT-токенов и библиотек simplejwt. Для хранения номеров телефонов используется Django Phonenumber Field.  
• Раздел **reviews** служит для хранения данных, полученных с формы отзывов.  
• Для работы с базой данных используется PostgreSQL, а также встроенная admin-панель Django. 

### Стэк разработки:

• Python 3.11  
• Django 4.1.1  
• Django Rest Framework 3.13.1
• PostgreSQL  
• SimpleJWT  
• Django Phonenumber Field и Cors Headers  

### Запуск

```python
python manage.py runserver
```
