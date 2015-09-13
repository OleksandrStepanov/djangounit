# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default=datetime.datetime(2015, 9, 10, 9, 46, 50, 718779, tzinfo=utc), max_length=256, verbose_name='\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=256, verbose_name="\u0406\u043c'\u044f"),
            preserve_default=True,
        ),
    ]
