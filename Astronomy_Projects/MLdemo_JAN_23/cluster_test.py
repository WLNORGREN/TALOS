#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 18:05:47 2023

@author: wn
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans

s = pd.read_csv('Astronomy_Datasets/stars.csv')


sub = s[['Luminosity(L/Lo)', 'Radius(R/Ro)']]

sub.columns = ['Luminosity', 'Radius']

X = np.array(sub['Luminosity'].fillna(0))

X = X[:,np.newaxis]

y = sub['Radius'].fillna(0)

k = KMeans(n_clusters=4)
labels = k.fit_predict(X,y)
print(k.cluster_centers_)

plt.plot()

sns.scatterplot(x='Luminosity', y='Radius', hue=labels, palette='viridis', data=sub)