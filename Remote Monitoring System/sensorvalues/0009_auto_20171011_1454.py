# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensorvalues', '0008_sensorvalues_rain_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensorvalues',
            name='day_value',
            field=models.CharField(default=100, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensorvalues',
            name='hour_value',
            field=models.CharField(default=100, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensorvalues',
            name='minute_value',
            field=models.CharField(default=100, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensorvalues',
            name='month_value',
            field=models.CharField(default=100, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensorvalues',
            name='year_value',
            field=models.CharField(default=100, max_length=250),
            preserve_default=False,
        ),
    ]
