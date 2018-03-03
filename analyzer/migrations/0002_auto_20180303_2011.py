# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-03 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='codictb',
            name='codic_registered_time',
            field=models.DateTimeField(db_column='CODIC_REGISTERED_TIME', default=django.utils.timezone.localtime),
        ),
        migrations.AddField(
            model_name='conmtb',
            name='conm_registered_time',
            field=models.DateTimeField(db_column='CONM_REGISTERED_TIME', default=django.utils.timezone.localtime),
        ),
        migrations.AddField(
            model_name='mtsctb',
            name='mtsc_registered_time',
            field=models.DateTimeField(db_column='MTSC_REGISTERED_TIME', default=django.utils.timezone.localtime),
        ),
        migrations.AddField(
            model_name='pdtb',
            name='pd_registered_time',
            field=models.DateTimeField(db_column='PD_REGISTERED_TIME', default=django.utils.timezone.localtime),
        ),
    ]