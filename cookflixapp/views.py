from cookflixapp.forms import UserProfileForm, UserForm, RecipeForm
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from cookflixapp.models import Recipe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from cookflixapp.webhose_search import run_query

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

@login_required
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
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid() :
            user = user_form.save(commit=True)
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request ,'cookflixapp/register.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def search(request):
        result_list = []

        if request.method == 'POST':
            query = request.POST['query'].strip()
            if query:
                result_list = run_query(query)

        return render(request, 'cookflixapp/search.html', {'result_list': result_list})
