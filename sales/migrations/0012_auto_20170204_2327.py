# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-04 22:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0011_auto_20170204_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrequest',
            old_name='level_of_agregation',
            new_name='level_of_aggregation',
        ),
    ]
