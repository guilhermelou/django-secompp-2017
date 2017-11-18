# -*- coding: utf-8 -*-

from django.conf.urls import url
from myprofile import views as myprofile_views
#from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    url(r'^$', myprofile_views.ListProfileView.as_view(), name='profile_list'),

    url(r'^create/$', myprofile_views.CreateProfileView.as_view(),
        name='profile_create'),

    url(r'^(?P<pk>\d+)/$', myprofile_views.DetailProfileView.as_view(),
        name='profile_detail'),

    url(r'^(?P<pk>\d+)/update/$', myprofile_views.UpdateProfileView.as_view(),
        name='profile_update'),

    url(r'^(?P<pk>\d+)/delete/$', myprofile_views.DeleteProfileView.as_view(),
        name='profile_delete'),
]


