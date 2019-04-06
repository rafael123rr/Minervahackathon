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

class Food:
    def __init__(self, name, lst):
        self.name = name
        self.ingredients = []
        for x in lst:
            self.ingredients.append(Ingredient(x))


class Ingredient:
    def __init__(self, name):
        self.name = name
        d = get_info(name)
        self.summary = d["summary"]
        self.health = d["health"]


def create_entry(name, ingredients):
    db = myclient.test
    newFood = Food(name, ingredients)
    food_post = {
        "name" : name,
        "ingredients" : []
    }
    for i in newFood.ingredients:


def postTest(term):

    db = myclient.ingredientInfo
    posts = db.posts

    post_data = {
        "title" : term,
    }
    #

    result = posts.insert_one(post_data)

postTest("glucose")

db = myclient.ingredient_info
posts = db.posts
print(posts.find_one({'title': 'glucose'})["_id"])
# x = mycol.insert_one(post_data)
#print(x)
#print(myclient.list_database_names())
