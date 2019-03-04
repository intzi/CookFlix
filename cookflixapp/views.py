from cookflixapp.forms import UserProfileForm, UserForm
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'cookflixapp/home.html', {})

def about(request):
    return render(request, 'cookflixapp/about.html', {})

def login(request):
    return render(request, 'cookflixapp/login.html', {})

def signup(request):
    return render(request, 'cookflixapp/signup.html', {})

def register(request):
    registered = False
    
    if request.method == 'POST':
        userForm = UserForm(data = request.POST)
        profileForm = UserProfileForm(data = request.POST)

        if userForm.is_valid() and profileForm.is_valid() :
            user = userForm.save(commit=True)
            user.set_password(user.password)
            user.save()
            profile = profileForm.save(commit = False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True

        else:
            print(userForm.errors, profileForm.errors)
    else:
        userForm = UserForm()
        profileForm = UserProfileForm()

    return render(request ,'cookflixapp/register.html', {'userForm':userForm, 'profileForm':profileForm, 'registered':registered})
