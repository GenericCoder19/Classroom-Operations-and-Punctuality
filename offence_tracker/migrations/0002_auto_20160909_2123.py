# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 17:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offence_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offence',
            name='details',
        ),
        migrations.AddField(
            model_name='offence',
            name='type',
            field=models.CharField(blank=True, choices=[('RL', 'Late Reporting Time'), ('LONW', 'Learning Objective Not Written'), ('TNH', 'Teaching Not Happening'), ('CCN', 'No Class Control'), ('SMO', 'Students Moving Outside')], max_length=4),
        ),
        migrations.AlterField(
            model_name='offence',
            name='block',
            field=models.CharField(choices=[('P', 'Primary'), ('M', 'Middle'), ('S', 'Senior')], max_length=1),
        ),
        migrations.AlterField(
            model_name='offence',
            name='floor',
            field=models.CharField(choices=[('G', 'Ground'), ('F', 'First'), ('S', 'Second')], max_length=1),
        ),
        migrations.AlterField(
            model_name='offence',
            name='period',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='offence',
            name='reporter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
