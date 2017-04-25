# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-25 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_visualisation_unit_divisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='visualisation',
            name='exterior_arc_percent',
            field=models.IntegerField(default=90),
        ),
        migrations.AddField(
            model_name='visualisation',
            name='interior_arc_percent',
            field=models.IntegerField(default=20),
        ),
    ]
