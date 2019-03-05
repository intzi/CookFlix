from django import forms
from django.contrib.auth.models import User
from cookflixapp.models import UserProfile, Recipe

class UserForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password',)

class UserProfileForm(forms.ModelForm):
    # name = forms.CharField(max_length=128, help_text="Full name")
    # email = forms.EmailField(max_length=64, help_text="Email")
    # password = forms.CharField(max_length=16, help_text="Password")
    # picture = forms.ImageField(help_text="Profile picture", required=False)
    # userid = forms.CharField(widget=forms.HiddenInput(), initial=0)
    rating = forms.CharField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = UserProfile
        fields = ('picture',)
        # exclude = ("preferred_cuisune", )

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title','video_file','thumbnail','cuisine_type', 'description',)
