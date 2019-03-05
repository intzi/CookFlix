# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-05 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookflixapp', '0003_auto_20190305_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='video_path',
            field=models.FileField(max_length=300, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
    ]
