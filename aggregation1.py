from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pprint

load_dotenv()
uri = os.environ['MONGODB_URI']
client = MongoClient(uri)

db = client.sample_analytics
collection = db.accounts

# pprint.pprint(collection.find_one())

pipeline = [
    { '$match': { 'limit': { '$lte': 10000 } } },
    { '$sort': { 'limit': -1}},
    # { '$group': { '_id': '$products' } },
    { '$project': { 'account_id': 1, 'limit': 1, '_id': 0}}
]

result = collection.aggregate(pipeline)

for doc in result:
    pprint.pprint(doc)