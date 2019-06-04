from django.urls import path, include

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.EventListView.as_view(), name='event-list'),
    path('<slug:slug>', views.EventDetailView.as_view(), name='event-detail'),
]