import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cookflix.settings')

import django
django.setup()
from cookflixapp.models import UserProfile, Recipe
from django.contrib.auth.models import User

def populate():

    print("!!!!!!!!!!!!!!!!!!!!!!!! POP !!!!!!!!!!!!!!!!!!!")
    cookflix_users = [
        {   "id" : "1",
            "username" : "user",
            "password" : "password",
            "user_profile" :
            {
                "name" : "Yingjia Li",
                "email" : "yingjia@gmail.com"
            },
            "recipes" :
            [
                {
                    "thumbnail": "f1.jpg",
                    "video_path": "v1.mp4",
                    "cuisine_type": "Chinese",
                    "title": "Chinese Kung pao Chicken",
                    "description":"Estimate time:1 h 30 m.4 servings. Ingredients: 1 pound skinless, boneless chicken breast halves - cut into chunks; 2 tablespoons white wine; 2 tablespoons soy sauce; 2 tablespoons sesame oil, divided; 2 tablespoons cornstarch, dissolved in 2 tablespoons water; 1 ounce hot chile paste; 1 teaspoon distilled white vinegar; 2 teaspoons brown sugar; 4 green onions, chopped; 1 tablespoon chopped garlic; 1 (8 ounce) can water chestnuts; 4 ounces chopped peanuts"
                },
                {
                    "thumbnail": "f2.jpg",
                    "video_path": "v2.mp4",
                    "cuisine_type": "Indian",
                    "title": "Butter chicken recipe",
                    "description":"Estimate time:1 h 30 m.6 servings. Ingredients: 1 cup butter, divided1 onion, minced; 1 tablespoon minced garlic1 (15 ounce) can tomato sauce; 3 cups heavy cream; 2 teaspoons salt1 teaspoon cayenne pepper; 1 teaspoon garam masala1 1/2 pounds skinless, boneless chicken breast, cut into bite-sized chunks; 2 tablespoons vegetable oil; 2 tablespoons tandoori masala"
                },
                {
                    "thumbnail": "f3.jpg",
                    "video_path": "v3.mp4",
                    "cuisine_type": "Italian",
                    "title": "Chicken pizza",
                    "description":"Estimate time:55 m.6 servings. Ingredients:2 skinless, boneless chicken breast halves; 1 (10 ounce) can refrigerated pizza crust; 1/2 cup Ranch-style salad dressing; 1 cup shredded mozzarella cheese; 1 cup shredded Cheddar cheese; 1 cup chopped tomatoes; 1/4 cup chopped green onions"
                },
                {
                    "thumbnail": "f4.jpg",
                    "video_path": "v4.mp4",
                    "cuisine_type": "Italian",
                    "title": "Best Italian sausage soup",
                    "description":"Estimate time:6 h 30 m.8 servings. Ingredients:1 1/2 pounds sweet Italian sausage; 2 cloves garlic, minced; 2 small onions, chopped; 2 (16 ounce) cans whole peeled tomatoes; 1 1/4 cups dry red wine; 5 cups beef broth; 1/2 teaspoon dried basil; 1/2 teaspoon dried oregano; 2 zucchini, sliced; 1 green bell pepper, chopped; 3 tablespoons chopped fresh parsley; 1 (16 ounce) package spinach fettuccine pastasalt and pepper to taste"
                },
                {
                    "thumbnail": "f5.jpg",
                    "video_path": "v5.mp4",
                    "cuisine_type": "Korean",
                    "title": "Fried chicken",
                    "description":"Estimate time:4 h 30 m.4 servings. Ingredients:1 pound skinless, boneless chicken thighs, quartered; 1/2 yellow onion, grated4 cloves garlic, minced; 1 teaspoon fine salt; 1/2 teaspoon freshly ground black pepperBatter:3/4 cup cornstarch; 1/2 cup self-rising flour; 1 teaspoon white sugar; 1/2 teaspoon ground black pepper; 1/4 teaspoon salt; 1 cup very cold water, or as neededoil, or as needed"
                },
                {
                    "thumbnail": "f6.jpg",
                    "video_path": "v6.mp4",
                    "cuisine_type": "Spanish",
                    "title": "Viva Madrid chicken",
                    "description":"Estimate time:1 h 30 m.4 servings. Ingredients:1 pound skinless, boneless chicken thighs, quartered; 1/2 yellow onion, grated4 cloves garlic, minced; 1 teaspoon fine salt; 1/2 teaspoon freshly ground black pepperBatter:3/4 cup cornstarch; 1/2 cup self-rising flour; 1 teaspoon white sugar; 1/2 teaspoon ground black pepper; 1/4 teaspoon salt; 1 cup very cold water, or as neededoil, or as needed"
                },
                {
                    "thumbnail": "f7.jpg",
                    "video_path": "v7.mp4",
                    "cuisine_type": "French",
                    "title": "Cruchy onion chicken",
                    "description":"Estimate time:1 h 30 m.4 servings. Ingredients:1 pound skinless, boneless chicken thighs, quartered; 1/2 yellow onion, grated4 cloves garlic, minced; 1 teaspoon fine salt; 1/2 teaspoon freshly ground black pepperBatter:3/4 cup cornstarch; 1/2 cup self-rising flour; 1 teaspoon white sugar; 1/2 teaspoon ground black pepper; 1/4 teaspoon salt; 1 cup very cold water, or as neededoil, or as needed"
                },
                {
                    "thumbnail": "f8.jpg",
                    "video_path": "v8.mp4",
                    "cuisine_type": "Pakistani",
                    "title": "Potato chicken",
                    "description":"Estimate time:55 m.6 servings. Ingredients:2 skinless, boneless chicken breast halves; 1 (10 ounce) can refrigerated pizza crust; 1/2 cup Ranch-style salad dressing; 1 cup shredded mozzarella cheese; 1 cup shredded Cheddar cheese; 1 cup chopped tomatoes; 1/4 cup chopped green onions"
                },
                {
                    "thumbnail": "f9.jpg",
                    "video_path": "v9.mp4",
                    "cuisine_type": "Bahrain",
                    "title": "Chicken Parmesan",
                    "description":"Estimate time:55 m.6 servings. Ingredients:2 skinless, boneless chicken breast halves; 1 (10 ounce) can refrigerated pizza crust; 1/2 cup Ranch-style salad dressing; 1 cup shredded mozzarella cheese; 1 cup shredded Cheddar cheese; 1 cup chopped tomatoes; 1/4 cup chopped green onions"
                },
                {
                    "thumbnail": "f10.jpg",
                    "video_path": "v10.mp4",
                    "cuisine_type": "Japanese",
                    "title": "Oyakodon chicken",
                    "description":"Estimate time:1 h 30 m.6 servings. Ingredients: 1 cup butter, divided1 onion, minced; 1 tablespoon minced garlic1 (15 ounce) can tomato sauce; 3 cups heavy cream; 2 teaspoons salt1 teaspoon cayenne pepper; 1 teaspoon garam masala1 1/2 pounds skinless, boneless chicken breast, cut into bite-sized chunks; 2 tablespoons vegetable oil; 2 tablespoons tandoori masala"
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
