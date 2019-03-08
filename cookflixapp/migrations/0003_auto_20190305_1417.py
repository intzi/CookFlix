# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-05 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookflixapp', '0002_auto_20190304_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=2),
        ),
    ]