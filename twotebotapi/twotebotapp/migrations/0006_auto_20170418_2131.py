# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twotebotapp', '0005_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='creator',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
