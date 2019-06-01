from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image


class JboUser(AbstractUser):
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.get_name_for_slug())
        super(JboUser, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('users:profile',
                       kwargs={'slug': self.slug})

    def get_name_for_slug(self):
        return f'{str.lower(self.first_name)}-{str.lower(self.last_name)}'

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/JBO_main.png',
                              upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)