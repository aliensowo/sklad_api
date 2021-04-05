from django.db import models

# Create your models here.


class Resources(models.Model):
    title = models.CharField(name='title', verbose_name='Наименование', max_length=128)
    amount = models.IntegerField(name='amount', verbose_name='Количество')
    unit = models.CharField(name='unit', verbose_name='Единица измерения', max_length=64)
    price = models.IntegerField(name='price', verbose_name='Цена в у.е.')
    date = models.DateField(name='date', verbose_name='Дата последнего поступления')

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'

    def __str__(self):
        return str(self.title)


