# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-05 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_guestbookentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestbookentry',
            name='job',
            field=models.CharField(default='type here', max_length=255),
            preserve_default=False,
        ),
    ]
