from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.CourseListView.as_view(), name='course-list'),
    # path('<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('<slug:slug>', views.CourseDetailView.as_view(), name='course-detail'),
    path('<slug:course_slug>/manage/', views.manage_course, name='course-manage'),
    path('new/', views.CourseCreateView.as_view(), name='course-create'),
]