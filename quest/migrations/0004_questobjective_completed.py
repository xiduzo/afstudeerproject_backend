# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-31 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0003_remove_questobjective_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='questobjective',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
