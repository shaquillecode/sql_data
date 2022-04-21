"""""
Country Data scraping exercise:
https://www.scrapethissite.com/pages/simple  (Country data)

Scrape this site for it's country data and create a database / table from the data.

Calculate the population density for each country
ADD that as a column in your table
ALONG with the other information provided on each country

population density = population / km^2

 Additionally Determine the following:

- Which country has the largest population ( using sql)
- Which country has the longest name (using sql)
- Which countries have a population between 30,000 and 500,000? (using sql)
- Which countries have a population greater than 500,000 and start with the letter A? (using sql)
"""

import mysql.connector
from dotenv import dotenv_values
from bs4 import BeautifulSoup
import requests

URL= 'http://www.scrapethissite.com/pages/simple'
result = requests.get(URL)
soup = BeautifulSoup(result.content, 'html.parser')

countries = soup.find_all('div', {'class' : 'col-md-4 country'})
country_info = []
countryName, countryCapital, countryPopulation, countryArea, countryDensity = None, None, 0, None, 0
for country in countries:
    countryName = country.find('h3').getText().strip().lower()
    countryCapital = country.find('span', {'class' : 'country-capital'}).getText().lower()
    countryPopulation = int(country.find('span', {'class' : 'country-population'}).getText())

    area = country.find('span', {'class' : 'country-area'}).getText()
    floatedArea = float(area)
    countryArea = floatedArea

    if countryArea != 0:
        countryDensity = round(countryPopulation / countryArea, 2)

country_info.append((countryName, countryCapital, countryPopulation, countryArea, countryDensity))

config = dotenv_values("1.env")

mydb = mysql.connector.connect(
  host=config['HOST'],
  user=config['USER'],
  password=config['PASS'],
  database='world_data'
)

mycursor = mydb.cursor()

mycursor.execute(''' DROP TABLE countries ''')

mycursor.execute(''' CREATE TABLE countries(
  countryId INT AUTO_INCREMENT PRIMARY KEY,
  country_name VARCHAR(100) NOT NULL,
  country_capital VARCHAR(100) NOT NULL,
  country_population INT NOT NULL,
  country_area REAL NOT NULL, 
  country_density REAL NOT NULL
) ''')


mycursor.executemany(''' INSERT INTO countries(country_name, country_capital, country_population, country_area, country_density) VALUES (%s, %s, %s, %s, %s) ''', country_info)
mydb.commit()

mycursor.execute(''' SELECT country_name, country_population FROM countries ORDER BY country_population DESC LIMIT 1; ''')

for x in mycursor:
    print(x)

mycursor.execute(''' SELECT country_name, country_population FROM countries WHERE country_population BETWEEN 30000 AND 500000; ''')

for x in mycursor:
    print(x)

mycursor.execute(''' SELECT country_name, country_population FROM countries WHERE country_population > 500000 AND country_name LIKE 'a%' ; ''')

for x in mycursor:
    print(x)
