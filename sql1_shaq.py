# # import string
# # print(string.ascii_letters)

import sqlite3
import os

# print(os.getcwd()) #this gets the working directory
# os.chdir('/Users/shaq/Desktop/sql_data')#this changes the working directory
# print(os.getcwd()) # This show changes

conn = sqlite3.connect('customer.db')

methods = [x for x in dir(conn) if not x.startswith('_')]
print(methods)


c = conn.cursor()
c.execute("""DROP TABLE customers""")

# Use the IF NOT EXISTS clause if we might have created the table previously
c.execute("""CREATE TABLE IF NOT EXISTS customers (
    fName TEXT,
    lName TEXT,
    address1 TEXT,
    address2 TEXT,
    zip TEXT)
""")
# conn.commit()  # <=== commit our table to the database
# conn.close()

conn = sqlite3.connect('customer.db')
c = conn.cursor()
for row in c.execute("""SELECT name FROM sqlite_master"""):
    print(row)
c.execute("""CREATE TABLE IF NOT EXISTS depts (
    dept_id TEXT,
    dept_name TEXT)
""")
for row in c.execute("""SELECT name FROM sqlite_master"""):
    print(row)
conn.commit()  # <=== commit our table to the database
conn.close()



# Inserting data - one record at a time
conn = sqlite3.connect('customer.db')
c = conn.cursor()
c.execute("""INSERT INTO customers VALUES
('Mary','Jones','15 Main street','','99995')""")
conn.commit()
conn.close()

# Inserting data - multiple records at once
conn = sqlite3.connect('customer.db')
c = conn.cursor()
all_customers = [
    ('Harry','Teague','100 Centre Street','Apt 1A','88888'),
    ('Henrietta','Teague','100 Centre Street','Apt 1A','88888'),
    ('Larry','Gantt','10 Bond Street','Apt 11C','88000'),
    ('Horace','Penn','50 Gansavort Street','Apt 9B','88770'),
    ('Patrice','Wright','60 Brooklyn Bridge Park Street','Apt 44M','11234'),
]
c.executemany("""INSERT INTO customers VALUES (?,?,?,?,?)""", all_customers)
conn.commit()
conn.close()

conn = sqlite3.connect('customer.db')
c = conn.cursor()


# # The asterick allows you to retreive all of the fields
c.execute('SELECT * FROM customers')
data = c.fetchall()
print(data)

# A list of tuples were returned
# Check the data type of the elements in the list
print(data[0])

print(data[0][1]) # Return the last name of the first element in the list
conn.commit()
conn.close()
# Fetchone
conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute('SELECT * FROM customers')
print(c.fetchone())

conn.commit()
conn.close()
# A first record is returned

# fetchmany
conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute('SELECT * FROM customers')
print(c.fetchmany(4))

conn.commit()
conn.close()
# The first four records are returned

conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute('SELECT * FROM customers')
ans = c.fetchone()

# Use indexing to return the elements of the tuple
print(f'First name: {ans[0]}\nLast name: {ans[1]}\nAddress 1: {ans[2]}\nAddress 2: {ans[3]}\nZip: {ans[4]}' )

conn.commit()
conn.close()

conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute('SELECT * FROM customers')
customers = c.fetchall()

# sqlite primary key is automatically created

conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute('SELECT rowid,* FROM customers')  # rowid is now the first element in the returned tuple
customers = c.fetchall()

for customer in customers:
    # Use indexing to return the elements of the tuple
    print(customer)
    print('='*30)

# i = 1
for customer in customers:
    # Use indexing to return the elements of the tuple
    print(f'Customer {customer[0]}')
    print(f'First name: {customer[1]}\nLast name: {customer[2]}\nAddress 1: {customer[3]}\nAddress 2: {customer[4]}\nZip: {customer[5]}' )
    print('='*30)
conn.commit()
conn.close()

conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute('SELECT rowid,* FROM customers WHERE lName = "Jones" ')  # rowid is now the first element in the returned tuple
customers = c.fetchall()

for customer in customers:
    # Use indexing to return the elements of the tuple
    print(customer)
    print('='*30)

# All last names that begin with 'T'
c.execute('SELECT rowid,* FROM customers WHERE lName LIKE "T%" ')  # <== The % sign is used as a wildcard
customers = c.fetchall()

for customer in customers:
    # Use indexing to return the elements of the tuple
    print(customer)
    print('='*30)

c.execute('SELECT rowid,* FROM customers WHERE address1 LIKE "%brooklyn%" ') # Case does not matter 
customers = c.fetchall()


for customer in customers:
    # Use indexing to return the elements of the tuple
    print(customer)
    print('='*30)

conn.commit()
conn.close()

# Notice the defaults for the fields and whereClause
def queryDB(db,table,fields='*',whereClause=''):   
    conn = sqlite3.connect(db if db[-3:] == '.db' else db+'.db')# <=== The .db extension is necessary
    c = conn.cursor()
    sql = '''SELECT {0} FROM {1} {2}'''.format(fields,table,whereClause)
    print(sql)
    c.execute(sql)  
    qResults = c.fetchall()

    for result in qResults:
        print(result)
        print('='*30)
    conn.commit()
    conn.close()
    

queryDB('customer','customers')  
print("*"*35)
queryDB('customer','customers','lName,fName')
print("*"*35)
queryDB('customer','customers','*',"WHERE address2 = '' ")

conn = sqlite3.connect('customer.db')
c = conn.cursor()

# All last names that begin with 'T'
c.execute('SELECT * FROM customers WHERE fName = "Larry" and lName = "Gantt" ')  # <== The % sign is used as a wildcard
customers = c.fetchall()


for customer in customers:
    # Use indexing to return the elements of the tuple
    print(customer)
    print('='*30)

conn.commit()
conn.close()

conn = sqlite3.connect('customer.db') #<--# This opens up the Database again and at the end of instructions put conn.close()
c = conn.cursor()


c.execute('''UPDATE customers SET 
address1 = "1 Park Avenue",
address2 = "Penthouse A"
WHERE fName = "Larry" and lName = "Gantt" ''') 
conn.commit()
c.execute('''SELECT * FROM customers WHERE fName = "Larry" and lName = "Gantt" ''') 
customers = c.fetchall()

for customer in customers:
    # Use indexing to return the elements of the tuple
    print(customer)
    print('='*30)

c.execute('''UPDATE customers SET 
lname = "Jones-Pollard"
WHERE fName = "Mary" and address1 = "15 Main street" ''') 
conn.commit()
c.execute('''SELECT * FROM customers WHERE fName = "Mary" and address1 = "15 Main street" ''') 
customers = c.fetchall()

for customer in customers:
    # Use indexing to return the elements of the tuple
    print(customer)
    print('='*30)

c.execute('''UPDATE customers SET 
address1 = "10 Pineapple street",
address2 = "apt 3B"
WHERE fName = "Henrietta" and lName = "Teague" ''') 
conn.commit()

for customer in customers:
    # Use indexing to return the elements of the tuple
    print(customer)
    print('='*30)

c.execute('''UPDATE customers SET 
address1 = "10 Pineapple street",
address2 = "apt 3B"
WHERE fName = "Harry" and lName = "Teague" ''') 
conn.commit()
c.execute('''SELECT * FROM customers WHERE lName = "Teague" ''') 
customers = c.fetchall()

for customer in customers:
    # Use indexing to return the elements of the tuple
    print(customer)
    print('='*30)

# String Operations
# SUBSTR, TRIM, LTRIM, RTRIM, LENGTH, REPLACE, UPPER, LOWER, INSTR
# String operations can be conducted on a table or a string
conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT SUBSTR('I LOVE PYTHON AND SQL',3,11)''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT TRIM(' SQL   ')''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT LTRIM('         SQL   ')''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT RTRIM('   SQL   ')''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT LENGTH('         SQL   ')''') 
sqlResults = c.fetchall()
print(sqlResults)

# Execute two commands
conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT LENGTH(TRIM('         SQL   '))''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT REPLACE('I LOVE PYTHON','PYTHON','SQL')''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT 'I LOVE PYTHON ' || '- I LOVE SQL' ''') 
sqlResults = c.fetchall()
print(sqlResults)

conn.close()

# We can delete one row in a table by adding a where clause
# We can delete allitems in a table by omitting the where clause
# To remove a table from a database we use the DROP TABLE command
# DROP TABLE [IF EXISTS] [schema_name.]table_name;
'''In case of a database locked issue.
Recreate your database by running the code again and changing the database name to customer1.db
'''