# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensorvalues', '0003_sensorvalues_hum_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensorvalues',
            name='moisture',
            field=models.CharField(default=33, max_length=250),
            preserve_default=False,
        ),
    ]