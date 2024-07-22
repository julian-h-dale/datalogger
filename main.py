import hug
from pymongo import MongoClient
from datetime import datetime
import json

db_client = MongoClient('localhost', 27017)
test_collection = db_client.test_db.test_collection
weather_collection = db_client.weather.barometric

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
    return {
        "result": "200 ok"
    }

@hug.get('/happy_birthday')
def happy_birthday(name, age:hug.types.number = 1):
    id  = test_collection.insert_one({'name': name, 'age': age})
    print(id)
    return "happy {age} birthday {name}!".format(**locals())