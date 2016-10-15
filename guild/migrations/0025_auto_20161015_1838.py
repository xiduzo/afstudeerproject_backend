# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-15 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guild', '0024_remove_guild_accepted_rules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guildruleendorsment',
            name='rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endorsements', to='guild.GuildRule'),
        ),
        migrations.AlterField(
            model_name='guildruleendorsment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GuildRuleEndorsment_user', to='user.User'),
        ),
    ]
