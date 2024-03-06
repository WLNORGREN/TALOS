#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:47:21 2023

@author: wn
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


s = pd.read_csv('Astronomy_Datasets/stars.csv')

print(s.head())


plt.figure()

sns.scatterplot(x='Radius(R/Ro)',y='Luminosity(L/Lo)', data=s)

sub = s[s['Radius(R/Ro)'] < 500][['Radius(R/Ro)','Luminosity(L/Lo)']]
sub.columns = ['Radius','Luminosity']

plt.figure()

sns.scatterplot(x='Radius',y='Luminosity', data=sub)

X_train = np.array(sub['Radius'].fillna(0))
X_train = X_train[:,np.newaxis]
y_train = np.array(sub['Luminosity'].fillna(0))

l = LinearRegression(fit_intercept=True)

l.fit(X_train,y_train)

X_test = np.linspace(0,100,1000)
X_test = X_test[:,np.newaxis]
y_test = l.predict(X_test)

plt.figure()

c = sub.corr()

sns.heatmap(c, cmap='viridis', annot=True)


plt.figure()

plt.plot(X_test,y_test)
sns.scatterplot(x='Radius',y='Luminosity',data=sub)