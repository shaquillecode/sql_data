'''Inventory Reader'''
import sqlite3
from pprint import pprint
import os
import csv

print(os.getcwd()) #this gets the working directory
os.chdir('/Users/shaq/Desktop/archive/sql_data/data')#this changes the working directory
print(os.getcwd()) # This show changes

def read_inventory_file(filename='inventory.csv'):
    ''' Reads Inventory csv'''


    with open(filename,'r') as fin:
        dr = csv.DictReader(fin)
        all_vals = []
        for entry in dr:
            csv_vals = list(entry.values())[:-1]
            price_quantity = round(float(entry['price']) * int(entry['quantity']), 2)
            csv_vals.append(price_quantity)
            all_vals.append(tuple(csv_vals))
    return all_vals


print(os.getcwd())

def run_execute():
    '''run_execute'''
    connection = sqlite3.connect("practice_hardware_store.db")

    cursor = connection.cursor()

    cursor.execute("""DROP TABLE inventory""")

    command1 ="""CREATE TABLE IF NOT EXISTS inventory (
	    item_id TEXT,
	    item TEXT,
	    price REAL,
	    quantity INTEGER)
	"""

    cursor.execute(command1)

    cursor.execute("INSERT INTO inventory VALUES ('HM01', 'Hammer', 19.99, 10)")
    cursor.execute("INSERT INTO inventory VALUES ('NL00', 'Nails', 4.99, 5)")
    cursor.execute("INSERT INTO inventory VALUES ('HW02', 'Pliers', 6.99, 2)")
    cursor.execute("INSERT INTO inventory VALUES ('HW10', 'Mop', 8.99, 1)")
    cursor.execute("INSERT INTO inventory VALUES ('HM02', 'Rubber mallet', 14.99, 15)")
    cursor.execute("INSERT INTO inventory VALUES ('NL01', 'Zinc coated Nails', 5.49, 20)")
    cursor.execute("INSERT INTO inventory VALUES ('HW22', 'Needle Nose Pliers', 6.49, 12)")
    cursor.execute("INSERT INTO inventory VALUES ('HW11', 'Swiffer Mop REFILL', 5.99, 30)")
    cursor.execute("INSERT INTO inventory VALUES ('CN01', 'Circular Saw - 12 inch Blade', 29.99, 40)")
    cursor.execute("INSERT INTO inventory VALUES ('NL00', '3 inch Nails', 5.99, 25)")
    cursor.execute("INSERT INTO inventory VALUES ('HW22', 'Plumbing wrench', 12.99, 20)")
    cursor.execute("INSERT INTO inventory VALUES ('HH90', 'Surgical Masks - 50 pack', 10.99, 1000)")


    cursor.execute("""SELECT * from inventory""")
    data = cursor.fetchall()
    pprint(data)
    return data

def generate_sql_from_input(n=3):
    '''Generate sql from input'''

	#amount of entries to input
	#split string by comma, cast to tuple
    rows = []
    while n > 0:
        data = tuple(input("Enter Row Data: ").split(','))
        rows.append(data)
        n -= 1

    return rows


if __name__ == '__main__':
    # for second part
    read_inventory_file()
    run_execute()
	# generate_sql_from_input()
