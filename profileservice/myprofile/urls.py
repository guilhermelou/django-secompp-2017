# -*- coding: utf-8 -*-

from django.conf.urls import url
from myprofile.views import ListProfileView
#from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    url(r'^$', ListProfileView.as_view(), name='profile_list')
]


