# Generated by Django 3.1.6 on 2021-02-18 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pride', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]