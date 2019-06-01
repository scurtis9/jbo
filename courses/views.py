from django.shortcuts import render, get_object_or_404, reverse
from django.forms import modelformset_factory
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

from .models import Course, Hole, TeeBox


class CourseListView(ListView):
    model = Course
    template_name = 'courses/courses.html'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'


class CourseCreateView(CreateView):
    model = Course
    fields = ['name']



