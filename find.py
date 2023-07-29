from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pprint

load_dotenv()
uri = os.environ['MONGODB_URI']

client = MongoClient(uri)

find_doc = {
    'limit' : {'$gte' : 20000}
}
db = client.sample_analytics
collection = db.accounts

cursor = collection.find(find_doc)

num_doc = 0
for doc in cursor:
    pprint.pprint(doc)
    num_doc += 1
    print('------------------')

print(f'Number of docs found: {num_doc}')

client.close()