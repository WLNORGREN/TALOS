#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 18:54:10 2023

@author: wn
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

p = pd.read_csv('Astronomy_Datasets/planets.csv')

print(p.info())

plt.figure()
sns.scatterplot(x='pl_orbper',y='pl_orbsmax',data=p)

plt.figure()

matrix = p[['pl_orbper','pl_orbsmax']]

c = matrix.corr()

sns.heatmap(c,cmap='viridis',annot=True)

l = LinearRegression(fit_intercept=True)


p = p[p['pl_orbper'] < 7000000]

x = np.array(p['pl_orbper'].fillna(0))
X = x[:,np.newaxis]

y = np.array(p['pl_orbsmax'].fillna(0))

l.fit(X,y)

X_test = np.linspace(1,700000,701)
X_test = X_test[:,np.newaxis]

y_test = l.predict(X_test)

plt.figure()
sns.scatterplot(x='pl_orbper',y='pl_orbsmax',data=p)
plt.plot(X_test,y_test)

plt.figure()

matrix = p[['pl_orbper','pl_orbsmax']]

c = matrix.corr()

sns.heatmap(c,cmap='viridis',annot=True)

