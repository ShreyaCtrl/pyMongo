from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pprint
from bson.objectid import ObjectId

load_dotenv()
uri = os.environ['MONGODB_URI']
client = MongoClient(uri)

db = client.sample_analytics
collection = db.accounts

delete_doc = {'_id': ObjectId('5ca4bbc7a2dd94ee581623e8')}
pprint.pprint(collection.find_one(delete_doc))

result = collection.delete_one(delete_doc)
print(f'Number of docs deleted: {result.deleted_count}')

delete_doc = {'limit': {'$gte': 20000}}
result = collection.delete_many(delete_doc)

print(f'Number of docs deleted: {result.deleted_count}')