# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-10 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tealdb', '0034_site_lightings_not_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='action_required',
            field=models.BooleanField(default=False),
        ),
    ]
