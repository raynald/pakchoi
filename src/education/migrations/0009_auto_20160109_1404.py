# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0008_article_articlecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='watch',
            field=models.IntegerField(default=0),
        ),
    ]
