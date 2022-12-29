#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 13:50:29 2022

@author: wn
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Read Data
s = pd.read_csv('Astronomy_Datasets/stars.csv')

#Define training arrays
X_train = np.array(s['Absolute magnitude(Mv)'])
y_train = np.array(s['Luminosity(L/Lo)'])


X_train = X_train[:,np.newaxis]

#Fit model
l = LinearRegression(fit_intercept=True)
l.fit(X_train,y_train)

#Train model
X_test = np.linspace(-10,20,31)
X_test = X_test[:,np.newaxis]

y_test = l.predict(X_test)

#Graph results
sns.scatterplot(x='Absolute magnitude(Mv)',y='Luminosity(L/Lo)',data=s)
plt.plot(X_test,y_test)

