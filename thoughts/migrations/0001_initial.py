# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-27 09:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thoughts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorder_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('conditions', models.IntegerField(choices=[(0, 'Ecstatic'), (5, 'Passionate'), (10, 'Happy'), (15, 'Optimistic'), (20, 'Content'), (25, 'Bored'), (26, 'Tired'), (27, 'Hungry'), (30, 'Pessimistic'), (35, 'Frustrated'), (40, 'Overwhelmed'), (45, 'Disappointed'), (50, 'Worried'), (55, 'Angry'), (60, 'Jealous'), (65, 'Insecure'), (70, 'Guilty'), (75, 'Fear'), (80, 'Grief'), (85, 'Despair')])),
                ('notes', models.TextField(blank=True, default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thoughts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]