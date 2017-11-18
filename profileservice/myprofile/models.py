# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User)
    job = models.CharField(u"Profissão", max_length=100)
    city = models.CharField("Cidade", max_length=100)

    def __str__(self):
        return self.job


class Heart(models.Model):
    profile_to = models.ForeignKey(Profile, related_name='heart_to')
    profile_from = models.ForeignKey(Profile, related_name='heart_from')


class Rate(models.Model):
    profile_to = models.ForeignKey(Profile, related_name='rate_to')
    profile_from = models.ForeignKey(Profile, related_name='rate_from')
    rate = models.IntegerField()


class Message(models.Model):
    profile_to = models.ForeignKey(Profile, related_name='message_to')
    profile_from = models.ForeignKey(Profile, related_name='message_from')
    message = models.TextField()

