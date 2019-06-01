from django.urls import path, include

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('markdownx/', include('markdownx.urls')),
    path('new/', views.PostCreateView.as_view(), name='post-create'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('<category>/', views.PostCategoryListView.as_view(), name='category')
]