# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2021-10-10 04:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='comment',
        ),
    ]
