# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 04:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_photoalbom_abpho_see'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoalbom',
            name='abpho_see',
        ),
    ]
