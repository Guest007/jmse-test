# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jmse', '0002_auto_20150902_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='area',
            field=models.CharField(max_length=100, null=True, verbose_name='Area', blank=True),
        ),
        migrations.AlterField(
            model_name='estate',
            name='status',
            field=models.CharField(max_length=50, null=True, verbose_name='Status', blank=True),
        ),
        migrations.AlterField(
            model_name='estate',
            name='title',
            field=models.CharField(max_length=500, null=True, verbose_name='ProjectName', blank=True),
        ),
    ]
