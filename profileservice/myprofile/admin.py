# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myprofile.models import *

# Register your models here.

admin.site.register(Heart)
admin.site.register(Rate)
admin.site.register(Message)
admin.site.register(Profile)

