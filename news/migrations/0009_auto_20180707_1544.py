# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_newscomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newscomment',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
