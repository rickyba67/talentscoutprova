# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 08:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thetalentscout', '0003_giudizio'),
    ]

    operations = [
        migrations.AddField(
            model_name='giocatoregara',
            name='giudizio',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='thetalentscout.Giudizio'),
        ),
    ]