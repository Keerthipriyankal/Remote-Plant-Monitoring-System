# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensorvalues', '0011_auto_20171102_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant_1',
            name='ph_value',
            field=models.CharField(default=100, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plant_2',
            name='ph_value',
            field=models.CharField(default=100, max_length=250),
            preserve_default=False,
        ),
    ]