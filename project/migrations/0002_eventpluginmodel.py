# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-05 07:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='project_eventpluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('limit', models.IntegerField(null=True)),
                ('show_more', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project.Category')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
