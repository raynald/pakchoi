# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0017_auto_20151228_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='pinyin',
            field=models.CharField(default='Beijing', max_length=50),
            preserve_default=False,
        ),
    ]
