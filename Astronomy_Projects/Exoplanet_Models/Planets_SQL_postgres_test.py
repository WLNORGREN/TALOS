#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 12:21:00 2025

@author: wln
"""

import psycopg2
import pandas as pd
import numpy as np
from sqlalchemy import create_engine



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
table_name = 'inferred_table2'
df = pd.read_csv(csv_file)

# Step 2: Infer SQL column types
columns_with_types = [
    f"{col} {infer_sql_type(df[col])}" for col in df.columns
]



try:
    # Connect to PostgreSQL
    connection = psycopg2.connect(
        dbname="test",
        user="wln",
        password="2023$loup",
        host="localhost",  # or '127.0.0.1'
        port="5432"        # Default PostgreSQL port
    )
    
    engine = create_engine('postgresql://wln:2023$loup@localhost:5432/test_db')

    # Create a cursor object
    cursor = connection.cursor()
    
    # Test the connection by fetching the version
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Connected to: {db_version[0]}")
    
    # Create new table for the planets database
    
    create_table_query = f"CREATE TABLE {table_name} ({', '.join(columns_with_types)});"
    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")  # Recreate table if it already exists
    cursor.execute(create_table_query)
    
    

    connection.commit()
    #  Insert the CSV data into the table
    df.to_sql(table_name, engine,if_exists='append', index=False)
    #  Run an SQL query (e.g., select top 10 rows)
    query = f"SELECT * FROM {table_name} LIMIT 10;"
    cursor.execute(query)
    
    # Fetch and display results
    results = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]  # Get column names for output

    print(f"\nResults of the query:\n{columns}")
    for row in results:
        print(row)
    

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed.")
