'''World Country Populations'''
import os
import sqlite3

print(os.getcwd()) #this gets the working directory
os.chdir('/Users/shaq/Desktop/archive/sql_data/data')#this changes the working directory
print(os.getcwd()) # This show changes

FN = "world_country_populations.csv" # This is the CSV file name that has the values that we will insert into "world_country_populations.db" database
'''num, country, population, year_change, net_change, density, land_area_km2, migrants, fertility_rate, median_age, urban_pop_pct, world_share'''
DB_NAME = "world_country_populations.db"

# with open(FN,'r') as fh:
#     line = fh.readline()
#     i = 0
#     while line:
#         if i > 0:
#             print(line)
#         line = fh.readline()
#         i += 1
'''CREATE THE DATABASE'''
conn = sqlite3.connect(DB_NAME)
curr = conn.cursor()
curr.executescript('''DROP table pop_data''')
curr.executescript('''
    CREATE TABLE IF NOT EXISTS pop_data(
        num INTEGER,
        country TEXT,
        population INTEGER,
        year_change REAL,
        net_change INTEGER,
        density INTEGER,
        land_area_km2 INTEGER,
        migrants INTEGER,
        fert_rate REAL,
        median_age INTEGER,
        urban_pop_pct REAL,
        world_share REAL
    );
    DELETE FROM pop_data;
''')
conn.commit()

'''CREATE THE TABLE IN A WAY THAT DOES NOT COUNT "N.A." AS A NUMERICAL VALUE'''
with open(FN,'r') as fh:
    line = fh.readline()
    i = 0
    while line:
        if i > 0:
            num,country,population,year_change,net_change,density,land_area_km2,migrants,fert_rate,median_age,\
            urban_pop_pct,world_share = line.split(',')

            # print(f"""{num} {country} {population} {year_change} {net_change} {density} {land_area_km2}
            # {migrants} {fert_rate} {median_age} {urban_pop_pct} {world_share}""")

            num = int(num)
            country = country.strip().replace("'"," ")
            population = int(population)
            year_change = float(year_change)
            net_change = int(net_change)
            density = int(density)
            land_area_km2 = int(land_area_km2)
            migrants = float(migrants) if migrants else 0
            fert_rate = 0 if fert_rate.strip() == 'N.A.' else float(fert_rate)
            median_age = 0 if median_age.strip() == 'N.A.' else float(median_age)
            urban_pop_pct = 0 if urban_pop_pct.strip() == 'N.A.' else float(urban_pop_pct)
            world_share = float(world_share)

            # print(f"""{num} {country} {population} {year_change} {net_change} {density} {land_area_km2}
            # {migrants} {fert_rate} {median_age} {urban_pop_pct} {world_share}""")

            # Store the data
            sql = f"""INSERT INTO pop_data (num,country,population,year_change,net_change,density,land_area_km2,
            migrants,fert_rate,median_age,urban_pop_pct,world_share) 
            VALUES ({num},'{country}',{population},{year_change},{net_change},{density},{land_area_km2},{migrants},
            {fert_rate},{median_age},{urban_pop_pct},{world_share});"""
            # print(sql)
            curr.execute(sql)
            conn.commit()

        line = fh.readline()
        i += 1


curr.execute('''SELECT country, population FROM pop_data ORDER BY population DESC''')
rows = curr.fetchall()
for row in rows:
    print(f'{row[0]} - population in mm {row[1]/1000000}')
conn.close()

print('==='*35)
conn = sqlite3.connect(DB_NAME)
curr = conn.cursor()
curr.execute('''SELECT sum(population) FROM pop_data ORDER BY population DESC''')
rows = curr.fetchall()
for row in rows:
    print(f' The Sum of all countries population is => {row[0]}')
conn.close()

print('==='*35)
conn = sqlite3.connect(DB_NAME)
curr = conn.cursor()
curr.execute('''SELECT country, median_age FROM pop_data ORDER BY median_age DESC LIMIT 10''')
rows = curr.fetchall()
for row in rows:
    print(f'{row[0]} - median age is {row[1]}')
conn.close()

print('==='*35)
conn = sqlite3.connect(DB_NAME)
curr = conn.cursor()
curr.execute('''SELECT country, net_change FROM pop_data WHERE net_change < 0 ORDER BY net_change ASC LIMIT 10''')
rows = curr.fetchall()
for row in rows:
    print(f'{row[0]} - people who left {row[1]}')
conn.close()

print('==='*35)
conn = sqlite3.connect(DB_NAME)
curr = conn.cursor()
curr.execute('''SELECT country, migrants FROM pop_data WHERE migrants > 0 ORDER BY migrants DESC LIMIT 10''')
rows = curr.fetchall()
for row in rows:
    print(f'{row[0]} - migrants {row[1]}')
conn.close()

print('==='*35)
conn = sqlite3.connect(DB_NAME)
curr = conn.cursor()
curr.execute('''SELECT country, population, year_change FROM pop_data WHERE population < 10000000 ORDER BY year_change DESC LIMIT 10''')
rows = curr.fetchall()
for row in rows:
    print(f'{row[0]} - year change {row[2]} - population - {row[1]}')
conn.close()
