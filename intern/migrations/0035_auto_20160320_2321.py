# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0034_auto_20160313_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='end',
            field=models.DateField(blank=True, null=True, verbose_name='Ende'),
        ),
        migrations.AlterField(
            model_name='date',
            name='start',
            field=models.DateField(blank=True, null=True, verbose_name='Beginn'),
        ),
    ]
