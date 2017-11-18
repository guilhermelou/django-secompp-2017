# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from myprofile.models import Profile
from django.views.generic import View, CreateView, ListView, DetailView,UpdateView, DeleteView

# Create your views here.

class ListProfileView(ListView):
    model = Profile


class CreateProfileView(CreateView):
    model = Profile


class DetailProfileView(DetailView):
    model = Profile


class UpdateProfileView(UpdateView):
    model = Profile


class DeleteProfileView(DeleteView):
    model = Profile

