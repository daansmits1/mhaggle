# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0013_auto_20170303_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='watchlist',
            field=models.IntegerField(choices=[(1, '1'), (0, '0')]),
        ),
    ]
