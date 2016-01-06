# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_auto_20151231_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='mobile',
            new_name='parent_mobile',
        ),
        migrations.AddField(
            model_name='order',
            name='teacher_mobile',
            field=models.IntegerField(default=1390000000),
        ),
        migrations.AddField(
            model_name='order',
            name='teacher_name',
            field=models.CharField(default='Jason Marz', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='parent_mobile',
            field=models.IntegerField(default=1520000000),
        ),
        migrations.AddField(
            model_name='teacher',
            name='mobile',
            field=models.IntegerField(default=1390000000),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.IntegerField(default=0, choices=[(0, '\u8ba2\u5355\u751f\u6210'), (1, '\u8001\u5e08\u5df2\u786e\u8ba4'), (2, '\u5b66\u751f\u5df2\u8bc4\u4ef7')]),
        ),
    ]
