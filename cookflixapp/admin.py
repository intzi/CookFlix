from django.contrib import admin
from cookflixapp.models import UserProfile, Comment, Recipe, Review, Saved_Recipes

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'preferred_cuisine', 'rating')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user', 'message')

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('user', 'video_file', 'cuisine_type', 'description', 'taste', 'difficulty', 'price')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user', 'taste', 'difficulty', 'price')

class Saved_RecipesAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Saved_Recipes, Saved_RecipesAdmin)
