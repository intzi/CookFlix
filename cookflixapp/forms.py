from django import forms
from django.contrib.auth.models import User
from cookflixapp.models import UserProfile, Recipe, Comment
from cookflixapp.global_data import GlobalData



class UserForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password',)

class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    class Meta:
        model = UserProfile
        fields = ('email', 'picture', 'first_name', 'last_name', 'preferred_cuisine')
        widgets = {
            'preferred_cuisine': forms.Select(choices=GlobalData.cuisine_types(),attrs={'class': 'form-control'}),
        }

class RecipeForm(forms.ModelForm):
    user_id = forms.CharField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = Recipe
        fields = ('title','video_file','thumbnail','cuisine_type', 'description', 'user_id')
        widgets = {
            'cuisine_type': forms.Select(choices=GlobalData.cuisine_types(),attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)
