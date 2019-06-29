# ============================================
# ; Title:  trueworthy-user-service.py
# ; Author: Professor Krasso
# ; Modified By: Lea Trueworthy
# ; Date:  28 June 2019
# ; Description: Exercise 9.2 - learn how to query and create documents in a MongoDB database instance through Python and pymongo.
# ;===========================================

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

user = {

    "first_name": "Black",

    "last_name": "Cat",

    "email": "meowmeow@me.com",

    "employee_id": "1031019",

    "date_created": datetime.datetime.utcnow()

}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "1031019"}))