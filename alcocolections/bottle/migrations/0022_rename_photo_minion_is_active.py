# Generated by Django 5.1.4 on 2025-02-06 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bottle', '0021_uploadfiles_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='minion',
            old_name='photo',
            new_name='is_active',
        ),
    ]
