# Generated by Django 5.1.4 on 2025-01-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottle', '0004_alter_minion_country_alter_minion_data_purchase_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minion',
            name='photo',
            field=models.BooleanField(default=False, verbose_name='Фото'),
        ),
    ]
