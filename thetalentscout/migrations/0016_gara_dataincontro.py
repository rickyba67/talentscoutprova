# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('thetalentscout', '0015_auto_20171024_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='gara',
            name='dataincontro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
