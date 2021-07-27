import csv

with open('World_country_populations.csv', 'r') as csv_file1:
    csv1_reader = csv.reader(csv_file1)

    print(csv1_reader)

    for line in csv1_reader:
       print(line)


import os


with open("World_country_populations.csv",'r') as fh:
    line = fh.readline()
    i = 0
    while line:
        if i > 0:
            print(line)
        line = fh.readline()
        i += 1

import os
import sqlite3


fn = "World_country_populations.csv"
db_name = "world_populations.db"

conn = sqlite3.connect(db_name)
c = conn.cursor()
c.executescript('''
    create table IF NOT EXISTS pop_data(
        num INTEGER,
        country TEXT,
        population INTEGER,
        year_change REAL,
        net_change INTEGER,
        density INTEGER,
        land_area_km INTEGER,
        migrants INTEGER,
        fert_rate REAL,
        median_age INTEGER,
        urban_pop_pct REAL,
        world_share REAL
    );
    DELETE FROM pop_data;    
''')
conn.commit()

# num	Country	population	year_change	net_change	density	land_area_km2	migrants	
# fertility_rate	Median_age	Urban_pop_pct	World_share

with open(fn,'r') as fh:
    line = fh.readline()
    i = 0
    while line:
        if i > 0:
            num,country,population,year_change,net_change,density,land_area_km,migrants,fert_rate,median_age,\
            urban_pop_pct,world_share = line.split(',')
            print(f"""{num} {country} {population} {year_change} {net_change} {density} {land_area_km}
            {migrants} {fert_rate} {median_age} {urban_pop_pct} {world_share}""")
            num = int(num)
            country = country.strip().replace("'"," ")
            population = int(population)
            year_change = float(year_change)
            net_change = int(net_change)
            density = int(density)
            land_area_km = int(land_area_km)
            migrants = float(migrants) if migrants else 0
            fert_rate = 0 if fert_rate.strip() == 'N.A.' else float(fert_rate)
            median_age = 0 if median_age.strip() == 'N.A.' else float(median_age)
            urban_pop_pct = 0 if urban_pop_pct.strip() == 'N.A.' else float(urban_pop_pct)
            world_share = float(world_share)
            
            # Store the data
            sql = f"""INSERT INTO pop_data (num,country,population,year_change,net_change,density,land_area_km,
            migrants,fert_rate,median_age,urban_pop_pct,world_share) 
            VALUES ({num},'{country}',{population},{year_change},{net_change},{density},{land_area_km},{migrants},
            {fert_rate},{median_age},{urban_pop_pct},{world_share});"""
            print(sql)
            c.execute(sql)
            conn.commit()
            
        line = fh.readline()
        i += 1

# CREATE THE DATABASE
import sqlite3, csv, pathlib
path = pathlib.Path()
con = sqlite3.connect('world_country_populations.db')
cur = con.cursor()
cur.executescript("""create table if not exists wcp (
    num integer,
    country text,
    population integer,
    year_change real,
    net_change real,
    density integer,
    land_area_km2 integer,
    migrants integer,
    fert_rate real,
    median_age integer,
    urban_pop_pct real,
    world_share real);
    delete from wcp;
    """)
con.commit()
# CREATE THE TABLE IN A WAY THAT DOES NOT COUNT "N.A." AS A NUMERICAL VALUE
with open('World_country_populations.csv', 'r') as data:
    line = data.readline()
    i = 0
    while line:
        if i > 0:
            num,country,population,year_change,net_change,density,land_area_km2,migrants,fert_rate,median_age,\
            urban_pop_pct,world_share = line.split(',')
            print(f"""{num} {country} {population} {year_change} {net_change} {density} {land_area_km2}
            {migrants} {fert_rate} {median_age} {urban_pop_pct} {world_share}""")
            num = int(num)
            country = country.strip().replace("'"," ")
            population = int(population)
            year_change = float(year_change)
            net_change = int(net_change)
            density = int(density)
            land_area_km2 = int(land_area_km2)
            migrants = float(migrants) if migrants else 0
            fert_rate = 0 if fert_rate.strip() == 'N.A.' else float(fert_rate)
            median_age =  0 if median_age.strip() == 'N.A.' else float(median_age)
            urban_pop_pct =  0 if urban_pop_pct.strip() == 'N.A.' else float(urban_pop_pct)
            world_share = float(world_share)
            sql = f"""INSERT INTO wcp (num,country,population,year_change,net_change,density,land_area_km2,
            migrants,fert_rate,median_age,urban_pop_pct,world_share) 
            VALUES ({num},'{country}',{population},{year_change},{net_change},{density},{land_area_km2},{migrants},
            {fert_rate},{median_age},{urban_pop_pct},{world_share});"""
            print(sql)
            cur.execute(sql)
            con.commit()
        line = data.readline()
        i += 1

import os
import sqlite3


fn = "World_country_populations.csv"

conn = sqlite3.connect("world_populations.db")
c = conn.cursor()
c.execute('''SELECT country, population FROM pop_data ORDER BY population DESC''')
rows = c.fetchall()
for row in rows:
    print(f'{row[0]} - population in mm {row[1]/1000000}') 
conn.close()

import os
import sqlite3

conn = sqlite3.connect("world_populations.db")
c = conn.cursor()
c.execute('''SELECT sum(population) FROM pop_data ORDER BY population DESC''')
rows = c.fetchall()
for row in rows:
    print(f'{row[0]}')
    

import os
import sqlite3


fn = "World_country_populations.csv"

conn = sqlite3.connect("world_populations.db")
c = conn.cursor()
c.execute('''SELECT country, median_age FROM pop_data ORDER BY median_age DESC LIMIT 10''')
rows = c.fetchall()
for row in rows:
    print(f'{row[0]} - median age is {row[1]}') 
conn.close()

import os
import sqlite3


fn = "World_country_populations.csv"

conn = sqlite3.connect("world_populations.db")
c = conn.cursor()
c.execute('''SELECT country, net_change FROM pop_data WHERE net_change < 0 ORDER BY net_change ASC LIMIT 10''')
rows = c.fetchall()
for row in rows:
    print(f'{row[0]} - people who left {row[1]}') 
conn.close()

import os
import sqlite3


fn = "World_country_populations.csv"

conn = sqlite3.connect("world_populations.db")
c = conn.cursor()
['']
c.execute('''SELECT country, migrants FROM pop_data WHERE migrants > 0 ORDER BY migrants DESC LIMIT 10''')
rows = c.fetchall()
for row in rows:
    print(f'{row[0]} - migrants {row[1]}') 
conn.close()

import os
import sqlite3


fn = "World_country_populations.csv"

conn = sqlite3.connect("world_populations.db")
c = conn.cursor()
c.execute('''SELECT country, population, year_change FROM pop_data WHERE population < 10000000 ORDER BY year_change DESC LIMIT 10''')
rows = c.fetchall()
for row in rows:
    print(f'{row[0]} - year change {row[2]} - population - {row[1]}') 
conn.close()

alist = [1,2,3]
3 in alist

import os
import sqlite3


fn = "World_country_populations.csv"

conn = sqlite3.connect("world_populations.db")
c = conn.cursor()

countries = ('Canada', 'France','Germany','Italy','United States','United Kingdom','Japan')

c.execute("""select sum(migrants) from pop_data where country in {0} and migrants > 0""".format(countries))
total_g7_migrants = c.fetchone()[0]
c.execute("""select sum(migrants) from pop_data where migrants > 0""")
total_migrants_world_wide =  c.fetchone()[0]
total_migrants_rest_of_world = total_migrants_world_wide - total_g7_migrants
print(f"Percentage of migrants G7 takes {round((total_g7_migrants/total_migrants_world_wide)*100,2)}")
print(f"Percentage of migrants the rest of the world takes {round((total_migrants_rest_of_world/total_migrants_world_wide)*100,2)}")

for country in countries:
    c.execute("""select sum(migrants) from pop_data where country = '{0}' and migrants > 0""".format(country))
    g_country_count = c.fetchone()[0]
    print(f"Percentage of migrants {country} takes: { round((g_country_count/total_g7_migrants)*100,2 ) }")


# alternate solution 
looking_for = str(20)
stringOfNumbers = '32040230213340205020112'
found_indicies = []
for index, entry in enumerate(stringOfNumbers):
    tmp_str = stringOfNumbers[index:index + 2]
    if tmp_str == looking_for:
        print(f"index: {index}, {tmp_str}")
        found_indicies.append(index)
print("There are {0} - 20's found in the following positions {1}".format(len(found_indicies),found_indicies))