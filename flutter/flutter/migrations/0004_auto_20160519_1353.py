# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flutter', '0003_flutt_date_n_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flutt',
            name='text',
            field=models.TextField(default='start typing', max_length=140),
        ),
        migrations.AlterField(
            model_name='flutt',
            name='user',
            field=models.TextField(default='elfough'),
        ),
    ]
