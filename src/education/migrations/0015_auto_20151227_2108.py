# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 21:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0014_auto_20151227_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.District'),
        ),
    ]
