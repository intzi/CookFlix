from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.contrib.auth import SESSION_KEY,authenticate
from django.core.urlresolvers import reverse
from cookflixapp.models import CUISINE_CHOICES,User,UserProfile,Recipe,Comment,Saved_Recipes,Review,Video
from cookflixapp.forms import RecipeForm


class homeViewTest(TestCase):
    def test_home(self):
        response  = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'Home')
        self.assertContains(response,'Browse')
        self.assertContains(response,'About')

class aboutViewTest(TestCase):
    def test_about(self):
        response  = self.client.get(reverse('about'))

class loginViewTest(TestCase):
    def test_login(self):
        response  = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
class signupViewTest(TestCase):
    def test_register(self):
        response  = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

class browseViewTest(TestCase):
    def test_about(self):
        response  = self.client.get(reverse('browse'))
        self.assertEqual(response.status_code, 200)


class searchViewTest(TestCase):
    def test_search(self):
        response  = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)

class uploadViewTest(TestCase):
    def test_upload(self):
        user = User.objects.create_user('cookflixTestUser','blabla@bla.com', 'badpasword123')
        user = authenticate(username='cookflixTestUser', password='badpasword123')
        user.save()
        c = Client()
        status = c.login(username='cookflixTestUser', password='badpasword123')
        response = c.post('/login/', {'username':'cookflixTestUser', 'password':'badpasword123'})
        response2 = c.get(reverse('upload'))
        self.assertEqual(response2.status_code, 200)

class MyRecipesViewTest(TestCase):
    def test_myRecipes(self):
        user = User.objects.create_user('cookflixTestUser','blabla@bla.com', 'badpasword123')
        user = authenticate(username='cookflixTestUser', password='badpasword123')
        user.save()
        c = Client()
        status = c.login(username='cookflixTestUser', password='badpasword123')
        response = c.post('/login/', {'username':'cookflixTestUser', 'password':'badpasword123'})
        response2 = c.get('/cookflixTestUser/myrecipes/')
        self.assertEqual(response2.status_code, 200)

class LoginFunctionTest(TestCase):
    def test_login(self):
        user = User.objects.create_user('cookflixTestUser','blabla@bla.com', 'badpasword123')
        user = authenticate(username='cookflixTestUser', password='badpasword123')
        user.save()
        c = Client()
        status = c.login(username='cookflixTestUser', password='badpasword123')
        response = c.post('/login/', {'username':'cookflixTestUser', 'password':'badpasword123'})
        self.assertRedirects(response, reverse('home'),302)
        self.assertTrue(status, user.is_active)

class LogoutFunctionTest(TestCase):
    def test_logout(self):
        user = User.objects.create_user('cookflixTestUser','blabla@bla.com', 'badpasword123')
        user = authenticate(username='cookflixTestUser', password='badpasword123')
        user.save()
        c = Client()
        c.login(username='cookflixTestUser', password='badpasword123')
        response = c.get('/logout/')
        c.logout()
        status = user.is_active
        self.assertRedirects(response, reverse('home'),302)
        self.assertTrue(status, False)


# class recipeCommentTest(TestCase):
#     def test_comment(self):
#         user = User.objects.create_user('cookflixTestUser','blabla@bla.com', 'badpasword123')
#         user = authenticate(username='cookflixTestUser', password='badpasword123')
#         user.save()
#         # recipe = Recipe(title='karahi', video_file='v1.mp4', thumbnail='f1.jpg', description='bla', cuisine_type='ITALIAN', user='user')
        
#         c = Client()
#         c.login(username='cookflixTestUser', password='badpasword123')
#         form = RecipeForm({user:'user'})
#         response = c.post('/upload/', form)
#         self.assertEqual(form.title, 'karahi')
        
def createUserAndLogin():
    user = User.objects.create_user('cookflixTestUser','blabla@bla.com', 'badpasword123')
    user = authenticate(username='cookflixTestUser', password='badpasword123')
    user.save()
    c = Client()
    c.login(username='cookflixTestUser', password='badpasword123')