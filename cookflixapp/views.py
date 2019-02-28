from cookflixapp.forms import UserProfileForm
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
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'cookflixapp/home.html', {})
        else:
            print(form.errors)
    else:
        return render(request ,'cookflixapp/register.html', {'form':form})