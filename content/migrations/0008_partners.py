# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-06 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20170606_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('name', models.CharField(blank=True, default=' ', max_length=1024)),
            ],
        ),
    ]
