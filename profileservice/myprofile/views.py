# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from myprofile.models import Profile
from django.views.generic import View, CreateView, ListView, DetailView,UpdateView, DeleteView
from myprofile.forms import ProfileForm
from django.urls import reverse_lazy
# Create your views here.

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

