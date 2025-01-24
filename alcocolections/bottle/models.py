from django.db import models
from django.urls import reverse

class PhotoNoneManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(photo=Minion.StatusPhoto.YES)


class Minion(models.Model):
    class StatusPhoto(models.IntegerChoices):
        NO = 0, 'Нет фото'
        YES = 1, 'Есть фото'

    name = models.CharField(max_length=100, verbose_name='Название', unique=True, )
    slug = models.SlugField(max_length=100, blank=False, null=False, unique=True, db_index=True)
    description = models.TextField(verbose_name='Описание алкоголя', blank=True, null=True)
    data_purchase = models.DateField(verbose_name='Дата покупки',  blank=True, null=True)
    date_reg = models.DateField(verbose_name='Дата регистрации',auto_now=True)
    alcohol_retention = models.IntegerField(verbose_name='Выдержка', blank=True, null=True)
    volume = models.IntegerField(verbose_name='Объем')
    strength = models.IntegerField(verbose_name='Крепость')
    country = models.CharField(max_length=255, verbose_name='Место производства', blank=True, null=True)
    manufacturer = models.CharField(max_length=50, verbose_name='Завод изготовитель',  blank=True, null=True)
    price = models.IntegerField(verbose_name='Цена миньёна')
    photo = models.BooleanField(choices=StatusPhoto.choices, verbose_name='Фото', default=StatusPhoto.NO)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='minions')
    tags = models.ManyToManyField('TagMinion', blank=True, related_name='tags')
    bigminion = models.OneToOneField('BigMinion', on_delete=models.SET_NULL, null=True, blank=True, related_name='minon')

    objects = models.Manager()
    manager = PhotoNoneManager()

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['-data_purchase']
        indexes = [
            models.Index(fields=['-data_purchase'])
        ]

    def get_absolute_url(self):
        return reverse('minion', kwargs={'minion_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagMinion(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolut_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class BigMinion(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name