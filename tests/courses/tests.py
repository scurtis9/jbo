from django.test import TestCase
from django.urls import reverse
from users.models import JboUser
from courses.models import Course, Hole, TeeBox


class CoursesViewTest(TestCase):

    def test_courses_list_view_template(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/courses.html')


class CourseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # cls.user = JboUser.objects.create(email='test@example.com',
        #                                   first_name='Jim',
        #                                   last_name='Beam')
        cls.course = Course.objects.create(name='Test Course')

    def test_course_slug(self):
        assert self.course.slug == 'test-course'

    def test_course_url(self):
        response = self.client.get(self.course.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('courses/course_detail.html')