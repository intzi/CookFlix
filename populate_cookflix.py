import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cookflix.settings')

import django
django.setup()
from cookflixapp.models import UserProfile, Recipe
from django.contrib.auth.models import User

def populate():

    print("!!!!!!!!!!!!!!!!!!!!!!!! POP !!!!!!!!!!!!!!!!!!!")
    cookflix_users = [
        {
            "id" : "1",
            "username" : "user",
            "password" : "password",
            "user_profile" :
            {
                "name" : "Yingjia Li",
                "email" : "yingjia@gmail.com"
            },
            "recipes" :[
            {
                "thumbnail": "cat.jpg",
                "video_path": "https://www.youtube.com/watch?v=jPOxWOE-3Xk",
                "cuisine_type": "Asian",
                "title": "chicken dish",
                "description":"this is a asian chicken dish",
            }
            ]
        }
    ]

    for user in cookflix_users:

        u = add_user(user["username"], user["password"])
        user_profile = user["user_profile"]
        #add_user_profile(u, user_profile["name"], user_profile["email"])
        for recipe in user["recipes"]:
            print(recipe['video_path'])
            add_recipe(user["id"], recipe["title"], recipe["description"], recipe["thumbnail"], recipe["video_path"], recipe["cuisine_type"])

def add_user(username, password):

    u = User.objects.get_or_create(username=username)[0]
    u.password = password
    u.save()

    return u

def add_user_profile(user, name, email):
    #print("########### User: "+user["id"])
    print("########### Name: "+name)
    print("########### Email: "+email)
    up = UserProfile.objects.get_or_create()
    up.name = name
    up.email = email
    up.rating = 0
    up.save()

    return up

def add_recipe(user, title, description, thumbnail, video_path, cuisine_type):

        print(user)
        print(title)
        print(description)

        r = Recipe.objects.get_or_create(title=title, user_id=user)[0]
        r.user_id = user
        r.title = title
        r.description = description
        r.thumbnail = thumbnail
        r.video_path = video_path
        r.cuisine_type = cuisine_type
        r.save()

        return r


# Start execution here!
if __name__ == '__main__':
    print("Starting Cookflix population script...")
    populate()
