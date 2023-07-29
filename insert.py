from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.environ['MONGODB_URI']
client = MongoClient(uri)

db = client.sample_analytics
collection = db.accounts
result = collection.insert_one({
    "account_id": 1,
    "limit": 10000,
    "products": [
        "InvestmentStock",
        "InvestmentFund"
    ],
})
print(f'One doc inserted with id: {result.inserted_id}')

result = collection.insert_many([
    {
        "account_id": 2,
        "limit": 20000,
        "products": [
            "InvestmentStock",
            "InvestmentFund"
        ],
    },
    {
        "account_id": 3,
        "limit": 30000,
        "products": [
            "InvestmentStock",
            "InvestmentFund"
        ],
    },
])

print(f'Number of docs inserted: {len(result.inserted_ids)}')
print(f'List of ids inserted: {result.inserted_ids}')

client.close()