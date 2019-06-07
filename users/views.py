from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import (
    View,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import JboUserViewForm
from .models import JboUser, Profile
from events.models import Event
# Create your views here.


class ProfileDetailView(DetailView):
    template_name = 'users/profile.html'
    model = JboUser


class ProfileListView(ListView):
    template_name = 'users/profile_list.html'
    model = Profile
    context_object_name = 'profiles'


class SocialProfileView(TemplateView):
    template_name = 'users/profile_detail.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_users = JboUser.objects.all()
        user = all_users.get(slug=self.kwargs.get('slug'))
        context['user'] = user
        context['events'] = Event.objects.filter(participant__user=user)
        return context
