# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 02:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0007_auto_20170207_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='description',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='language',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='stars',
        ),
    ]