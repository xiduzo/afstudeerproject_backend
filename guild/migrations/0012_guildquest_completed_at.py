# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-02 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guild', '0011_guildhistoryupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='guildquest',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
