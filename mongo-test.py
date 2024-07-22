from pymongo import MongoClient
import json
from typing import Any
from bson import ObjectId

class MongoJSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)


client = MongoClient('localhost', 27017)

# get the test collection

collection = client.test_db.test_collection

test = {
    'name': 'julian',
    'age': 35
}

# id = collection.insert_one(test)
# print(id)

# for test in collection.find():
#     print(test)

# for test in collection.find({"name":"bill"}):
#     json.dumps(test, indent=2, default=str)
#     print(test)

curs = collection.find()
data_json = MongoJSONEncoder().encode(list(curs))
print(json.dumps(data_json, indent=2))