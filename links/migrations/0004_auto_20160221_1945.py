# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 18:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_link_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='intern.State'),
        ),
    ]
