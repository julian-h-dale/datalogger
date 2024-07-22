from pymongo import MongoClient


client = MongoClient('localhost', 27017)

# get the test collection

collection = client['test-db']['test-collection']

test = {
    'name': 'julian',
    'age': 35
}

collection.