# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20160531_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.PositiveIntegerField(choices=[(0, 'male'), (1, 'female')]),
        ),
    ]
