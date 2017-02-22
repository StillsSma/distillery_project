# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_remove_stray_bottle_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bottle_size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_number',
        ),
        migrations.AddField(
            model_name='product',
            name='UPC',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
