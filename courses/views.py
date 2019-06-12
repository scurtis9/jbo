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
    template_name = 'courses/course_list.html'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'


class CourseCreateView(CreateView):
    model = Course
    fields = ['name']


def manage_course(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    TeeBoxInlineFormSet = inlineformset_factory(
        Course,
        TeeBox,
        fields=('color', 'rating', 'slope'),
        exclude=('course',),
        max_num=4
    )
    HoleInlineFormSet = inlineformset_factory(
        Course,
        Hole,
        fields=('number', 'par', 'handicap'),
        exclude=('course',),
        max_num=18
    )
    if request.method == "POST":
        teebox_formset = TeeBoxInlineFormSet(request.POST, request.FILES, instance=course, prefix='teeboxes')
        hole_formset = HoleInlineFormSet(request.POST, request.FILES, instance=course, prefix='holes')
        if teebox_formset.is_valid() and hole_formset.is_valid():
            teebox_formset.save()
            hole_formset.save()
            return HttpResponseRedirect(course.get_absolute_url())
    else:
        teebox_formset = TeeBoxInlineFormSet(instance=course, prefix='teeboxes')
        hole_formset = HoleInlineFormSet(instance=course, prefix='holes')
    return render(request, 'courses/course_manage.html', {'teebox_formset': teebox_formset, 'hole_formset': hole_formset, 'course': course})


