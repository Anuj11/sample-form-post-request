# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='submit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
