# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 20:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movielist', '0035_auto_20170323_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='user_name',
        ),
        migrations.AddField(
            model_name='rating',
            name='movies',
            field=models.ManyToManyField(to='movielist.Movie'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='movies',
            field=models.ManyToManyField(to='movielist.Movie'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
    ]