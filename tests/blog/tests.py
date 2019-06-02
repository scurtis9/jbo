from django.test import TestCase

from blog.models import Post, Category, Comment
from users.models import JboUser


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = JboUser.objects.create(email='test@example.com',
                                          first_name='Jim',
                                          last_name='Beam')
        cls.post = Post.objects.create(title='Test Post', author=cls.user)

    def test_post_slug(self):
        assert self.post.slug == 'test-post'


class CategoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = JboUser.objects.create(email='test@example.com',
                                          first_name='Jim',
                                          last_name='Beam')
        cls.post = Post.objects.create(title='Test Post', author=cls.user)
        cls.category = Category.objects.create(name='test')

    def test_category_returns_name(self):
        assert self.category.__str__() == self.category.name


class BlogViewTest(TestCase):
    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('blog/post-list.html')