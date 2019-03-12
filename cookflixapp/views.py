from cookflixapp.forms import UserProfileForm, UserForm, RecipeForm
from cookflixapp.models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from cookflixapp.models import Recipe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from cookflixapp.webhose_search import run_query
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    return render(request, 'cookflixapp/home.html', {})

def about(request):
    return render(request, 'cookflixapp/about.html', {})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponseRedirect("Your account is disabled")
        else:
            print("Invalid login details: {0}, {1}".format(username,password))
    else:
        return render(request, 'cookflixapp/login.html', {})

def signup(request):
    return render(request, 'cookflixapp/signup.html', {})

def browse(request):
    recipes = Recipe.objects.all()

    query = request.GET.get("q")
    if query:
        recipes = recipes.filter(title__icontains=query)

    return render(request, 'cookflixapp/browse.html', {'recipes' : recipes })

def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'cookflixapp/recipe.html', {'recipe' : recipe})

@login_required
def upload(request):

    if request.method == 'POST' and request.FILES['video_file']:
        recipeForm = RecipeForm(request.POST, request.FILES)

        if(recipeForm.is_valid()):
            data = recipeForm.cleaned_data
            user_id = data['user_id']

            recipe = recipeForm.save(commit=False)
            recipe.user_id = user_id
            recipe.save()
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


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        #user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            #user_form.save()
            profile_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            #return redirect('settings:profile')
            return redirect('profile', user.username)
        else:
            print(profile_form.errors)
    else:
        #user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=user_profile)
    return render(request, 'cookflixapp/profile.html', {
        'userprofile': user_profile,
        'selecteduser': user,
        'form' : profile_form
    })
