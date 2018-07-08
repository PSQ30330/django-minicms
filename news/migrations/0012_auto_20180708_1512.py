# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20180707_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(verbose_name='用户名', max_length=50)),
                ('like', models.CharField(verbose_name='点赞', max_length=50)),
                ('article', models.CharField(verbose_name='文章', max_length=50)),
            ],
            options={
                'verbose_name_plural': '点赞',
            },
        ),
        migrations.AlterModelOptions(
            name='newscomment',
            options={'verbose_name': '新闻评论', 'verbose_name_plural': '新闻评论'},
        ),
    ]
