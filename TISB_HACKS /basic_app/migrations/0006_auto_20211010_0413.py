# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2021-10-10 04:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_remove_reply_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='name',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]