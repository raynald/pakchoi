# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0011_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='grades',
            field=models.ManyToManyField(to='education.Grade'),
        ),
    ]
