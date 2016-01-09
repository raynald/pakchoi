# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0009_auto_20160109_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='create_by',
        ),
        migrations.RemoveField(
            model_name='articlecomment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='articlecomment',
            name='create_by',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='ArticleComment',
        ),
    ]
