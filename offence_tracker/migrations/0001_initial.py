# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-05 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='offence',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('block', models.CharField(max_length=10)),
                ('floor', models.IntegerField()),
                ('period', models.IntegerField()),
                ('details', models.CharField(max_length=200)),
                ('reporter', models.CharField(max_length=50)),
            ],
        ),
    ]
