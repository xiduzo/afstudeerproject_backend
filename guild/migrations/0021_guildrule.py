# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-14 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('guild', '0020_guild_accepted_rules'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildRule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('rule', models.TextField()),
                ('importance', models.IntegerField()),
                ('rule_type', models.CharField(choices=[(1, b'houding'), (2, b'functioneren binnen het team'), (3, b'kennisontwikkeling'), (4, b'verantwoording')], max_length=2)),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rules', to='guild.Guild')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]