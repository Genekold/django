# Generated by Django 5.1.4 on 2025-01-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottle', '0017_alter_minion_date_reg'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='minion',
            options={'ordering': ['-date_reg']},
        ),
        migrations.RemoveIndex(
            model_name='minion',
            name='bottle_mini_data_pu_dd3f37_idx',
        ),
        migrations.AddIndex(
            model_name='minion',
            index=models.Index(fields=['-date_reg'], name='bottle_mini_date_re_e41a8f_idx'),
        ),
    ]
