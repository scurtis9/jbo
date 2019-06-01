from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('<slug:slug>/', views.ProfileDetail.as_view(), name='profile'),
]