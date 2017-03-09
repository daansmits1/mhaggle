# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0017_auto_20170309_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='movie',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='movie',
            field=models.ForeignKey(default='Movie', on_delete=django.db.models.deletion.CASCADE, to='movielist.Movie'),
            preserve_default=False,
        ),
    ]
