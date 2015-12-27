# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0013_auto_20151227_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='verify_picture',
            field=models.ImageField(blank=True, null=True, upload_to='teacher_vers/%Y-%m-%d/', verbose_name='\u5b66\u751f\u8bc1\u9a8c\u8bc1\uff08\u5b66\u751f\u8bc1\u7167\u7247+\u624b\u5199\u8fb9\u9645\u6559\u80b2\uff09'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='gender',
            field=models.CharField(choices=[('M', '\u7537'), ('F', '\u5973')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='teacher_pics/%Y-%m-%d/', verbose_name='\u4e0a\u4f20\u5934\u50cf\uff08\u8bf7\u4f7f\u7528\u771f\u5b9e\u7167\u7247\uff09'),
        ),
    ]
