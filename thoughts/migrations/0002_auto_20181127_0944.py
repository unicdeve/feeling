# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-27 09:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Thoughts',
            new_name='Thought',
        ),
    ]
