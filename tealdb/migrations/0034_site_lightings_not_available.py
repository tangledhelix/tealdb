# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-06 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tealdb', '0033_site_accepted_this_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='lightings_not_available',
            field=models.BooleanField(default=False),
        ),
    ]
