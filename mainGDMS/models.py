# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class GameUser(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField()
    date_lastlogin = models.DateTimeField()

    def __str__(self):
        return self.login