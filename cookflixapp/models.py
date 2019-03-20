from django.db import models
import uuid
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

CUISINE_CHOICES = (
    ('CHINESE','CHINESE'),
    ('INDIAN','INDIAN'),
    ('ITALIAN','ITALIAN'),
    ('KOREAN','KOREAN'),
    ('SPANISH','SPANISH'),
    ('FRENCH','FRENCH'),
    ('PAKISTANI','PAKISTANI'),
    ('GREEK','GREEK'),
    ('JAPANESE','JAPANESE'),
    ('AMERICAN','AMERICAN'),
    ('BRITISH','BRITISH'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    # preferred_cuisine = models.CharField(max_length=50, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, default=0)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    preferred_cuisine = models.CharField(max_length=50, choices=CUISINE_CHOICES, default='CHINESE')

    #class ReadonlyMeta:
    #    readonly= ["rating"]

    def __str__(self):
        return self.user.username


class Recipe(models.Model):
    thumbnail = models.FileField(upload_to="debug/", null=False, verbose_name='Thumbnail Upload', validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg'])])
    video_file= models.FileField(upload_to="debug/", null=False, verbose_name='Video Upload', validators=[FileExtensionValidator(allowed_extensions=['mp4','webm','ogg'])])
    cuisine_type = models.CharField(max_length=10, choices=CUISINE_CHOICES, default='CHINESE')
    title = models.CharField(max_length=50, verbose_name='Recipe Name')
    description = models.CharField(max_length=2000)
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
