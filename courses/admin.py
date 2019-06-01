from django.contrib import admin

from .models import Course, TeeBox, Hole


class HoleInline(admin.TabularInline):
    model = Hole
    extra = 18
    max_num = 18


class TeeBoxInline(admin.TabularInline):
    model = TeeBox
    extra = 4
    max_num = 4


class CourseAdmin(admin.ModelAdmin):
    inlines = [TeeBoxInline, HoleInline]


admin.site.register(Course, CourseAdmin)