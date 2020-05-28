# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import (CreateView, ListView, DetailView,
                                  UpdateView, DeleteView)
from django.urls import reverse_lazy

from myprofile.forms import ProfileForm
from myprofile.models import Profile


class ListProfileView(ListView):
    model = Profile


class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('myprofile:profile_list')


class DetailProfileView(DetailView):
    model = Profile


class UpdateProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('myprofile:profile_list')


class DeleteProfileView(DeleteView):
    model = Profile
    success_url = reverse_lazy('myprofile:profile_list')
