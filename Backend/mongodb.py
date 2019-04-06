import pymongo
from wiki_info import get_info
import ssl

myclient = pymongo.MongoClient("mongodb+srv://ryan:password22@cluster0-cxijt.gcp.mongodb.net/test?retryWrites=true&ssl=true&ssl_cert_reqs=CERT_NONE")

# food  = {
#     "name" : string,
#     "ingredients" : [list by ID]
#  }

# ingredient = {
#                 "title",
#                 "summary",
#                 "health"
#              }


def create_entry(name, ingredients):
    db = myclient.ingredientInfo
    food_ingredients = db.ingredients
    foods = db.foods

    food_post = {
        "name" : name,
        "ingredients" : []
    }

    for i in ingredients:
        id = food_ingredients.find_one({'name': i})

        if id == None: # if ingredient not in database
            d = get_info(i)
            post_data = {
                "name" : i,
                "info" : d
            }
            result = food_ingredients.insert_one(post_data)

        food_post["ingredients"].append(i)
    result = foods.insert_one(food_post)



def postTest(term):

    db = myclient.ingredientInfo
    posts = db.posts

    post_data = {
        "title" : term,
    }
    #

    result = posts.insert_one(post_data)

lst = ["Water", "Malic Acid", "Absorbic Acid", "xanthan gum"]
create_entry("other", lst)

# db = myclient.test2
# posts = db.ingredients
#
# post_data = {
#     "title" : "water",
#     "info" : get_info("water")
# }
# result = posts.insert_one(post_data)

# postTest("glucose")
#
# db = myclient.ingredient_info
# posts = db.posts
#
# x = posts.find_one({'title': 'apple'})
# if x == None:
#     print("none")
# else:
#     print(x["_id"])
# x = mycol.insert_one(post_data)
#print(x)
#print(myclient.list_database_names())
