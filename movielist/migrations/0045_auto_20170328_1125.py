# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0044_auto_20170326_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]
