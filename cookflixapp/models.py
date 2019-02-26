from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    userid = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    picture = models.ImageField(upload_to=None, height_field='picture_width', width_field='picture_height', max_length=255, null=True, blank=True)
    preferred_cuisine = models.CharField(max_length=10)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    class ReadonlyMeta:
        readonly= ["rating"]

    def __str__(self):
        return self.userid

class Comment(models.Model):
    recipeid = models.CharField(max_length=30, unique=True)
    userid = models.CharField(max_length=30)
    message = models.TextField()

class Recipe(models.Model):
    recipeid = models.CharField(max_length=30, unique=True)
    video_path = models.CharField(max_length=30)
    cuisine_type = models.CharField(max_length=10)
    description = models.CharField(max_length=10)
    taste = models.CharField(max_length=10)
    difficulty = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    userid = models.CharField(max_length=30)
    class ReadonlyMeta:
        readonly= ["taste", "difficulty", "price"]

    def __str__(self):
        return self.recipeid


class Saved_Recipes(models.Model):
    userid = models.CharField(max_length=30)
    recipeid = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.recipeid

class Review(models.Model):
    userid = models.CharField(max_length=30)
    recipeid = models.CharField(max_length=30, unique=True)
    taste = models.CharField(max_length=10)
    difficulty = models.CharField(max_length=10)
    price = models.CharField(max_length=10)