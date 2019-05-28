from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('<category>/', views.PostCategoryListView.as_view(), name='category'),
]