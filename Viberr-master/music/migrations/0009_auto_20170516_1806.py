# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_album_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_logo',
        ),
        migrations.AddField(
            model_name='album',
            name='termin',
            field=models.DateField(null=True),
        ),
    ]
