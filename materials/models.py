from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название курса')
    description = models.CharField(max_length=500, verbose_name='Описание курса')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
