from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


class Course(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('courses:course-detail',
                       kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class TeeBox(models.Model):
    BLACK = 'BLACK'
    BLUE = 'BLUE'
    WHITE = 'WHITE'
    GOLD = 'GOLD'
    TEE_BOX_CHOICES = [
        (BLACK, 'Black'),
        (BLUE, 'Blue'),
        (WHITE, 'White'),
        (GOLD, 'Gold')
    ]
    color = models.CharField(max_length=5,
                             choices=TEE_BOX_CHOICES,
                             default=BLUE
                             )
    rating = models.FloatField()
    slope = models.PositiveSmallIntegerField()
    course = models.ForeignKey('Course',
                               on_delete=models.CASCADE,
                               related_name='teeboxes',
                               related_query_name='teebox')

    class Meta:
        verbose_name_plural = 'Tee Boxes'


class Hole(models.Model):
    number = models.PositiveSmallIntegerField()
    par = models.PositiveSmallIntegerField()
    handicap = models.PositiveSmallIntegerField()
    course = models.ForeignKey('Course',
                               on_delete=models.CASCADE,
                               related_name='holes',
                               related_query_name='hole')
