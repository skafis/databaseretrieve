# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-06 08:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20160405_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view',
            name='message',
        ),
        migrations.RemoveField(
            model_name='view',
            name='name',
        ),
        migrations.AddField(
            model_name='view',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='view',
            name='location',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='view',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 4, 6, 8, 59, 43, 132932, tzinfo=utc), max_length=140),
            preserve_default=False,
        ),
    ]
