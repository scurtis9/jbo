from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = MarkdownxField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categories = models.ManyToManyField("Category", related_name="posts")
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post-detail',
                       kwargs={'slug': self.slug})

    def formatted_markdown(self):
        return markdownify(self.content)

    @classmethod
    def recent_posts(cls):
        recent = cls.objects.order_by('-date_posted')[:3]
        return recent

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
