# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 20:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0018_auto_20170309_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='movie',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
