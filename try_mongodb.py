import pymongo.mongo_client
import pymongo.server_api
import os
from pprint import pprint
from datetime import datetime, timezone
import bson 

from dotenv import load_dotenv

load_dotenv()

mongodb_uri=os.environ['MONGODB_URI']
myclient = pymongo.MongoClient(mongodb_uri, server_api=pymongo.server_api.ServerApi('1'))

#TEST CONNECTION
try: 
  myclient.admin.command('ping')
  print("Pinged")
except Exception as e:
  print(e)


#Create a DB - Databases and Collections aren't created until you insert a document into them.
mydb = myclient["mydatabase"]

#Create an db entry - a post // document
post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.now(tz=timezone.utc),
}

# #Insert post // create db and collection// document into collection called posts in mydb
posts = mydb.posts
# post_id = posts.insert_one(post).inserted_id


#Print name of collections
print(list(mydb.list_collection_names()))

# print list of databases
print(myclient.list_database_names())


new_posts = [
    {
        "author": "Mike",
        "text": "Another post!",
        "tags": ["bulk", "insert"],
        "date": datetime(2009, 11, 12, 11, 14),
    },
    {
        "author": "Eliot",
        "title": "MongoDB is fun",
        "text": "and pretty easy too!",
        "date": datetime(2009, 11, 10, 10, 45),
    },
]
result = posts.insert_many(new_posts)

#If you don't use list it returns a cursor. You need to use a for loop to print each one or a list :)
# pprint(list(mydb.posts.find()))
# print(mydb.posts.count_documents({}))
# print(mydb.posts.count_documents({"author": "Eliot"}))

# mydb.posts.delete_many({"author": "Eliot",})

# Get a reference to the 'sample_mflix' database:
db = myclient['sample_mflix']

# # List all the collections in 'sample_mflix':
collections = db.list_collection_names()
for collection in collections:
   print(collection)

# # OR 
# pprint(list(collections))


# Get a reference to the 'movies' collection:
movies = db['movies']

pprint(list(movies.find().limit(3)))

# # Insert a document for the movie 'Parasite':
# insert_result = movies.insert_one({
#       "title": "Parasite",
#       "year": 2020,
#       "plot": "A poor family, the Kims, con their way into becoming the servants of a rich family, the Parks. "
#       "But their easy life gets complicated when their deception is threatened with exposure.",
#       "released": datetime(2020, 2, 7, 0, 0, 0),
#    })

# # Save the inserted_id of the document you just created:
# parasite_id = insert_result.inserted_id
# print("_id of inserted document: {parasite_id}".format(parasite_id=parasite_id))

# Get the document with the title 'Parasite':
#pprint(movies.find_one({'title': 'Parasite'}))

users = db['users']
# pprint(list(users.find().limit(3)))

comments = db['comments']
#pprint(list(comments.find().limit(3)))


# Look up the document you just created in the collection:
# It’s necessary in this case to convert the ObjectId from a string before passing it.
print(movies.find_one({'_id': bson.ObjectId('661bc7bed3e4e1f97167aef5')}))

#pprint(list(movies.find(({'title':'Parasite'}))))

# for document in movies.find({'title': 'Parasite'}):
#    pprint(document)

## Print movies before released before 1920 of the Romance genre
# count = 0
# for document in movies.find({'year': {'$lt': 1920}, 'genres': 'Romance'}):
#    count += 1
#    pprint(document['year'])
# print(f"Count: {count}")

print(list(movies.find({'year': {'$lt': 1920}, 'genres': 'Romance'})))

## Print year of movies release after 2013 of the Comedy genre
# count = 0
# for document in movies.find({'year': {'$gt': 2013}, 'genres': 'Comedy'}):
#    count += 1
#    pprint(document['year'])
# print(f"Count: {count}")

# # Update the document with the correct year:
#update_result = movies.update_one({ '_id': bson.ObjectId('661bc7bed3e4e1f97167aef5')}, {'$set': {"year": 2019}})

# # Print out the updated record to make sure it's correct:
# pprint(movies.find_one({'_id': bson.ObjectId('661bc7bed3e4e1f97167aef5')}))