# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-29 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
    ]