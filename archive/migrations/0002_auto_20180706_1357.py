# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 11:57
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('archive', '0001_squashed_0016_auto_20180604_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='years',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Erstellt am'),
        ),
        migrations.AlterField(
            model_name='item',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Zuletzt geändert'),
        ),
        migrations.AlterField(
            model_name='item',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Hinzugefügt am'),
        ),
        migrations.AlterField(
            model_name='year',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Erstellt am'),
        ),
    ]