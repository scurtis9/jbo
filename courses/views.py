from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from django.forms import inlineformset_factory, modelformset_factory
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


def manage_course(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    HoleInlineFormSet = inlineformset_factory(
        Course,
        Hole,
        fields=('number', 'par', 'handicap'),
        exclude=('course',),
        max_num=18
    )
    if request.method == "POST":
        formset = HoleInlineFormSet(request.POST, request.FILES, instance=course)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(course.get_absolute_url())
    else:
        formset = HoleInlineFormSet(instance=course)
    return render(request, 'courses/course_manage.html', {'formset': formset, 'course': course})


