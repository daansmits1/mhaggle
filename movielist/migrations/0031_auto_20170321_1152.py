# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 15:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movielist', '0030_auto_20170321_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seenlist',
            name='user_name',
        ),
        migrations.AddField(
            model_name='seenlist',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]