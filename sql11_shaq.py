import sqlite3
import csv
import mysql.connector
from dotenv import dotenv_values

config = dotenv_values("1.env")


mydb = mysql.connector.connect(
  host= 'localhost',
  user= 'root',
  password= ' ',
  database='mock_data'
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists mock_data")
mycursor.execute('''DROP TABLE users''')
mycursor.execute('''CREATE TABLE if not exists users  (Id INTEGER,Firstname varchar(20),Lastname varchar(20),email varchar(50),ip_address varchar(20));''')
mydb.commit()
val = []
with open('/Users/shaq/Desktop/archive/sql_data/mock_data.csv', newline='') as csvfile:
	data = csv.DictReader(csvfile)
	for entry in data:
		val.append(tuple(list(entry.values())))
	print(val)
mycursor.executemany('''INSERT INTO users VALUES (%s,%s,%s,%s,%s)''', val)
mydb.commit()