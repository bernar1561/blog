# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-27 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albome', '0002_auto_20170527_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='название'),
        ),
    ]
