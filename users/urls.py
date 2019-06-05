from django.urls import path
from django.views.decorators.cache import never_cache


from . import views

app_name = 'users'
urlpatterns = [
    path('<slug:slug>/', never_cache(views.ProfileDetail.as_view()), name='profile'),
    path('view/<slug:slug>/', views.ProfileView.as_view(), name='profile-view'),
]