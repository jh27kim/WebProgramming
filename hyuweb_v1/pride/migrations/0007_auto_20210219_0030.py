# Generated by Django 3.1.6 on 2021-02-18 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pride', '0006_auto_20210219_0023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_date',
            new_name='create_date',
        ),
    ]