from django.contrib import admin
from .models import Event, Participant


class EventAdmin(admin.ModelAdmin):
    pass


class ParticipantAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Participant, ParticipantAdmin)