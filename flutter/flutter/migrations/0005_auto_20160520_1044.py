# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flutter', '0004_auto_20160519_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flutt',
            name='text',
            field=models.CharField(default='start typing', max_length=140),
        ),
        migrations.AlterField(
            model_name='flutt',
            name='user',
            field=models.CharField(default='elfough', max_length=25),
        ),
    ]