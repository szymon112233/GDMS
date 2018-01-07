# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from random import *

class tableNames(models.Model):
	stringName = models.CharField(max_length=32, primary_key=True, unique=True)
	dbName = models.CharField(max_length=32, unique=True)

class skill(models.Model):
	name = models.CharField(max_length=32, unique=True)
	desc = models.CharField(max_length=256)
	req_lvl = models.IntegerField(default=0)
	damage = models.FloatField(default=0)
	is_targeted = models.BooleanField(default=False)
	is_aoe = models.BooleanField(default=False)
	is_passive = models.BooleanField(default=False)

	def __str__(self):
		return self.name


class item(models.Model):
	name = models.CharField(max_length=64, unique=True)
	desc = models.CharField(max_length=256)
	type = models.CharField(max_length=64)
	damage = models.FloatField(default=0)
	# more data here?

	def __str__(self):
		return self.name

class users_data(models.Model):
	login = models.CharField(max_length=16, primary_key=True, unique=True)
	password = models.CharField(max_length=32)

	def __str__(self):
		return self.login

class player(models.Model):
	user = models.OneToOneField(users_data, on_delete=models.CASCADE)
	# more data here??

	def __str__(self):
		return self.user.__str__()

class character(models.Model):
	name = models.CharField(max_length=64, unique=True)
	owner = models.ForeignKey(player, on_delete=models.CASCADE)
	skills = models.ManyToManyField(skill, through='skillbook', through_fields=('skill_owner', 'skill_base'))
	items = models.ManyToManyField(item, through='inventory', through_fields=('item_owner', 'item_base'))
	# more data here?

	def __str__(self):
		return self.name

class npc(models.Model):
	name = models.CharField(max_length=64)
	spriteID = models.IntegerField(default=0)
	skills = models.ManyToManyField(skill)

	def __str__(self):
		return self.name

class enemy(models.Model):
	name = models.CharField(max_length=64)
	modelID = models.IntegerField(default=0)
	damage = models.FloatField(default=0)
	speed = models.FloatField(default=1)
	health = models.FloatField(default=1)
	vision_range = models.FloatField(default=10)
	chase_range = models.FloatField(default=10)

	def __str__(self):
		return self.name


class skillbook(models.Model):
	skill_base = models.ForeignKey(skill, on_delete=models.CASCADE)
	skill_owner = models.ForeignKey(character, on_delete=models.CASCADE)
	#local skill modifications here?

	def __str__(self):
		return self.skill_owner

class inventory(models.Model):
	item_base = models.ForeignKey(item, on_delete=models.CASCADE)
	item_owner = models.ForeignKey(character, on_delete=models.CASCADE)
	# local item modifications here?

	def __str__(self):
		return self.item_owner


class configs(models.Model):
	database_ver = models.FloatField()
	game_ver = models.FloatField(default=0.1)
	exp_mult = models.FloatField(default=1)

class logs(models.Model):
	date = models.DateTimeField()
	message = models.CharField(max_length=1024)

class locale(models.Model):
	default_transl = models.CharField(max_length=256)
	en_transl = models.CharField(max_length=256)
	pl_transl = models.CharField(max_length=256)

	def __str__(self):
		return self.default_transl
