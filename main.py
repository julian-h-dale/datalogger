import hug
from pymongo import MongoClient
from datetime import datetime
import json
from typing import Any
from bson import ObjectId


db_client = MongoClient('mongo', 27017)
test_collection = db_client.test_db.test_collection
weather_collection = db_client.weather.barometric


class MongoJSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return str(o)
        return super().default(o)


@hug.get("/datapoint")
def save_data_point(pressure:hug.types.number, temp:hug.types.number, humidity:hug.types.number):
    datapoint = {
        "pressure": pressure,
        "temperature": temp,
        "humidity": humidity,
        "time": datetime.now().strftime('%H:%M'),
        "date": datetime.now().strftime('%Y-%m-%d')
    }
    print(datapoint)
    id = weather_collection.insert_one(datapoint)
    data_json = MongoJSONEncoder().encode(datapoint)
    return json.loads(data_json)

@hug.get("/datareport")
def get_reported_data(date):
    curs = weather_collection.find({"date": date})
    data_json = MongoJSONEncoder().encode(list(curs))
    return json.loads(data_json)


@hug.get("/happy_birthdayreport")
def get_test_report():
    curs = test_collection.find()
    data_json = MongoJSONEncoder().encode(list(curs))
    return json.loads(data_json)

@hug.get('/happy_birthday')
def happy_birthday(name, age:hug.types.number = 1):
    id  = test_collection.insert_one({'name': name, 'age': age, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")})
    print(id)
    return "happy {age} birthday {name}!".format(**locals())