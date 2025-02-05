#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:31:40 2025

@author: wln
"""
import sqlite3
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
import numpy as np

planets = pd.read_csv(
    '~/Documents/python_programs/Astronomy_Datasets/planets.csv')

table_name = 'planet_table'

conn = sqlite3.connect('my_database.db')
planets.to_sql(table_name, conn, if_exists='replace', index=False)


print(f"CSV file '{planets}' successfully imported into '{table_name}'")

conn.close()