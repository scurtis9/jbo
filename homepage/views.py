from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from blog.models import Post


class HomeView(generic.TemplateView):
    template_name = 'homepage/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recent_posts = Post.objects.order_by('-date_posted')[:3]
        context['recent_posts'] = recent_posts
        return context

