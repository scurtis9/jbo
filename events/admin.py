from django.contrib import admin
from .models import Event, Participant


class ParticipantInLine(admin.TabularInline):
    model = Participant


class EventAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [
        ParticipantInLine,
    ]


admin.site.register(Event, EventAdmin)