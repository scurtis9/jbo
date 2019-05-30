from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('new/', views.PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('<category>/', views.PostCategoryListView.as_view(), name='category')
]