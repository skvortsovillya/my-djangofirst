# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 14:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='ext',
        ),
    ]
