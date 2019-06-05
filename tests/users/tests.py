from django.test import TestCase
from users.models import JboUser, Profile
from django.urls import reverse


class TestJboUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = JboUser.objects.create(
            email='test@example.com', first_name='Jim', last_name='Beam'
        )

    def test_save(self):
        self.assertEquals(self.user.slug, 'jim-beam')
        self.assertEquals(self.user.username, 'jim-beam')

    def test_get_absolute_url(self):
        self.assertEquals(self.user.get_absolute_url(), reverse('users:profile', kwargs={'slug': self.user.slug}))

    def test_get_name_for_slug(self):
        slug_name = f'{str.lower(self.user.first_name)}-{str.lower(self.user.last_name)}'
        self.assertEquals(self.user.slug, slug_name)

    def test_profile_exists(self):
        self.assertIsNotNone(Profile.objects.get(user=self.user))