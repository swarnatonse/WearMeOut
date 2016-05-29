import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('S://Academic//Fashion//Database.csv', 'r')
reader = csv.DictReader( csvfile )
try:
    mongo_client=MongoClient()
    print("Connected successfully")
except pymongo.errors.ConnectionFailure:
    print("Could not connect: %s" % e)
mongo_client
db=mongo_client.fashion
db.segment.drop()
header= [ "Top", "Bottom", "MinimumTemp", "Style" ]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.segment.insert(row)
    
for item in db.segment.find({"Bottom": "Black Trousers"}):
    print(item['Style'])
