from pymongo import MongoClient
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId
import pprint

load_dotenv()
uri = os.environ['MONGODB_URI']
client = MongoClient(uri)

db = client.sample_analytics
collection = db.accounts
update_doc = {'_id': ObjectId('5ca4bbc7a2dd94ee581623e8')}
filter_doc = {'$inc': {'limit': 1000}}

result = collection.find_one(update_doc)
result = collection.update_one(update_doc, filter_doc)
result = collection.find_one(update_doc)

pprint.pprint(result)

update_doc = {'limit': {'$gte': 20000}}
filter_doc = {'$inc': {'limit': 1000}}
# NOTE: just as $inc works $dec does not work

result = collection.find(update_doc)
result = collection.update_many(update_doc, filter_doc)

num_doc = 0
# for doc in result:
#     pprint.pprint(doc)
#     print('------------------')

# got an error here why is that?
print(f'Number of docs found: {result.matched_count}')
print(f'Number of docs updated: {result.modified_count}')
