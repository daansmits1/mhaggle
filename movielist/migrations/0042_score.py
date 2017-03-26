# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 17:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movielist', '0041_auto_20170326_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('score', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movielist.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]