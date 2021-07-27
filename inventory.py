import csv, sqlite3
from pprint import pprint

def main_solution():
	with open('inventory.csv','r') as inv_csv:
		dr = csv.DictReader(inv_csv)
		all_vals = []
		for entry in dr:
			csv_vals = list(entry.values())[:-1]
			price_quantity = round(float(entry['price']) * int(entry['quantity']), 2)
			csv_vals.append(price_quantity)
			all_vals.append(tuple(csv_vals))
		print(all_vals)
	#create database, add new table, drop table if already there.	
	con = sqlite3.connect("hardware_store.db") 
	cur = con.cursor()
	cur.execute("""DROP TABLE inventory""")
	cur.execute("""CREATE TABLE IF NOT EXISTS inventory (
	    item_id TEXT,
	    item TEXT,
	    price REAL,
	    quantity INTEGER,
	   	price_extended REAL)
	""")
	cur.executemany("""INSERT INTO inventory VALUES (?,?,?,?,?)""", all_vals )
	cur.execute("""SELECT * from inventory""")
	data = cur.fetchall()
	pprint(data) 
if __name__ == '__main__':
	main_solution()