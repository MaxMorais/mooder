# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 19:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0015_auto_20161013_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='buyers',
            field=models.ManyToManyField(blank=True, related_name='user_buy_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
