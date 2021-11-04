import os, csv
import sqlite3
from pprint import pprint

conn = sqlite3.connect(":memory:")
curr = conn.cursor()
curr.executescript('''
    create table allData(
        emp_id TEXT,
        marital_status TEXT,
        last_name TEXT,
        first_name TEXT,
        hire_date TEXT,
        gender TEXT,
        dept_id TEXT,
        dept_name TEXT,
        manager_id TEXT,
        status TEXT,
        term_date TEXT,
        region TEXT,
        sick_days_accumulated TEXT,
        sick_day1 TEXT,
        sick_day2 TEXT,
        sick_day3 TEXT
    );
''')
conn.commit()
curr.close()# <=== cursor is closed
conn.row_factory = sqlite3.Row #allows you to access rows using names like a dictionary row['term_date']
curr = conn.cursor()

filePath = '/Users/shaq/Desktop/archive/sql_data/employee_data.csv'
with open(filePath, 'r', encoding='UTF8') as f:
    # create the csv writer
    dr = csv.DictReader(f)
    
    #create lambda for cleaning inner quotes
    clean = lambda x: x.replace("'", "")
    
    #clean "normalize" field names and entries
    #map -> apply a function to every value in the list
    entries = [tuple(map(clean, entry.values())) for entry in dr]
    fieldnames = list(map(clean, dr.fieldnames)) 
    
    
    #create sql statement and execute 
    sql = f"""INSERT INTO allData ({",".join(fieldnames)}) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""    
    curr.executemany(sql, entries)
    
    
    # Employees by gender 
    
    # get all genders from data
    all_genders = [g[0] for g in curr.execute("SELECT DISTINCT gender FROM allData").fetchall()]
    

    
    #fetchone -> returns one row. so 
    # fetchone()[0] -> value of first column in row, 
    # fetchone()[1] -> value of second column in row.
    
    
    # count by gender
    for gender in all_genders:
        curr.execute("SELECT COUNT(gender) FROM allData WHERE gender = '{0}'".format(gender))
        gendered_employee_count = curr.fetchone()[0] #you are only going to have one result
        print(f"{gender} Employee count: { gendered_employee_count }")
    print("=" * 30)
    
    # Employees by Dept. name
    all_depts = [g[0] for g in curr.execute("SELECT DISTINCT dept_name FROM allData").fetchall()]
    
    # count by dept. name
    for dept in all_depts:
        curr.execute("SELECT COUNT(dept_name) FROM allData WHERE dept_name = '{0}'".format(dept))
        dept_employee_count = curr.fetchone()[0]
        print(f"{dept} Employee count: {dept_employee_count }")
    print("=" * 30)
        
    # Employees in last name, first name order 
    all_employees_by_last = [f"{g[0]}, {g[1]}" for g in curr.execute("SELECT last_name, first_name FROM allData ORDER BY last_name").fetchall()]
    print("Employees by Last Name:")
    pprint(all_employees_by_last)
    print("=" * 30)
    
    # Employees in tenure order (active employees only) in descending order
    
    all_employees_by_last = [f"{g[0]}, {g[1]}, {g[2]}" for g in curr.execute("SELECT last_name, first_name, status FROM allData ORDER BY status DESC").fetchall()]
    print("Employees by Status:")
    pprint(all_employees_by_last)
    print("=" * 30)
    
    # Provide a list of employees by manager name in alphabetical order by last name 
    # weak ordering -> which means, sorting by multiple things 
    all_employees_by_last = [f"{g[0]}, {g[1]}, {g[2]}" for g in curr.execute("SELECT last_name, first_name, manager_id FROM allData ORDER BY manager_id, last_name ASC").fetchall()]
    print("Employees by Manager Id and last name:")
    pprint(all_employees_by_last)
    print("=" * 30)
    
    # Provide a list of employees by region
    all_employees_by_last = [f"{g[0]}, {g[1]}, {g[2]}" for g in curr.execute("SELECT last_name, first_name, region FROM allData ORDER BY region").fetchall()]
    print("Employees by region:")
    pprint(all_employees_by_last)
    print("=" * 30)
    
    # Provide a list of employees who have exceeded their allotment of sick days
    sick_days_limit = 3
    #days = [days[0] for days in curr.execute("SELECT DISTINCT sick_days_accumulated FROM allData").fetchall()]
    #print("days", days)
    all_employees_by_last = [f"{g[0]}, {g[1]}, {g[2]}" for g in curr.execute("SELECT last_name, first_name, sick_days_accumulated FROM allData WHERE CAST(sick_days_accumulated as int) > {0}".format(sick_days_limit)).fetchall()]
    print("Employees that exceeded their allotment of sick days:")
    pprint(all_employees_by_last)
    print("=" * 30)
    curr.close()
    

print("My name is {0} {1} and I am {2}".format("Shaquille", "Duggan", "28"))
print(f"My name is Shaquille Duggan and I am 28")

test = '3'
print(type(int(test)))