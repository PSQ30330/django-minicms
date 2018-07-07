# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20180707_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newscomment',
            name='article',
            field=models.CharField(max_length=50),
        ),
    ]
