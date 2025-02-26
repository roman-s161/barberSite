
from django.db import models
from django.core.validators import MinLengthValidator



# Класс для записи на стрижку
class Visit(models.Model):

    STATUS_CHOICES = [
        (0, 'Не подтверждена'),
        (1, 'Подтверждена'),
        (2, 'Отменена'),
        (3, 'Выполнена'),
    ]

    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name='Статус')
    master = models.ForeignKey('Master', on_delete=models.CASCADE, verbose_name='Мастер')
    services = models.ManyToManyField('Service', verbose_name='Услуги')

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


# Класс для мастеров
class Master(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=255, verbose_name='Домашний адрес')
    photo = models.ImageField(upload_to='masters/photos/', blank=True, null=True, verbose_name='Фотография')
    services = models.ManyToManyField('Service', related_name='masters', verbose_name='Услуги')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"


# Класс для услуг
class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


"""
Модель отзыв
Поля
- Имя
- Текст
- Мастер (Внешний ключ)
- Рейтиг
- Дата создания (автоматически)
- Статус
    - Опубликован
    - Не проверен
    - Одобрен
    - Отклонен
"""

class Review(models.Model):
    STATUS_CHOICES = [
        (0, 'Опубликован'),
        (1, 'Не проверен'),
        (2, 'Одобрен'),
        (3, 'Отклонен'),
    ]

    RAITING_CHOICES = [
        (1, 'Ужасно'),
        (2, 'Плохо'),
        (3, 'Нормально'),
        (4, 'Хорошо'),
        (5, 'Отлично'),
    ]

    name = models.CharField(max_length=50, verbose_name='Имя')
    text = models.TextField(max_length=400, verbose_name='Текст', validators=[MinLengthValidator(30)])
    master = models.ForeignKey('Master', on_delete=models.CASCADE, verbose_name='Мастер')
    rating = models.IntegerField(choices=RAITING_CHOICES, verbose_name='Рейтинг')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name='Статус')
