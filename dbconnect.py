#This script establishes the database connectivity and tests it

import os
import psycopg2 

pgpassword='password'
conn = None 

try:
    conn = psycopg2.connect(
        user = "kanavikd",
        password = pgpassword,
        host = 'localhost',
        port = 5432,
        database = 'postgres'
    )

except Exception as e:
    print("Error connecting to data warehouse")
    print(e)

else:
    print("Successfully connected to data warehouse")

finally:
    if conn:
        conn.close()
        print("Connection Closed")