# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jmse', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estate',
            options={'verbose_name': 'Estate Object', 'verbose_name_plural': 'Estate Objects'},
        ),
    ]
