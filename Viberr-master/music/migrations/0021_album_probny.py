# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-02 08:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0020_auto_20170524_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='probny',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]