'''Titanic Passengers'''
import os
import csv
import sqlite3
from pprint import pprint

print(os.getcwd()) #this gets the working directory
os.chdir('/Users/shaq/Desktop/archive/sql_data/data')#this changes the working directory
print(os.getcwd()) # This show changes

#Create a table in titanic database.
conn = sqlite3.connect("titanic.db") #<-- File path can be used here too.

cur = conn.cursor()
cur.execute('''DROP TABLE passengers''')
cur.execute('''CREATE TABLE IF NOT EXISTS passengers(
  PassengerId     TEXT NOT NULL,                
  Name            TEXT NOT NULL,                
  Age             TEXT NOT NULL,                
  PRIMARY KEY     (Passengerid)                         
)''')
for row in cur.execute("""SELECT name FROM sqlite_master"""):
    print(row)
# conn.row_factory = sqlite3.Row #access rows using names like a dictionary row['term_date']
# print(conn.row_factory)
conn.commit()
conn.close() # closed

FILENAME = 'titanic.csv'
with open(FILENAME,'r') as fin:
    conn = sqlite3.connect("titanic.db")

    cur = conn.cursor()
    dr = csv.DictReader(fin)
    # Insert passengers values
    to_insert = [(entry['PassengerId'], entry['Name'], entry['Age']  ) for entry in dr]
    cur.executemany("""INSERT INTO passengers VALUES (?,?,?)""", to_insert)
    conn.commit()
    # Select all passengers
    cur.execute("""SELECT * FROM passengers""")
    passengers = cur.fetchall()
    pprint(passengers)

conn.commit()
conn.close()

# Update
conn = sqlite3.connect("titanic.db")

cur = conn.cursor()
cur.execute("""UPDATE passengers SET
Name = 'Moran, Mr. James', 
Age = 50
WHERE PassengerId = 6""")
cur.execute("""SELECT rowid,* FROM passengers WHERE Name = "Moran, Mr. James" """)
passengers = cur.fetchall()
for passenger in passengers:
    # Use indexing to return the elements of the tuple
    print(passenger)
    print('='*30)

conn.commit()
conn.close()

# Delete
conn = sqlite3.connect("titanic.db")

cur = conn.cursor()
cur.execute("""SELECT * FROM passengers WHERE Name = "Sjostedt, Mr. Ernst Adolf" """)
passengers = cur.fetchall()

cur.execute("""DELETE FROM passengers WHERE Name = "Sjostedt, Mr. Ernst Adolf" """)

for passenger in passengers:
    # Use indexing to return the elements of the tuple
    print(passenger)
    print('='*30)
conn.commit()
conn.close()

# Average age of passengers
conn = sqlite3.connect("titanic.db")

cur = conn.cursor()
cur.execute("""SELECT AVG("Age") FROM passengers""")
passengers = cur.fetchall()

for passenger in passengers:
    # Use indexing to return the elements of the tuple
    print(passenger)
    print('='*30)
conn.commit()
conn.close()
