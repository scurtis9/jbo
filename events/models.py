from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils.text import slugify
from django.conf import settings
from PIL import Image



# Create your models here.
class Event(models.Model):
    """Model to create events.
    Attributes:
        title (str)
        description (str)
        start_date (date)
        end_date (date)
        venue (str)
        slug (str)
    """
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
        super().save(*args, **kwargs)

    def is_past(self):
        if timezone.now() > self.end_date:
            return True
        return False

    def __str__(self):
        return self.title


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_captain = models.BooleanField(verbose_name='Captain', default=False)
    player_card = models.ImageField(upload_to='player_cards', blank=True)

    def __str__(self):
        return self.user.__str__()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.player_card.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.player_card.path)
