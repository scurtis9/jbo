from django.http import Http404
from django.shortcuts import render, get_object_or_404, reverse
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
# Create your views here.


class ProfileDetail(DetailView):
    template_name = 'users/profile.html'
    model = JboUser


class ProfileView(TemplateView):
    template_name = 'users/profile_view.html'
    http_method_names = {'get'}

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')

        if slug:
            user = get_object_or_404(JboUser, slug=slug)
        elif self.request.user.is_authenticated():
            user = self.request.user
        else:
            raise Http404  # Case where user gets to this view anonymously for non-existent user

        sp_form = JboUserViewForm(instance=user.profile)

        return {'sp_form': sp_form, 'user': user}