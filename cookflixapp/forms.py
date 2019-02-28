from django import forms
from cookflixapp.models import UserProfile

class UserProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Full name")
    email = forms.EmailField(max_length=64, help_text="Email")
    password = forms.CharField(max_length=16, help_text="Password")
    picture = forms.ImageField(help_text="Profile picture", required=False)
    userid = forms.CharField(widget=forms.HiddenInput(), initial=0)
    rating = forms.CharField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = UserProfile
        fields = ("name", "email", "password", "picture")
        exclude = ("preferred_cuisune", )

class LoginForm(forms.ModelForm):
    email = forms.CharField(max_length=64, required=True)
    password = forms.CharField(max_length=16, required=True)