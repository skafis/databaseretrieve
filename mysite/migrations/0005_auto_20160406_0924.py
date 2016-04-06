# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-06 09:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20160406_0859'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='view',
            options={'get_latest_by': 'creation_date'},
        ),
        migrations.AddField(
            model_name='view',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 4, 6, 9, 24, 13, 181699, tzinfo=utc)),
            preserve_default=False,
        ),
    ]