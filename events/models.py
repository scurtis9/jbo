from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils.text import slugify


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(
        default=timezone.now() + timezone.timedelta(days=3)
    )
    venue = models.CharField(max_length=100, null=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)

    def is_past(self):
        if timezone.now() > self.end_date:
            return True
        return False

    def __str__(self):
        return self.title


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_captain = models.BooleanField(verbose_name='Captain', default=False)

    def __str__(self):
        return self.user.get_full_name()
