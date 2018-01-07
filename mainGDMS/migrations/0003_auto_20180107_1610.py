# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-07 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainGDMS', '0002_tablenames'),
    ]

    operations = [
        migrations.CreateModel(
            name='enemy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('modelID', models.IntegerField(default=0)),
                ('damage', models.FloatField(default=0)),
                ('speed', models.FloatField(default=1)),
                ('health', models.FloatField(default=1)),
                ('vision_range', models.FloatField(default=10)),
                ('chase_range', models.FloatField(default=10)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='damage',
            field=models.FloatField(default=0),
        ),
    ]
