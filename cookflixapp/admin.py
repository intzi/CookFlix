from django.contrib import admin
from cookflixapp.models import UserProfile, Comment, Recipe, Review, Saved_Recipes

# class UserProfileAdmin(admin.ModelAdmin):
    # list_display = ('username', 'email', 'preferred_cuisine', 'rating')

# class CommentAdmin(admin.ModelAdmin):
    # list_display = ('recipeid', 'username', 'message')

# class RecipeAdmin(admin.ModelAdmin):
    # list_display = ('recipeid', 'username', 'video_path', 'cuisine_type', 'description', 'taste', 'difficulty', 'price')

# class ReviewAdmin(admin.ModelAdmin):
    # list_display = ('recipeid', 'username', 'taste', 'difficulty', 'price')

# class Saved_RecipesAdmin(admin.ModelAdmin):
    # list_display = ( 'recipeid')


admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(Saved_Recipes)
