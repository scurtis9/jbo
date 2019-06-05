from django.urls import path
from django.views.decorators.cache import never_cache


from . import views

app_name = 'users'
urlpatterns = [
    path('', views.ProfileListView.as_view(), name='profile-list'),
    path('<slug:slug>/', never_cache(views.ProfileDetailView.as_view()), name='profile'),
    path('view/<slug:slug>/', views.SocialProfileView.as_view(), name='profile-detail'),
]