# Billing Data Warehouse Setup and Data Quality Checks

This repository provides scripts to set up a **Billing Data Warehouse** using PostgreSQL, load sample billing data, and perform **data quality checks** to ensure the integrity of your data.


## Features

- Automated creation of PostgreSQL database and schema.
- Download and extraction of sample billing data files.
- Loading of dimension and fact tables into the data warehouse.
- Verification scripts to confirm successful data load.
- Python-based data quality checks including:
  - Null checks
  - Min/Max value checks
  - Valid value checks
  - Duplicate checks

---

## Prerequisites

- PostgreSQL installed and running
- Python 3.x
- Required Python packages:
  ```bash
  pip install psycopg2 pandas tabulate


## Example output 

+-----------------------+------------+-----------+-------------+
| Test Name             | Table      | Column    | Test Passed |
|-----------------------+------------+-----------+-------------|
| Check for nulls       | DimMonth   | monthid   | True        |
| Check for min and max | DimMonth   | month     | True        |
| Check for duplicates  | DimCustomer| customerid| True        |
...
