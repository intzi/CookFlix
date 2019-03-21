from django.db import models
import uuid
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from cookflixapp.global_data import GlobalData

# UserProfile Model is an extension of user to store extra information like first name email etc..
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, default=0)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    preferred_cuisine = models.CharField(max_length=50, choices=GlobalData.cuisine_types(), default='CHINESE')

    def __str__(self):
        return self.user.username


class Recipe(models.Model):
    thumbnail = models.FileField(upload_to="debug/", null=False, verbose_name='Thumbnail Upload', validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg'])])
    video_file= models.FileField(upload_to="debug/", null=False, verbose_name='Video Upload', validators=[FileExtensionValidator(allowed_extensions=['mp4','webm','ogg'])])
    cuisine_type = models.CharField(max_length=10, choices=GlobalData.cuisine_types(), default='CHINESE')
    title = models.CharField(max_length=50, verbose_name='Recipe Name')
    description = models.CharField(max_length=2000)
    ratings = GenericRelation(Rating, related_query_name='rrating')
    taste = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title +":"+str(self.video_file)

    def delete(self, *args, **kwargs):
        self.video_file.delete()
        self.thumbnail.delete()
        super().delete(*args, **kwargs)

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

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

class Video(models.Model):
    name=models.CharField(max_length=500)
