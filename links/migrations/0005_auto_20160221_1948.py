# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0004_auto_20160221_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='intern.State'),
        ),
    ]
