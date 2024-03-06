#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 18:06:08 2023

@author: wn
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import kmeans_plusplus
import seaborn as sns
import pandas as pd

s = pd.read_csv('Astronomy_Datasets/stars.csv')

print(s.info())


sns.scatterplot(x='Temperature (K)',y='Absolute magnitude(Mv)',data=s)



X = np.array(s[['Temperature (K)','Absolute magnitude(Mv)']].fillna(0))




centers, indices = kmeans_plusplus(X,n_clusters=3)

print(centers)
print(indices)




