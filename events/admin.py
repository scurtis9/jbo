from django.contrib import admin
from .models import Event, Participant, PlayerCard


class PlayerCardInline(admin.TabularInline):
    model = PlayerCard


class ParticipantInLine(admin.TabularInline):
    model = Participant


class EventAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [
        ParticipantInLine,
        PlayerCardInline
    ]



admin.site.register(Event, EventAdmin)