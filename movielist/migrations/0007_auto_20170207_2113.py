# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0006_auto_20170207_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]
