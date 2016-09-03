# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-02 00:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20160603_1329'),
        ('guild', '0010_auto_20160831_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildHistoryUpdate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('action', models.TextField()),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_updates', to='guild.Guild')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='user.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
