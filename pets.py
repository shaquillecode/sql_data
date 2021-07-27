import csv
from pprint import pprint
# Links: 
# https://docs.python.org/3/library/csv.html (how to read csv in python)

# Write a pure python program that does the following from the CSV file. 

# 1) read the csv file dogs_data.csv 
# 2) return a string as seen below in the output

# input -> csv file


# output-> 

''' 
INSERT INTO cats ( name, owner, birth) VALUES
  ( 'Sandy', 'Lennon', '2015-01-03' ),
  ( 'Cookie', 'Casey', '2013-11-13' ),
  ( 'Charlie', 'River', '2016-05-21' );
''' 


Values = 'Values'
table_name = 'cats'
final_sql_str = " ".join(['INSERT INTO', table_name, '( name, owner, birth )', Values])

with open('dog_data.csv', newline='') as csvfile:
	dogs_data = csv.reader(csvfile, delimiter=' ', quotechar='|')

	comma_counter = 0
	for entry in dogs_data:
		#print(entry)
		final_sql_str += '( ' + "".join(entry) + ' ), '
		comma_counter += 1

	final_sql_str += ';'
	#for entry in dogs_data:
	pprint(final_sql_str)