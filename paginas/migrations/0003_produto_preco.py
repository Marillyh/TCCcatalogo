# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-11-02 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0002_auto_20211101_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=20),
        ),
    ]
