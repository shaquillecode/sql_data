"""
use pymongo to write a find statement that finds countries that have a population greater than 500,000
use pymongo to write a find statement to calculate the total populations of the following countries [mexico, canada, us, brazil]
use pymongo to write a find statement to find all countries that have a landmass less than 2000 km^2
use pymongo to write a find statement to find the total population of countries not including Russia, USA and China. extra: write a function that allows you to pass in the search parameters to find and returns the results.
"""

import mysql.connector
from dotenv import dotenv_values
from pprint import pprint
from pymongo import MongoClient

config = dotenv_values("sqltopython.env")

mydb = mysql.connector.connect(
  host= 'localhost',
  user= 'root',
  password= ' ',
  database='world_stats'
)

cur = mydb.cursor()
data = []
cur.execute("SELECT * FROM country_data;")
for entry in cur:
    fields = ['id','country_name','country_capital','population','area','density']
    data.append(dict(zip(fields,entry)))
pprint(data)


#add data to mongodb 
client = MongoClient()
world_db = client.world_database
country_collection = world_db.country_collection
country_collection.insert_many(data)

# population greater than 500,000
for post in country_collection.find( { "population": { "$gt": 500000 } } ):
    print(post)

# total populations of the following countries
total_populations = 0
for post in country_collection.find( { "country_name": { "$in":  ["Mexico", "Canada", "USA", "Brazil"] } } ):
    total_populations += post['population']
    
# land mass greater than 2000
for post in country_collection.find( { "area": { "$gt": 2000 } } ):
    print(post)


for post in country_collection.find( { "country_name": { "$nin": ["Mexico", "Canada", "USA", "Brazil"] } } ):
    print(post)

#extra 
def apply_mongo_find(data, query):
    return data.find(query)



def apply_mongo_find(data, query):
    res = []
    for entry in data.find(query):
        res.append(entry)
    return res 


def apply_mongo_find(data, query):
    for entry in data.find(query):
        yield entry 
        
apply_mongo_find(data,{ "population": { "$gt": 500000 } })
apply_mongo_find(data,{ "area": { "$gt": 2000 } } )