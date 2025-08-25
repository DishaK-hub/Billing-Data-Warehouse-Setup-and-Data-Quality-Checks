# 1. we write data quallity checks to define dunctions to check for anomalies 

from time import time, ctime

#Check for nulls
conn = None 

def run_data_quality_checks(**options):
    print("*" * 50)
    print(ctime())
    
    start_time = time()
    testname = options.pop("testname")
    test = options.pop("test")

    print(f"Starting test {testname}")
    status = test(**options)
    print(f"Finished test {testname}")
    
    print(f"Test passed {status}")
    end_time = time()

    options.pop("conn")
    print("Test Parameters")

    for key,value in options.items():
        print(f"{key} = {value}")
    
    print()
    print("Duration: ", str(end_time - start_time))
    print(ctime())
    print("*" * 50)

    return testname, options.get('table'), options.get('columns'), status

def check_for_nulls(column, table, conn=conn):
    SQL=f'SELECT COUNT(*) FROM "{table}" WHERE {column} IS NULL'
    cursor = conn.cursor()
    cursor.execute(SQL)
    row_count = cursor.fetchone()
    cursor.close()
    return not bool(row_count[0])

def check_for_min_max(column, table, minimum, maximum, conn=conn):
    SQL=f'SELECT COUNT(*) FROM "{table}" WHERE {column} < {minimum} or {column} > {maximum}'
    cursor = conn.cursor()
    cursor.execute(SQL)
    row_count = cursor.fetchone()
    cursor.close()

    return not bool(row_count[0])

def check_for_valid_values(column, table, valid_values=None, conn=conn):
    SQL=f'SELECT DISTINCT({column}) FROM "{table}"'
    cursor = conn.cursor()
    cursor.execute(SQL)
    result = cursor.fetchall()

    actual_values = {x[0] for x in result}
    status = [value in valid_values for value in actual_values] # this is called membership test - For each value in the actual, it checks if the value is an element of the valid_values list and returns boolean.
    cursor.close()
    return all(status)
    

def check_for_duplicates(column, table, conn=conn):
    SQL=f'SELECT COUNT({column}) FROM "{table}" GROUP BY {column} HAVING COUNT({column}) > 1'
    cursor = conn.cursor()
    cursor.execute(SQL)
    row_count = cursor.fetchone()
    cursor.close()
    return not bool(row_count)