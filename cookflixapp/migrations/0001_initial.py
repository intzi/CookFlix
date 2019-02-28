# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-26 16:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipeid', models.CharField(max_length=30, unique=True)),
                ('userid', models.CharField(max_length=30)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipeid', models.CharField(max_length=30, unique=True)),
                ('video_path', models.CharField(max_length=30)),
                ('cuisine_type', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=10)),
                ('taste', models.CharField(max_length=10)),
                ('difficulty', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('userid', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=30)),
                ('recipeid', models.CharField(max_length=30, unique=True)),
                ('taste', models.CharField(max_length=10)),
                ('difficulty', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Saved_Recipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=30)),
                ('recipeid', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('picture', models.ImageField(height_field='picture_width', max_length=255, null=True, upload_to=None, width_field='picture_height')),
                ('preferred_cuisine', models.CharField(max_length=10)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]