# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-05-11 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tealdb', '0035_site_action_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='twitter',
            field=models.CharField(default='', max_length=64),
        ),
    ]