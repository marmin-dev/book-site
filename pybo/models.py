from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.contrib.auth.models import User


class Profile(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    image = ProcessedImageField(
        upload_to='images',
        processors=[ResizeToFit(800, 800)],
        format='JPEG',
        options={'quality': 90},
        null=True,
        blank=True)
    create_at = models.DateTimeField()

    def __str__(self):
        return self.title


class ProfileComment(models.Model):
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    like = models.ManyToManyField(User, blank=True)
    create_at = models.DateTimeField()

    def __str__(self):
        return self.title