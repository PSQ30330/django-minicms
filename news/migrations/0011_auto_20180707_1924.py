# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20180707_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newscomment',
            name='article',
            field=models.CharField(verbose_name='文章', max_length=50),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='username',
            field=models.CharField(verbose_name='用户名', max_length=50),
        ),
    ]
