from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    create_at = models.DateTimeField()
    like = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.title


class ProfileComment(models.Model):
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    like = models.ManyToManyField(User, blank=True)
    create_at = models.DateTimeField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    def __str__(self):
        return self.title