# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-22 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20190620_0802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='updated',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='updated',
            new_name='updated_at',
        ),
    ]
