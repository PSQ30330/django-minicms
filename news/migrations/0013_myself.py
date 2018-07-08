# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20180708_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myself',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(verbose_name='用户名', max_length=100)),
                ('start', models.CharField(verbose_name='收藏', max_length=100)),
            ],
            options={
                'verbose_name_plural': '收藏',
            },
        ),
    ]
