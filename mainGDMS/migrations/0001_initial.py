# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='configs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_mult', models.FloatField(default=1)),
                ('database_ver', models.FloatField()),
                ('game_ver', models.FloatField(default=0.1)),
            ],
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('desc', models.CharField(max_length=256)),
                ('type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='locale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_transl', models.CharField(max_length=256)),
                ('en_transl', models.CharField(max_length=256)),
                ('pl_transl', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('message', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='npc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('spriteID', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('desc', models.CharField(max_length=256)),
                ('req_lvl', models.IntegerField(default=0)),
                ('damage', models.FloatField(default=0)),
                ('is_targeted', models.BooleanField(default=False)),
                ('is_aoe', models.BooleanField(default=False)),
                ('is_passive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='skillbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainGDMS.skill')),
                ('skill_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainGDMS.character')),
            ],
        ),
        migrations.CreateModel(
            name='users_data',
            fields=[
                ('login', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainGDMS.users_data'),
        ),
        migrations.AddField(
            model_name='npc',
            name='skills',
            field=models.ManyToManyField(to='mainGDMS.skill'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='item_base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainGDMS.item'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='item_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainGDMS.character'),
        ),
        migrations.AddField(
            model_name='character',
            name='items',
            field=models.ManyToManyField(through='mainGDMS.inventory', to='mainGDMS.item'),
        ),
        migrations.AddField(
            model_name='character',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainGDMS.player'),
        ),
        migrations.AddField(
            model_name='character',
            name='skills',
            field=models.ManyToManyField(through='mainGDMS.skillbook', to='mainGDMS.skill'),
        ),
    ]