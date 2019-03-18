from django import forms
from django.contrib.auth.models import User
from cookflixapp.models import UserProfile, Recipe

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

class UserForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password',)

class UserProfileForm(forms.ModelForm):
    ## name = forms.CharField(max_length=128, help_text="Full name")

    #email = forms.EmailField(max_length=64, required=False)

    ## password = forms.CharField(max_length=16, help_text="Password")
    picture = forms.ImageField(required=False)
    # preferred_cuisine = forms.ChoiceField(choices=CUISINE_CHOICES, required=True)
    # userid = forms.CharField(widget=forms.HiddenInput(), initial=0)
    # rating = forms.CharField(widget=forms.HiddenInput(), initial=0)

    #first_name = forms.CharField(max_length=20, required=True)
    #last_name = forms.CharField(max_length=20, required=True)
    class Meta:
        model = UserProfile
        fields = ('email', 'picture', 'first_name', 'last_name', 'preferred_cuisine')
        widgets = {
            'preferred_cuisine': forms.Select(choices=CUISINE_CHOICES,attrs={'class': 'form-control'}),
        }
        # exclude = ('rating', )

class RecipeForm(forms.ModelForm):

    user_id = forms.CharField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Recipe
        fields = ('title','video_file','thumbnail','cuisine_type', 'description', 'user_id')
        widgets = {
            'cuisine_type': forms.Select(choices=CUISINE_CHOICES,attrs={'class': 'form-control'}),
        }
