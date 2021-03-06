# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2021-10-10 03:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20211009_0652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('question', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='basic_app.Doctor')),
            ],
        ),
    ]
