from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses'),
    # path('<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('<slug:slug>', views.CourseDetailView.as_view(), name='course-detail'),
    path('manage/<slug:course_slug>', views.manage_course, name='course_manage'),
    path('new/', views.CourseCreateView.as_view(), name='course-create'),
]