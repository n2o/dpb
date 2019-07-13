# Generated by Django 2.2.1 on 2019-05-25 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('links', '0005_auto_20160221_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='links.LinkCategory'),
        ),
        migrations.AlterField(
            model_name='link',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='intern.State'),
        ),
    ]