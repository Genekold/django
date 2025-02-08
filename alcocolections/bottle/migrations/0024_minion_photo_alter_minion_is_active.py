# Generated by Django 5.1.4 on 2025-02-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottle', '0023_alter_minion_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='minion',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='minion',
            name='is_active',
            field=models.BooleanField(choices=[(False, 'Не активный'), (True, 'Активный')], default=0, verbose_name='Ствтус'),
        ),
    ]
