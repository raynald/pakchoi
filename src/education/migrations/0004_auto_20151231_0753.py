# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 07:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_auto_20151230_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='grades',
            field=models.ManyToManyField(to='education.Grade'),
        ),
        migrations.AddField(
            model_name='order',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.Student'),
        ),
        migrations.AddField(
            model_name='order',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.Teacher'),
        ),
    ]
