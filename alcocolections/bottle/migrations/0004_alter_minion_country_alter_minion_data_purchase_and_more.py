# Generated by Django 5.1.4 on 2025-01-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottle', '0003_alter_minion_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minion',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Место производства'),
        ),
        migrations.AlterField(
            model_name='minion',
            name='data_purchase',
            field=models.DateField(blank=True, null=True, verbose_name='Дата покупки'),
        ),
        migrations.AlterField(
            model_name='minion',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Завод изготовитель'),
        ),
    ]
