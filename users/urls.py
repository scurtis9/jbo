from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('<int:pk>/', views.ProfileDetail.as_view(), name='profile'),
]