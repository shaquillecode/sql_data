'''mySQLconnector.py'''
import os
import mysql.connector
from dotenv import dotenv_values

print(os.getcwd()) #this gets the working directory
os.chdir('/Users/shaq/Desktop/archive/sql_data/data')#this changes the working directory
print(os.getcwd()) # This show changes

config = dotenv_values("1.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
mydb = mysql.connector.connect(
  host=config['HOST'],
  user=config['USER'],
  password=config['PASS'],
  database='chinook'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM album")

for x in mycursor:
  print(x)
mydb.close()
print("==="*35)

mydb = mysql.connector.connect(
  host=config['HOST'],
  user=config['USER'],
  password=config['PASS'],
  database='chinook'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM GENRE LIMIT 10")
for x in mycursor:
  print(x)
print("==="*35)

mycursor.execute('''
SELECT BillingCountry ,
CASE
    WHEN total > 0  and total <= 7  THEN '0 - 10'
    WHEN total > 7  and total <= 15 THEN '10 - 15'
    WHEN total > 15 and total <= 26 THEN '15 - 26'
    ELSE 'NONE'
END AS Total
FROM invoice
''')

for x in mycursor:
  print(x)
print("==="*35)

mycursor.execute("SELECT * FROM TRACK LIMIT 10")
for x in mycursor:
  print(x)
print("===" * 35)

mycursor.execute("SELECT * FROM invoiceline LIMIT 10")
for x in mycursor:
  print(x)
mydb.close()
print("==="*35)
