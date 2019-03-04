from cookflixapp.forms import UserProfileForm, UserForm, RecipeForm
from django.shortcuts import render
from django.http import HttpResponse
from cookflixapp.models import Recipe

# Create your views here.
def home(request):
    return render(request, 'cookflixapp/home.html', {})

def about(request):
    return render(request, 'cookflixapp/about.html', {})

def login(request):
    return render(request, 'cookflixapp/login.html', {})

def signup(request):
    return render(request, 'cookflixapp/signup.html', {})

def browse(request):
    recipes = Recipe.objects.all()
    return render(request, 'cookflixapp/browse.html', {'recipes' : recipes })

def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'cookflixapp/recipe.html', {'recipe' : recipe})

def upload(request):

    if request.method == 'POST':
        recipeForm = RecipeForm(data = request.POST)

        if(recipeForm.is_valid()):
            print("Add recipe here..")
        else:
            print(recipeForm.errors)

    else:
        recipeForm = RecipeForm()

    return render(request, 'cookflixapp/upload.html', {'recipe_form': recipeForm})

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

    return render(request ,'cookflixapp/register.html', {'user_form':userForm, 'profile_form':profileForm, 'registered':registered})
