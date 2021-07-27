import mysql.connector
from dotenv import dotenv_values

config = dotenv_values("1.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password=' ',
  database='chinook'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM album")

for x in mycursor:
  print(x)
mydb.close()

import mysql.connector
from dotenv import dotenv_values

config = dotenv_values("1.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password=' ',
  database='chinook'
)


mycursor = mydb.cursor()

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
mydb.close()

config = dotenv_values("1.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password=' ',
  database='chinook'
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM TRACK LIMIT 10")
for x in mycursor:
  print(x)
print("=" * 30)

mycursor.execute("SELECT * FROM GENRE LIMIT 10")
for x in mycursor:
  print(x)
print("=" * 30)

mycursor.execute('''
SELECT a.name, a.composer, b.name
FROM track AS a
INNER JOIN genre AS b
ON a.genreid = b.genreid
WHERE b.name LIKE 'b%'
LIMIT 10
''')
for x in mycursor:
    print(x)


mydb.close()
import mysql.connector
from dotenv import dotenv_values
config = dotenv_values("1.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password=' ',
  database='chinook'
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM TRACK LIMIT 10")
for x in mycursor:
  print(x)
print("=" * 30)


mycursor.execute("SELECT * FROM GENRE LIMIT 10")
for x in mycursor:
  print(x)
print("=" * 30)

mycursor.execute('''
 SELECT a.name, a.composer, b.name
 FROM Track AS a
 INNER JOIN Genre AS b
 ON a.genreid = b.genreid
 WHERE b.name LIKE 'b%'
 LIMIT 10
 ''')
for x in mycursor:
  print(x)
print("=" * 30)
    

config = dotenv_values("1.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password=' ',
  database='chinook'
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM TRACK LIMIT 10")
for x in mycursor:
  print(x)
print("=" * 30)

mycursor.execute("SELECT * FROM invoiceline LIMIT 10")
for x in mycursor:
  print(x)
print("=" * 30)

mycursor.execute('''
SELECT a.trackid, a.name, a.composer, b.invoicelineid, b.invoiceid
FROM track AS a
LEFT JOIN invoiceline AS b
ON a.trackid = b.trackid;
''')
for x in mycursor:
    print(x)


mydb.close()

config = dotenv_values("1.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password=' ',
  database='chinook'
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM TRACK LIMIT 10")
for x in mycursor:
  print(x)
print("=" * 30)

mycursor.execute("SELECT * FROM invoiceline LIMIT 10")
for x in mycursor:
  print(x)
print("=" * 30)

mycursor.execute('''
SELECT a.trackid, a.name, a.composer, b.invoicelineid, b.invoiceid
FROM track AS a
RIGHT JOIN invoiceline AS b
ON a.trackid = b.trackid;
''')
for x in mycursor:
    print(x)


mydb.close()