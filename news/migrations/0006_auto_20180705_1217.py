# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180703_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user_type',
        ),
        migrations.DeleteModel(
            name='userinfo',
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]
