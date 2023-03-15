from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    STATUS_PUBLIC = 'public'
    STATUS_PRIVATE = 'private'
    STATUSES = (
        ('public', 'публичная привычка'),
        ('private', 'приватная привычка')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='место')
    time = models.TimeField(default='00.00', verbose_name='время исполнения')
    action = models.CharField(max_length=150, verbose_name='действие')
    pleasant_or_not = models.BooleanField(default=False, verbose_name='приятная или полезная привычка')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL,  verbose_name='связанная привычка', **NULLABLE)
    frequency = models.IntegerField(default=1, verbose_name='периодичность выполнения (в днях)', **NULLABLE)
    award = models.CharField(max_length=150, verbose_name='награда', **NULLABLE)
    time_to_complete = models.TimeField(default='00:03', verbose_name='время на выполнение')
    status = models.CharField(max_length=20, choices=STATUSES, default=STATUS_PUBLIC, verbose_name='признак публичности')
