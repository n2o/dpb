# Generated by Django 2.2.17 on 2021-03-08 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adressverzeichnis', '0002_auto_20210308_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='manuelleberechtigung',
            name='hat_stimmrecht',
            field=models.BooleanField(default=False, verbose_name='Hat Stimmrecht?'),
        ),
    ]
