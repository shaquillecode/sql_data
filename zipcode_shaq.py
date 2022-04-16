'''Zip code Digits Frequencies'''
import os
from operator import itemgetter

print(os.getcwd()) #this gets the working directory
os.chdir('/Users/shaq/Desktop/archive/sql_data/data')#this changes the working directory
print(os.getcwd()) # This show changes

def get_digit_frequencies(file='zipcode_data.txt'):
    '''This function will return the Digits Frequencies'''

    digits = {}
    zipcodes = []

    total_digits = 0
    with open(file) as fin:
        for line in fin.readlines():
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

get_digit_frequencies()
