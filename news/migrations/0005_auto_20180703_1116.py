# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20180702_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '发布新闻', 'verbose_name_plural': '发布新闻'},
        ),
        migrations.AlterModelOptions(
            name='column',
            options={'verbose_name': '添加栏目', 'verbose_name_plural': '添加栏目', 'ordering': ['name']},
        ),
    ]
