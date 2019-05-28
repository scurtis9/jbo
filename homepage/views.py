from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'homepage/home.html'
