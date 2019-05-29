from django.shortcuts import render
from django.views import generic
from .models import JboUser, Profile
# Create your views here.


class ProfileDetail(generic.DetailView):
    template_name = 'users/profile.html'
    model = JboUser
