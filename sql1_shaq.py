'''I am performing CRUD operations on the clients database'''
import os, sqlite3

print(os.getcwd()) #this gets the working directory
os.chdir('/Users/shaq/Desktop/archive/sql_data')#this changes the working directory
print(os.getcwd()) # This show changes

conn = sqlite3.connect('clients.db')
c = conn.cursor()
# methods = [x for x in dir(conn) if not x.startswith('_')]
# print(methods)

c.execute("""DROP TABLE customers""")
# Use the IF NOT EXISTS clause if we might have created the table previously
c.execute("""CREATE TABLE IF NOT EXISTS customers (
    fName TEXT,
    lName TEXT,
    address1 TEXT,
    address2 TEXT,
    zip TEXT)
""")
conn.commit()  # <=== commit our table to the database
conn.close()

conn = sqlite3.connect('clients.db')#<--# This opens up the Database again and at the end of instructions put conn.close()
c = conn.cursor()
# for row in c.execute("""SELECT name FROM sqlite_master"""):
#     print(row)

c.execute("""DROP TABLE depts""")
c.execute("""CREATE TABLE IF NOT EXISTS depts (
    dept_id TEXT,
    dept_name TEXT)
""")
for row in c.execute("""SELECT name FROM sqlite_master"""):
    print(row)

conn.commit()
conn.close()


conn = sqlite3.connect('clients.db')
c = conn.cursor()

# Inserting data - one record at a time
c.execute("""INSERT INTO customers VALUES
('Mary','Jones','15 Main street','','99995')""")

# Inserting data - multiple records at once
all_customers = [
    ('Harry','Teague','100 Centre Street','Apt 1A','88888'),
    ('Henrietta','Teague','100 Centre Street','Apt 1A','88888'),
    ('Larry','Gantt','10 Bond Street','Apt 11C','88000'),
    ('Horace','Penn','50 Gansavort Street','Apt 9B','88770'),
    ('Patrice','Wright','60 Brooklyn Bridge Park Street','Apt 44M','11234'),
]
c.executemany("""INSERT INTO customers VALUES (?,?,?,?,?)""", [
    ('Harry','Teague','100 Centre Street','Apt 1A','88888'),
    ('Henrietta','Teague','100 Centre Street','Apt 1A','88888'),
    ('Larry','Gantt','10 Bond Street','Apt 11C','88000'),
    ('Horace','Penn','50 Gansavort Street','Apt 9B','88770'),
    ('Patrice','Wright','60 Brooklyn Bridge Park Street','Apt 44M','11234')
])
# A better way to insert multiple records at once 
# c.executemany("""INSERT INTO customers VALUES (?,?,?,?,?)""", all_customers)


# The asterick allows you to retreive all of the fields
# c.execute('SELECT * FROM customers')
# data = c.fetchall()
# print(data)
# A list of tuples were returned

# Check the data type of the elements in the list
# print(data[0],type(data[0]))

#print(data[0][1]) # Return the last name of the first element in the list

# Fetchone
# c.execute('SELECT * FROM customers')
# print(c.fetchone())
# A first record is returned

# fetchmany
# c.execute('SELECT * FROM customers')
# print(c.fetchmany(3))
# The first three records are returned

conn.commit()
conn.close()

conn = sqlite3.connect('clients.db')
c = conn.cursor()

c.execute('SELECT * FROM customers')
ans = c.fetchone()

# Use indexing to return the elements of the tuple
print(f'First name: {ans[0]}\nLast name: {ans[1]}\nAddress 1: {ans[2]}\nAddress 2: {ans[3]}\nZip: {ans[4]}' )

conn.commit()
conn.close()

# sqlite primary key is automatically created
conn = sqlite3.connect('clients.db')
c = conn.cursor()

c.execute('SELECT rowid,* FROM customers')  # rowid is now the first element in the returned tuple
custData = c.fetchmany(2)

for cdata in custData:
    # Use indexing to return the elements of  tuple or tuples
    print(f'Customer {cdata[0]}')
    print(f'First name: {cdata[1]}\nLast name: {cdata[2]}\nAddress 1: {cdata[3]}\nAddress 2: {cdata[4]}\nZip: {cdata[5]}' )
    print('='*30)
conn.commit()
conn.close()

conn = sqlite3.connect('clients.db')
c = conn.cursor()

c.execute('SELECT rowid,* FROM customers WHERE lName = "Jones" ')  # rowid is now the first element in the returned tuple
custData = c.fetchall()

for cdata in custData:
    # Use indexing to return the elements of  tuple or tuples
    print(f"Last name = Jones : {cdata}")
    print('='*30)

# All last names that begin with 'T'
c.execute('SELECT rowid,* FROM customers WHERE lName LIKE "T%" ')  # <== The % sign is used as a wildcard
custT = c.fetchall()

for cdata in custT:
    # Use indexing to return the elements of  tuple or tuples
    print(f"Last name like T : {cdata}")
    print('='*30)

c.execute('SELECT rowid,* FROM customers WHERE address1 LIKE "%brooklyn%" ') # Case does not matter 
customers_like_bk = c.fetchall()

for cdata in customers_like_bk:
    # Use indexing to return the elements of  tuple or tuples
    print(f"Address1 like brooklyn : {cdata}")
    print('='*30)

conn.commit()
conn.close()

# Notice the defaults for the fields and whereClause
def queryDB(db,table,fields='*',whereClause=''):   
    conn = sqlite3.connect(db if db[-3:] == '.db' else db+'.db')# <=== The .db extension is necessary
    c = conn.cursor()
    sql = '''SELECT {0} FROM {1} {2}'''.format(fields,table,whereClause)
    print(f"This is the initial Query ==> {sql}")
    c.execute(sql)  
    queryResults = c.fetchall()
    # print(queryResults)

    for result in queryResults:
        print(result)
        print('='*30)
    conn.commit()
    conn.close()

    
queryDB('clients','customers')
print("Reults of the First query using the queryDB() Function end ^ above")
print()

queryDB('clients','customers','lName,fName')
print("Reults of the Second query using the queryDB() Function end ^ above")
print()

queryDB('clients','customers','*',"WHERE address2 = '' ")
print("Reults of the Third query using the queryDB() Function end ^ above")
print()

conn = sqlite3.connect('clients.db')
c = conn.cursor()

c.execute('SELECT * FROM customers WHERE fName = "Larry" and lName = "Gantt" ')
theCust = c.fetchall()
# print(theCust) #==> Notice List of Tuple or Tuples
for cust in theCust:
    # Use indexing to return the elements of  tuple or tuples
    print(cust)
    print('='*30)


c.execute('''UPDATE customers SET 
address1 = "1 Park Avenue",
address2 = "Penthouse A"
WHERE fName = "Larry" and lName = "Gantt" ''') 
c.execute('''SELECT * FROM customers WHERE fName = "Larry" and lName = "Gantt" ''') 
updateCust = c.fetchall()
# print(updateCust) #==> Notice List of Tuple or Tuples
for cust in updateCust:
    # Use indexing to return the elements of tuple or tuples
    print(cust)
    print('='*30)


c.execute('''UPDATE customers SET 
lname = "Jones-Pollard"
WHERE fName = "Mary" and address1 = "15 Main street" ''') 
c.execute('''SELECT * FROM customers WHERE fName = "Mary" and address1 = "15 Main street" ''') 
marriedCust = c.fetchall()
for cust in marriedCust:
    # Use indexing to return the elements of tuple or tuples
    print(cust)
    print('='*30)


c.execute('''UPDATE customers SET 
address1 = "10 Pineapple street",
address2 = "apt 3B"
WHERE fName = "Henrietta" and lName = "Teague" ''') 

c.execute('''UPDATE customers SET 
address1 = "10 Pineapple street",
address2 = "apt 3B"
WHERE fName = "Harry" and lName = "Teague" ''') 

c.execute('''SELECT * FROM customers WHERE lName = "Teague" ''') 
custTeague = c.fetchall()
for cust in custTeague:
    # Use indexing to return the elements of the tuple
    print(cust)
    print('='*30)

conn.commit()
conn.close()

# String Operations
# SUBSTR, TRIM, LTRIM, RTRIM, LENGTH, REPLACE, UPPER, LOWER, INSTR
# String operations can be conducted on a table or a string
conn = sqlite3.connect('clients.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT SUBSTR('I LOVE PYTHON AND SQL',3,11)''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('clients.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT TRIM(' SQL   ')''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('clients.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT LTRIM('         SQL   ')''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('clients.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT RTRIM('   SQL   ')''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('clients.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT LENGTH('         SQL   ')''') 
sqlResults = c.fetchall()
print(sqlResults)

# Execute two commands
conn = sqlite3.connect('clients.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT LENGTH(TRIM('         SQL   '))''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('clients.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT REPLACE('I LOVE PYTHON','PYTHON','SQL')''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('clients.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT 'I LOVE PYTHON ' || '- I LOVE SQL' ''') 
sqlResults = c.fetchall()
print(sqlResults)

conn.close()

# We can delete one row in a table by adding a where clause
# We can delete all items in a table by omitting the where clause
# To remove a table from a database we use the DROP TABLE command
# DROP TABLE [IF EXISTS] [schema_name.]table_name;
'''In case of a database locked issue.
Recreate your database by running the code again and changing the database name to customer1.db
'''