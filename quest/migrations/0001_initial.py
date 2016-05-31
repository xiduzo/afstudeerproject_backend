# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('world', '0002_userinworld'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('experience', models.PositiveIntegerField()),
                ('interaction_design', models.PositiveIntegerField()),
                ('visual_interface_design', models.PositiveIntegerField()),
                ('frontend_development', models.PositiveIntegerField()),
                ('content_management', models.PositiveIntegerField()),
                ('project_management', models.PositiveIntegerField()),
                ('active', models.BooleanField(default=True)),
                ('world', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='world', to='world.World')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
