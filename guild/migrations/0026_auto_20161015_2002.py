# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-15 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20160922_1707'),
        ('guild', '0025_auto_20161015_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='guildruleendorsment',
            name='endorsed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='endorser', to='user.User'),
        ),
        migrations.AlterField(
            model_name='guildruleendorsment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endorsed', to='user.User'),
        ),
    ]
