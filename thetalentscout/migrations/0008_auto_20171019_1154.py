# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thetalentscout', '0007_auto_20171019_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giocatore',
            name='foto',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
