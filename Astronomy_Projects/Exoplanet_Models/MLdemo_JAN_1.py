#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 18:41:36 2023

@author: wn
"""

from sklearn.linear_model import PoissonRegressor
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

p = pd.read_csv('Astronomy_Datasets/planets.csv')



sns.scatterplot(x='pl_orbeccen',y='st_mass',data=p)


x = np.array(p['pl_orbeccen'].fillna(0))
y = np.array(p['st_mass'].fillna(0))

X = x[:,np.newaxis]

P = PoissonRegressor(fit_intercept=True)

P.fit(X,y)

x_test = np.linspace(0,1,101)
X_test = x_test[:,np.newaxis]
print(x_test)

y_test = P.predict(X_test)


plt.figure()
sns.scatterplot(x='pl_orbeccen',y='st_mass',data=p)
plt.plot(x_test,y_test)
plt.title("Mass vs. Orbital Eccentricity")

plt.figure()

subset = p[['pl_orbeccen','st_mass']]

c = subset.corr()

sns.heatmap(c,cmap='viridis',annot=True)





