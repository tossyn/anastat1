# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-21 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20170221_0938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='manager',
            new_name='is_manager',
        ),
    ]
