from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pprint

load_dotenv()
uri = os.environ['MONGODB_URI']
client = MongoClient(uri)

db = client.sample_analytics
collection = db.accounts

pipeline = [
    { '$match': { 'limit': { '$lte': 10000 } } },
    { '$group': { '_id': '$products'} }
]

result = collection.aggregate(pipeline)

for doc in result:
    pprint.pprint(doc)
    print('------------------')