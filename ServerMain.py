import csv
import json
import requests
from bson import Binary, Code
from bson.json_util import dumps
import socket               # Import socket module
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#Open CSV database and put it into MongoDB
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
    
##for item in db.segment.find():
##    print(item['Style'])

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   param = c.recv(1024)
   r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=4156404&APPID=ab6938454e4a68abb2920603ceac03a8')
   if(r.ok):
       weather = json.loads(r.content.decode('utf-8'))
   mintemp = weather['main']['temp_min']
   print(mintemp)
   items = db.segment.find({"MinimumTemp":{"$lt":mintemp}})
   response = ""
   for item in items: 
       response += item['Top'] + ' ' + item['Bottom'] + '\n'
   #response += item['Bottom']
   c.send(response.encode('utf-8'))
   c.close()                # Close the connection
