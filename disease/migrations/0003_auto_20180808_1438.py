# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-08 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0002_auto_20180803_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=200),
        ),
    ]