# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_auto_20151224_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='school',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]