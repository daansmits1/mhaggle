# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0042_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
