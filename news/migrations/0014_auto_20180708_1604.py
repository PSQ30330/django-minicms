# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_myself'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Myself',
            new_name='Start',
        ),
    ]
