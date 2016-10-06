# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-06 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guild', '0015_auto_20160927_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='guildhistoryupdate',
            name='action_type',
            field=models.CharField(choices=[(1, b'added task'), (2, b'removed task'), (3, b'assigned'), (4, b'remove assigned'), (5, b'completed'), (6, b'remove completed'), (7, b'graded'), (8, b'regraded')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='guildquest',
            name='grade',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]