# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import thetalentscout.models


class Migration(migrations.Migration):

    dependencies = [
        ('thetalentscout', '0014_auto_20171023_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giocatore',
            name='foto',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=thetalentscout.models.user_directory_path),
        ),
    ]
