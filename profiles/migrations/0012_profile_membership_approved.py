# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-26 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20170221_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='membership_approved',
            field=models.NullBooleanField(),
        ),
    ]
