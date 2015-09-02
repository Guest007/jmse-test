# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import jmse.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pageid', models.IntegerField(verbose_name='PageId')),
                ('title', models.CharField(max_length=500, verbose_name='ProjectName')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
                ('area', models.CharField(max_length=100, verbose_name='Area')),
                ('url', models.URLField(verbose_name='URL')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=jmse.models.get_file_name, verbose_name='Image')),
                ('is_publish', models.BooleanField(default=True, verbose_name='IsPublish')),
            ],
        ),
    ]
