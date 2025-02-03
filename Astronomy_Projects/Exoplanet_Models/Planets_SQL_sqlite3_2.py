#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 12:10:32 2025

@author: wln
"""

import sqlite3
import pandas as pd
import numpy as np

def infer_sql_type(series):
    """Infer SQLite data type based on a Pandas Series."""
    if np.issubdtype(series.dtype, np.integer):
        return "INTEGER"
    elif np.issubdtype(series.dtype, np.floating):
        return "REAL"
    else:
        return "TEXT"

# Step 1: Load CSV
csv_file = '~/Documents/python_programs/Astronomy_Datasets/planets.csv'
table_name = 'inferred_table'
df = pd.read_csv(csv_file)

# Step 2: Infer SQL column types
columns_with_types = [
    f"{col} {infer_sql_type(df[col])}" for col in df.columns
]

# Step 3: Connect to SQLite and create the table
conn = sqlite3.connect('my_database2.db')
cursor = conn.cursor()

# Drop and create the table
create_table_query = f"CREATE TABLE {table_name} ({', '.join(columns_with_types)});"
cursor.execute(f"DROP TABLE IF EXISTS {table_name};")  # Recreate table if it already exists
cursor.execute(create_table_query)

# Step 4: Insert the CSV data into the table
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Step 5: Run an SQL query (e.g., select top 5 rows)
query = f"SELECT AVG(ra), AVG(dec), pl_hostname FROM {table_name} GROUP BY pl_hostname LIMIT 5;"
cursor.execute(query)

# Fetch and display results
results = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]  # Get column names for output

print(f"\nResults of the query:\n{columns}")
for row in results:
    print(row)

# Step 6: Close connection
conn.close()
