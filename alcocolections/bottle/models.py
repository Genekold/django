from django.db import models
from django.urls import reverse


class PhotoNoneManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=Minion.StatusPhoto.YES)


class Minion(models.Model):
    class StatusPhoto(models.IntegerChoices):
        NO = 0, 'Не активный'
        YES = 1, 'Активный'

    name = models.CharField(max_length=100, verbose_name='Название', unique=True, )
    slug = models.SlugField(max_length=100, blank=False, null=False, unique=True, db_index=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', default=None, blank=True, null=True, verbose_name='Фото')
    description = models.TextField(verbose_name='Описание алкоголя', blank=True, null=True)
    data_purchase = models.DateField(verbose_name='Дата покупки', blank=True, null=True)
    date_reg = models.DateTimeField(verbose_name='Дата регистрации', auto_now=True)
    alcohol_retention = models.IntegerField(verbose_name='Выдержка', blank=True, null=True)
    volume = models.IntegerField(verbose_name='Объем')
    strength = models.IntegerField(verbose_name='Крепость')
    country = models.CharField(max_length=255, verbose_name='Место производства', blank=True, null=True)
    manufacturer = models.CharField(max_length=50, verbose_name='Завод изготовитель', blank=True, null=True)
    price = models.IntegerField(verbose_name='Цена миньёна')
    is_active = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), StatusPhoto.choices)),
                                verbose_name='Ствтус', default=StatusPhoto.NO)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='minions')
    tags = models.ManyToManyField('TagMinion', blank=True, related_name='tags')
    bigminion = models.OneToOneField('BigMinion', on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='minon')

    objects = models.Manager()
    manager = PhotoNoneManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Миньен'
        verbose_name_plural = 'Миньены'
        ordering = ['-date_reg']
        indexes = [
            models.Index(fields=['-date_reg'])
        ]

    def get_absolute_url(self):
        return reverse('minion', kwargs={'minion_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

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
    char = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.name


class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')