# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-25 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20170525_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='singer',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='song',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
