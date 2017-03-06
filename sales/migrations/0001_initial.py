# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-21 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields
import sales.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryOfAggregation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=5, null=True)),
                ('description', models.TextField(default='description goes here')),
            ],
            options={
                'verbose_name_plural': 'categories of Aggregation',
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=5, null=True)),
                ('description', models.TextField(default='Database category description goes here')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='ConcatTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='ConcatTable Name', max_length=200)),
                ('code', models.CharField(default=sales.models.ConcatTable.concat_code, max_length=7)),
                ('concat_price', models.PositiveSmallIntegerField()),
                ('description', models.TextField(default='description goes here')),
                ('avail_from', models.PositiveSmallIntegerField(default=1990)),
                ('avail_to', models.PositiveSmallIntegerField(default=2016)),
            ],
            options={
                'verbose_name_plural': 'Concatenated Table',
            },
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=3, null=True)),
                ('description', models.TextField(default='description goes here')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Component')),
            ],
        ),
        migrations.CreateModel(
            name='Factor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f', models.CharField(max_length=15)),
                ('value', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=5, null=True)),
                ('description', models.TextField(default='description goes here')),
                ('price', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Frequencies',
            },
        ),
        migrations.CreateModel(
            name='LevelOfAggregation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=5, null=True)),
                ('description', models.TextField(default='description goes here')),
                ('category_of_aggregation', models.ManyToManyField(to='sales.CategoryOfAggregation')),
            ],
            options={
                'verbose_name_plural': 'Levels of Aggregation',
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_from', models.PositiveSmallIntegerField()),
                ('period_to', models.PositiveSmallIntegerField()),
                ('description', models.TextField(default='description goes here')),
                ('factor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sales.Factor')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=3)),
                ('description', models.TextField(default='description goes here')),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Database')),
                ('frequency', models.ManyToManyField(to='sales.Frequency')),
                ('level_of_aggregation', models.ManyToManyField(to='sales.LevelOfAggregation')),
            ],
            options={
                'verbose_name_plural': 'Tables',
            },
        ),
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='username', max_length=200)),
                ('table', models.CharField(max_length=200)),
                ('level_of_agregation', models.CharField(max_length=100)),
                ('frequency', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('concat_price', models.PositiveSmallIntegerField()),
                ('years', multiselectfield.db.fields.MultiSelectField(max_length=200)),
                ('variables', multiselectfield.db.fields.MultiSelectField(max_length=200)),
                ('categories_of_aggregation', multiselectfield.db.fields.MultiSelectField(max_length=200)),
                ('request_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_price', models.IntegerField(default=0)),
                ('purchased', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=5)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(default='description goes here')),
            ],
        ),
        migrations.AddField(
            model_name='concattable',
            name='frequency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Frequency'),
        ),
        migrations.AddField(
            model_name='concattable',
            name='level_of_aggregation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.LevelOfAggregation'),
        ),
        migrations.AddField(
            model_name='concattable',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Table'),
        ),
        migrations.AddField(
            model_name='concattable',
            name='variable',
            field=models.ManyToManyField(to='sales.Variable'),
        ),
    ]
