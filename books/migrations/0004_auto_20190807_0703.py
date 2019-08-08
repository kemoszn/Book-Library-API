# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-07 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, unique=True),
        ),
    ]
