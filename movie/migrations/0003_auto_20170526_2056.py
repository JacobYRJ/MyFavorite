# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-26 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='protagonist',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]