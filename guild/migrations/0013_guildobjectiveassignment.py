# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-09 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20160908_1313'),
        ('guild', '0012_guildquest_completed_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildObjectiveAssignment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='guild.GuildObjective')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_objectives', to='user.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
