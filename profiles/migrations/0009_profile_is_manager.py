# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-20 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20170218_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_manager',
            field=models.BooleanField(default=False, help_text='Check for affiliate managers'),
        ),
    ]
