'''pets.py'''
import os
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
print(os.getcwd()) #this gets the working directory
os.chdir('/Users/shaq/Desktop/archive/sql_data/data')#this changes the working directory
print(os.getcwd()) # This show changes

VALUES = 'VALUES'
TABLE_NAME = 'cats'
FINAL_SQL_STR = " ".join([f"""INSERT INTO {TABLE_NAME} (name, owner, birth ) {VALUES}"""])

with open('dog_data.csv', newline='') as csvfile:
    dogs_data = csv.reader(csvfile, delimiter=' ', quotechar='|')

    COMMA_COUNTER = 0
    for entry in dogs_data:
        FINAL_SQL_STR += '( ' + "".join(entry) + ' ), '
        COMMA_COUNTER += 1

    FINAL_SQL_STR += ';'
    pprint(FINAL_SQL_STR)
