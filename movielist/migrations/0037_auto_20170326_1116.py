# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 15:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0036_auto_20170323_1635'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Seenlist',
            new_name='Toseelist',
        ),
        migrations.RenameField(
            model_name='toseelist',
            old_name='seenlist',
            new_name='toseelist',
        ),
    ]
