import os
import psycopg2 
import pandas as pd
from tabulate import tabulate 

import mytests 

from dataqualitychecks import check_for_duplicates, check_for_min_max, check_for_nulls, check_for_valid_values, run_data_quality_checks

pgpassword = 'password'
#connection to db 
try:
    conn = psycopg2.connect(
        user = 'kanavikd',
        host = 'localhost',
        port = 5432,
        password = pgpassword,
        database = 'billingDW'
    )

except Exception as e:
    print("DB connection unsuccessful")
    print(e)

else:
    print("DB connection successful !")

#Start of data quality checks 
results = []
tests = {key:value for key,value in mytests.__dict__.items() if key.startswith('test')}
for testname, test in tests.items():
    test['conn'] = conn
    results.append(run_data_quality_checks(**test)) # The **test part is the unpacking operator. It takes all the key-value pairs from the test dictionary and passes them as keyword arguments to the function. 


#printing the results 
df = pd.DataFrame(results)
df.columns = ['Test Name', 'Table', 'Column', 'Test Passed']
print(tabulate(df,headers='keys', tablefmt='psql'))
conn.close()
print('Disconnected from data warehouse')