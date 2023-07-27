import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
uri = os.environ["MONGODB_URI"]
client = MongoClient(uri)

for db_name in client.list_database_names():
    print(db_name)

client.close()