# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-25 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170425_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='visualisation',
            name='label_significant_digits',
            field=models.IntegerField(default=1),
        ),
    ]
