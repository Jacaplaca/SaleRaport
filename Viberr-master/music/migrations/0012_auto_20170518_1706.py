# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-18 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20170518_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_title',
        ),
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='album',
            name='genre',
        ),
        migrations.AddField(
            model_name='album',
            name='aktywnosc',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24')], max_length=2),
        ),
        migrations.AddField(
            model_name='album',
            name='kodpocztowy',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AddField(
            model_name='album',
            name='miejscowosc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='album',
            name='uwagi',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='album',
            name='zakonczono',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='album',
            name='godzinakoniec',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24')], max_length=2),
        ),
        migrations.AlterField(
            model_name='album',
            name='godzinastart',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24')], max_length=2),
        ),
    ]
