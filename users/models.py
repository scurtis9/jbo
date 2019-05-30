from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image


class JboUser(AbstractUser):
    pass

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(default='jbo_main.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)