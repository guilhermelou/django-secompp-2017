# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Profile(models.Model):
    job = models.CharField(u"Profissão", max_length=100)
    city = models.CharField("Cidade", max_length=100)


