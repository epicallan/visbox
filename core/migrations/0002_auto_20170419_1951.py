# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-19 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='data',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataset',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]