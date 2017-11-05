# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField()),
                ('date_lastlogin', models.DateTimeField()),
            ],
        ),
    ]
