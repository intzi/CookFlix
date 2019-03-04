from django.db import models
import uuid
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    picture = models.ImageField(upload_to=None, blank=True)
    preferred_cuisine = models.CharField(max_length=10, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    #class ReadonlyMeta:
    #    readonly= ["rating"]

    def __str__(self):
        return self.user.username


class Recipe(models.Model):
    thumbnail = models.ImageField(upload_to=None, blank=True)
    video_path = models.CharField(max_length=30)
    cuisine_type = models.CharField(max_length=10)
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=300)
    taste = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #class ReadonlyMeta:
    #    readonly= ["taste", "difficulty", "price"]

    def __str__(self):
        return self

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self

class Saved_Recipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    taste = models.CharField(max_length=10)
    difficulty = models.CharField(max_length=10)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self
