# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-17 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0004_headache_stomach'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer1',
            field=models.CharField(default=b'yes', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='answer2',
            field=models.CharField(default=b'no', max_length=200),
        ),
    ]