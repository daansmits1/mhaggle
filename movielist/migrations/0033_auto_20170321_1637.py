# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0032_auto_20170321_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seenlist',
            name='movie',
        ),
        migrations.AddField(
            model_name='seenlist',
            name='movie',
            field=models.ManyToManyField(to='movielist.Movie'),
        ),
    ]
