# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 21:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0020_wishlist'),
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
