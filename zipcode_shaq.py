import mysql.connector
from dotenv import dotenv_values
from pprint import pprint
from operator import itemgetter

	

def get_digit_frequencies(file='/Users/shaq/Desktop/archive/sql_data/zipcode_data.txt'):

	digits = {}
	zipcodes = []

	total_digits = 0 
	with open(file) as f:
		for line in f.readlines():
			line = line.strip()
			if line.isdigit():
				zipcodes.append(line)
				total_digits += len(line)
				for char in line:
					if char not in digits:
						digits[char] = 0
					digits[char] += 1

	print("=" * 35)
	digit_freqs = {}
	for key, val in sorted(digits.items(), key=itemgetter(1), reverse=True):
		print(f"the digit {key} occurrs { round((val / total_digits) * 100, 2) }")
		digit_freqs[key] = round((val / total_digits) * 100, 2)

	return digit_freqs, zipcodes

config = dotenv_values("/Users/shaq/Desktop/archive/sql_data/1.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

mydb = mysql.connector.connect(
  host=config['HOST'],
  user=config['USER'],
  password=config['PASSWORD'],
  database='zip'
)

mycursor = mydb.cursor()

"""
Lists the number of customers in each country, sorted high to low
"""

query = """ 
CREATE DATABASE IF NOT EXISTS zip;
USE zip;

DROP TABLE IF EXISTS zipcodes;
DROP TABLE IF EXISTS digit_frequencies;

CREATE TABLE IF NOT EXISTS zipcodes
(
  id              INT unsigned NOT NULL AUTO_INCREMENT, 
  zipcode         VARCHAR(150) NOT NULL,                                      
  PRIMARY KEY     (id)  
);

CREATE TABLE IF NOT EXISTS digit_frequencies
(
  id              INT unsigned NOT NULL AUTO_INCREMENT, 
  digit           INT unsigned,
  frequency       float(10,2),                                      
  PRIMARY KEY     (id)  
);
"""

insert_into_query = """
INSERT INTO digit_frequencies(digit, frequency)
VALUES (%s, %s);
"""

insert_into_query2 = """
INSERT INTO zipcodes(zipcode)
VALUES (%s);
"""
mycursor.execute(query, multi=True)
mydb.commit()

#get digit frequencies and zipcodes
digit_freqs, zipcodes = get_digit_frequencies()
print(zipcodes)


# # package frequencies as tuple for insert
data = [(int(k),v) for k, v in digit_freqs.items()] 
# package zipcode  as tuple
zipcodes_tup = [(zipcode,) for zipcode in zipcodes]
#insert into digit frequencies
mycursor.executemany(insert_into_query, data)
print(mycursor.statement)

# #insert into zipcodes 
#mycursor.executemany(insert_into_query2, zipcodes_tup)


mydb.commit()


# for x in mycursor:
#   print(x)

mycursor.close()
mydb.close()