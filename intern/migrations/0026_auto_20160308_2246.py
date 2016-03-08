# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0025_house_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='haeuser', verbose_name='1. Bild'),
        ),
        migrations.AlterField(
            model_name='house',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='haeuser', verbose_name='2. Bild'),
        ),
        migrations.AlterField(
            model_name='house',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='haeuser', verbose_name='3. Bild'),
        ),
        migrations.AlterField(
            model_name='house',
            name='name',
            field=models.CharField(max_length=4096, verbose_name='* Name des Heimes/Hauses'),
        ),
    ]
