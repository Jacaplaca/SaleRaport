# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-18 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20170516_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='approved',
            field=models.CharField(choices=[('1', 'Awaiting'), ('2', 'No'), ('3', 'Yes')], default=1, max_length=1),
        ),
    ]
