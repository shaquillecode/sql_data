'''Library DB reader'''
import os
import sqlite3

print(os.getcwd()) #this gets the working directory
os.chdir('/Users/shaq/Desktop/archive/sql_data/data')#this changes the working directory
print(os.getcwd()) # This show changes

conn = sqlite3.connect(":memory:")
c = conn.cursor()

c.executescript('''
    create table person(
        firstname,
        lastname,
        age
    );

    create table book(
        title,
        author,
        published
    );

    insert into book(title, author, published)
    values (
        'Dirk Gently''s Holistic Detective Agency',
        'Douglas Adams',
        1987
    );
 ''')
conn.commit()
c.close()   # <=== cursor is closed

conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute('select * from book')
r = c.fetchone()
for member in r:
    print(member,type(member))


conn = sqlite3.connect("library.db")
c = conn.cursor()
c.execute('''DROP table books;''')
c.execute('''
    create table IF NOT EXISTS books(
        id TEXT,
        Title TEXT,
        Author TEXT
    );''')
c.execute("""insert into books(id, title, author) values ('001','Outliers','Malcolm Gladwell');""")
c.execute("""insert into books(id, title, author) values ('002','Humble Pie','Matt Parker');""")
c.execute("""insert into books(id, title, author) values ('003','52 Small Changes','Brett Blumenthal');""")
c.execute("""insert into books(id, title, author) values ('004','Blink','Malcolm Gladwell');""")
c.execute("""insert into books(id, title, author) values ('005','The Tipping Point','Malcolm Gladwell');""")
c.execute("""insert into books(id, title, author) values ('006','All the Powers of Earth','Sidney Blumenthal'); """)
conn.commit()

#select entries from books, such that the values are distinct , show us the columns id, title, author
c.execute('SELECT DISTINCT id,title,author FROM books')  # Equivalent to using set() on a list
books = c.fetchall()
for book in books:
    print(book)
    print('='*30)
conn.close()

#set is a collection of distinct objects with no repeated elements
# sets do not have an order
list1 = [1,2,3,4]
list2 =  [1,2,3,4, 4]
set1 = set(list2)
print(set1)
set(list1) == set(list2)
new_list = list(set1)
print(new_list)

conn = sqlite3.connect("library.db")
c = conn.cursor()
c.execute('SELECT ALL count(*) FROM books')  # Counts all values in the table
# c.execute('SELECT count(DISTINCT id) FROM books')  # Counts all values in the table based on the expression
countBooks = c.fetchall()

for cnt in countBooks:
    print(cnt)
    print('='*30)

# c.execute('ALTER TABLE books RENAME TO my_books')

# Rename it back to books
# c.execute('ALTER TABLE my_books RENAME TO books')

conn.commit()
conn.close()

conn = sqlite3.connect("library.db")
c = conn.cursor()
c.execute('ALTER TABLE books RENAME COLUMN title TO sub_title')

# Rename it back
c.execute('ALTER TABLE books RENAME COLUMN sub_title TO title')

c.execute('ALTER TABLE books ADD COLUMN price TEXT') # This can be REAL type as well

c.execute('ALTER TABLE books ADD COLUMN ebook_price REAL') # This can be REAL type as well
conn.commit()
conn.close()

conn = sqlite3.connect("library.db")
c = conn.cursor()
c.execute('''
UPDATE  books SET
price = 12.99
WHERE author = 'Malcolm Gladwell'
''')
c.execute('''
UPDATE  books SET
price = 9.99
WHERE author LIKE '%Blumenthal'
''')
c.execute('''
UPDATE  books SET
price = 7.99
WHERE author = 'Matt Parker'
''')

c.execute('SELECT * FROM books')
updatedBooks = c.fetchall()
for book in updatedBooks:
    print(book)
    print('='*30)
conn.commit()
conn.close()

conn = sqlite3.connect("library.db")
c = conn.cursor()
c.execute('SELECT MIN(CAST(price as REAL)) FROM books')
minBooks = c.fetchall()
for minB in minBooks:
    print(minB)
    print('='*30)

c.execute('SELECT MAX(CAST(price as REAL)) FROM books')
maxBooks = c.fetchall()
for maxB in maxBooks:
    print(maxB)
    print('='*30)
conn.close()

conn = sqlite3.connect("library.db")
c = conn.cursor()
c.execute('SELECT SUM(CAST(price as REAL)) FROM books')
sumPrice = c.fetchall()
for price in sumPrice:
    print(price)
    print('='*30)

c.execute('SELECT AVG(CAST(price as REAL)) FROM books')
avgPrice = c.fetchall()
for avg in avgPrice:
    print(avg)
    print('='*30)
conn.close()
