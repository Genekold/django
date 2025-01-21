from django.db import models


class Minion(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True, )
    description = models.TextField(verbose_name='Описание алкоголя', blank=True, null=True)
    data_purchase = models.DateField(verbose_name='Дата покупки',  blank=True, null=True)
    data_bottling = models.DateField(verbose_name='Дата розлива', blank=True, null=True)
    alcohol_retention = models.IntegerField(verbose_name='Выдержка', blank=True, null=True)
    volume = models.IntegerField(verbose_name='Объем')
    strength = models.IntegerField(verbose_name='Крепость')
    country = models.CharField(max_length=255, verbose_name='Место производства', blank=True, null=True)
    manufacturer = models.CharField(max_length=50, verbose_name='Завод изготовитель',  blank=True, null=True)
    price = models.IntegerField(verbose_name='Цена миньёна')
    photo = models.BooleanField(verbose_name='Фото', default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-data_purchase"]
        indexes = [
            models.Index(fields=['-data_purchase'])
        ]
