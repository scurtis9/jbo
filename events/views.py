from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import (
    View,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Event, Participant


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    ordering = ['-start_date']


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'

    def get_object(self):
        obj = super().get_object()
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['participants'] = Participant.objects.filter(event=self.object)
        return context
