# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-26 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('affiliates', '0002_auto_20170224_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='expiry_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='expiry_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
