# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-26 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookflixapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, height_field='picture_width', max_length=255, null=True, upload_to=None, width_field='picture_height'),
        ),
    ]