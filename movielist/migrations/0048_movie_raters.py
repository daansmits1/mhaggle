# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 13:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movielist', '0047_auto_20170328_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='raters',
            field=models.ManyToManyField(through='movielist.Score', to=settings.AUTH_USER_MODEL),
        ),
    ]
