# ============================================
# ; Title:  trueworthy-user-update.py
# ; Author: Professor Krasso
# ; Modified By: Lea Trueworthy
# ; Date:  29 June 2019
# ; Description: how to update and delete documents in a MongoDB database instance through Python and pymongo
# ;===========================================

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

db.users.update_one(

    {"employee_id": "1031019"},

    {

        "$set": {

            "email": "meow.meow@me.com"

        }

    }

)

pprint.pprint(db.users.find_one({"employee_id": "1031019"}))