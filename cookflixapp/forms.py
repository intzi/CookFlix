from django import forms
from django.contrib.auth.models import User
from cookflixapp.models import UserProfile, Recipe

class UserForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password',)

class UserProfileForm(forms.ModelForm):
    ## name = forms.CharField(max_length=128, help_text="Full name")

    email = forms.EmailField(max_length=64, required=False)

    ## password = forms.CharField(max_length=16, help_text="Password")
    picture = forms.ImageField(required=False)
    # preferred_cuisine = forms.CharField(required=True)
    # userid = forms.CharField(widget=forms.HiddenInput(), initial=0)
    # rating = forms.CharField(widget=forms.HiddenInput(), initial=0)

    #first_name = forms.CharField(max_length=20, required=True)
    #last_name = forms.CharField(max_length=20, required=True)
    class Meta:
        model = UserProfile
        fields = ('email', 'picture', 'first_name', 'last_name', 'preferred_cuisine')
        # exclude = ('rating', )

class RecipeForm(forms.ModelForm):

    user_id = forms.CharField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Recipe
        fields = ('title','video_file','thumbnail','cuisine_type', 'description', 'user_id')
